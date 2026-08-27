from pathlib import Path

import pytest
import yaml

from engine.entity_reference import EntityReferenceValidator
from engine.schema_loader import (
    SchemaDefinitionError,
    SchemaLoader,
)


class FakeRegistry:

    def __init__(self):
        self.entities = {
            "platform.test": {
                "id": "platform.test",
                "type": "platform",
            },
            "emulator.test": {
                "id": "emulator.test",
                "type": "emulator",
            },
            "core.test": {
                "id": "core.test",
                "type": "core",
            },
            "frontend.test": {
                "id": "frontend.test",
                "type": "frontend",
            },
        }

    def get(self, entity_id):
        return self.entities.get(entity_id)


def test_entity_reference_preserves_singular_entity_type():
    validator = EntityReferenceValidator(
        registry=FakeRegistry(),
    )

    assert validator.validate(
        "emulator.test",
        entity_type="emulator",
    )

    assert not validator.validate(
        "core.test",
        entity_type="emulator",
    )


def test_entity_reference_accepts_allowed_entity_types():
    validator = EntityReferenceValidator(
        registry=FakeRegistry(),
    )

    assert validator.validate(
        "emulator.test",
        entity_types=[
            "emulator",
            "core",
        ],
    )

    assert validator.validate(
        "core.test",
        entity_types=[
            "emulator",
            "core",
        ],
    )


def test_entity_reference_rejects_type_outside_allowed_entity_types():
    validator = EntityReferenceValidator(
        registry=FakeRegistry(),
    )

    assert not validator.validate(
        "frontend.test",
        entity_types=[
            "emulator",
            "core",
        ],
    )


def test_entity_reference_rejects_unknown_reference_with_entity_types():
    validator = EntityReferenceValidator(
        registry=FakeRegistry(),
    )

    assert not validator.validate(
        "emulator.missing",
        entity_types=[
            "emulator",
            "core",
        ],
    )


def test_entity_reference_rejects_conflicting_type_constraints():
    validator = EntityReferenceValidator(
        registry=FakeRegistry(),
    )

    with pytest.raises(ValueError):
        validator.validate(
            "emulator.test",
            entity_type="emulator",
            entity_types=[
                "emulator",
                "core",
            ],
        )


def _write_schema_root(
    tmp_path: Path,
    field_definition: dict,
) -> Path:

    root = tmp_path / "schemas"
    entity_dir = root / "entities"

    entity_dir.mkdir(
        parents=True,
    )

    common = {
        "schema_version": 1.0,
        "entity": {
            "required": [
                "id",
                "type",
                "name",
            ],
            "optional": [],
        },
        "types": {
            "compatibility": {
                "description": "Compatibility claim",
            },
        },
        "fields": {
            "id": {
                "type": "string",
                "required": True,
            },
            "type": {
                "type": "string",
                "required": True,
            },
            "name": {
                "type": "string",
                "required": True,
            },
        },
    }

    entity_schema = {
        "required": [
            "implementation",
        ],
        "optional": [],
        "fields": {
            "implementation": field_definition,
        },
        "relationships": {},
    }

    (
        root / "entity_schema.yaml"
    ).write_text(
        yaml.safe_dump(
            common,
            sort_keys=False,
        ),
        encoding="utf-8",
    )

    (
        entity_dir / "compatibility.yaml"
    ).write_text(
        yaml.safe_dump(
            entity_schema,
            sort_keys=False,
        ),
        encoding="utf-8",
    )

    minimal_schema = {
        "required": [],
        "optional": [],
        "fields": {},
        "relationships": {},
    }

    for entity_type in (
        "platform",
        "emulator",
        "core",
        "frontend",
    ):
        (
            entity_dir
            / f"{entity_type}.yaml"
        ).write_text(
            yaml.safe_dump(
                minimal_schema,
                sort_keys=False,
            ),
            encoding="utf-8",
        )

    return root


def test_schema_loader_accepts_entity_types_constraint(
    tmp_path,
):
    root = _write_schema_root(
        tmp_path,
        {
            "type": "entity_reference",
            "entity_types": [
                "emulator",
                "core",
            ],
        },
    )

    loader = SchemaLoader(
        schema_root=root,
    )

    definition = loader.get_schema(
        "compatibility"
    )["fields"]["implementation"]

    assert definition["entity_types"] == [
        "emulator",
        "core",
    ]


@pytest.mark.parametrize(
    "entity_types",
    [
        [],
        "emulator",
        [""],
        ["emulator", ""],
        ["emulator", "emulator"],
    ],
)
def test_schema_loader_rejects_invalid_entity_types_constraint(
    tmp_path,
    entity_types,
):
    root = _write_schema_root(
        tmp_path,
        {
            "type": "entity_reference",
            "entity_types": entity_types,
        },
    )

    with pytest.raises(SchemaDefinitionError):
        SchemaLoader(
            schema_root=root,
        )


def test_schema_loader_rejects_entity_type_and_entity_types_together(
    tmp_path,
):
    root = _write_schema_root(
        tmp_path,
        {
            "type": "entity_reference",
            "entity_type": "emulator",
            "entity_types": [
                "emulator",
                "core",
            ],
        },
    )

    with pytest.raises(SchemaDefinitionError):
        SchemaLoader(
            schema_root=root,
        )


def test_existing_singular_reference_schemas_still_load():
    loader = SchemaLoader()

    platform = loader.get_schema(
        "platform"
    )

    assert (
        platform["relationships"]
        ["supports_core"]
        ["entity_type"]
        == "core"
    )

    core = loader.get_schema(
        "core"
    )

    assert (
        core["relationships"]
        ["supports"]
        ["entity_type"]
        == "platform"
    )


def test_schema_loader_rejects_unknown_entity_types_target(
    tmp_path,
):
    root = _write_schema_root(
        tmp_path,
        {
            "type": "entity_reference",
            "entity_types": [
                "emulator",
                "missing_type",
            ],
        },
    )

    with pytest.raises(
        SchemaDefinitionError
    ):
        SchemaLoader(
            schema_root=root,
        )


def test_schema_loader_accepts_singular_field_entity_type(
    tmp_path,
):
    root = _write_schema_root(
        tmp_path,
        {
            "type": "entity_reference",
            "entity_type": "emulator",
        },
    )

    loader = SchemaLoader(
        schema_root=root,
    )

    definition = loader.get_schema(
        "compatibility"
    )["fields"]["implementation"]

    assert (
        definition["entity_type"]
        == "emulator"
    )


def test_schema_loader_rejects_unknown_singular_field_target(
    tmp_path,
):
    root = _write_schema_root(
        tmp_path,
        {
            "type": "entity_reference",
            "entity_type": "missing_type",
        },
    )

    with pytest.raises(
        SchemaDefinitionError
    ):
        SchemaLoader(
            schema_root=root,
        )


def test_schema_loader_rejects_entity_types_on_non_reference_field(
    tmp_path,
):
    root = _write_schema_root(
        tmp_path,
        {
            "type": "string",
            "entity_types": [
                "emulator",
                "core",
            ],
        },
    )

    with pytest.raises(
        SchemaDefinitionError
    ):
        SchemaLoader(
            schema_root=root,
        )
