from pathlib import Path

import pytest

from engine.schema_loader import (
    SchemaDefinitionError,
    SchemaLoader,
)
from engine.type_registry import TypeRegistry
from validator.schema import SchemaValidator


def test_list_accepts_exact_min_items():
    registry = TypeRegistry()

    assert registry.validate(
        "list",
        ["a", "b"],
        min_items=2,
    )


def test_list_accepts_more_than_min_items():
    registry = TypeRegistry()

    assert registry.validate(
        "list",
        ["a", "b", "c"],
        min_items=2,
    )


def test_list_rejects_fewer_than_min_items():
    registry = TypeRegistry()

    assert not registry.validate(
        "list",
        ["a"],
        min_items=2,
    )


def test_min_items_zero_accepts_empty_list():
    registry = TypeRegistry()

    assert registry.validate(
        "list",
        [],
        min_items=0,
    )


@pytest.mark.parametrize(
    "value",
    [
        -1,
        1.5,
        "1",
        True,
    ],
)
def test_type_registry_rejects_invalid_min_items(value):
    registry = TypeRegistry()

    assert not registry.validate(
        "list",
        [],
        min_items=value,
    )


def _write_schema(
    root: Path,
    field_definition: str,
) -> None:
    entities = root / "entities"
    entities.mkdir(parents=True)

    (root / "entity_schema.yaml").write_text(
        """
entity:
  required:
    - id
    - type
    - name
  optional: []
fields:
  id:
    type: string
  type:
    type: string
  name:
    type: string
relationships: {}
""".lstrip(),
        encoding="utf-8",
    )

    (entities / "example.yaml").write_text(
        f"""
entity_type: example
required:
  - values
optional: []
fields:
  values:
{field_definition}
relationships: {{}}
""".lstrip(),
        encoding="utf-8",
    )


def test_schema_loader_accepts_valid_min_items(tmp_path):
    _write_schema(
        tmp_path,
        """    type: list
    min_items: 1
""",
    )

    loader = SchemaLoader(
        schema_root=tmp_path
    )

    schema = loader.get_schema("example")

    assert (
        schema["fields"]["values"]["min_items"]
        == 1
    )


@pytest.mark.parametrize(
    "yaml_value",
    [
        "-1",
        "1.5",
        '"1"',
        "null",
        "true",
    ],
)
def test_schema_loader_rejects_invalid_min_items(
    tmp_path,
    yaml_value,
):
    _write_schema(
        tmp_path,
        f"""    type: list
    min_items: {yaml_value}
""",
    )

    with pytest.raises(
        SchemaDefinitionError,
        match="min_items",
    ):
        SchemaLoader(
            schema_root=tmp_path
        )


@pytest.mark.parametrize(
    "field_type",
    [
        "string",
        "object",
    ],
)
def test_schema_loader_rejects_min_items_on_non_list(
    tmp_path,
    field_type,
):
    _write_schema(
        tmp_path,
        f"""    type: {field_type}
    min_items: 1
""",
    )

    with pytest.raises(
        SchemaDefinitionError,
        match="min_items.*only valid for list fields",
    ):
        SchemaLoader(
            schema_root=tmp_path
        )


def test_nested_list_enforces_min_items(
    tmp_path,
    monkeypatch,
):
    _write_schema(
        tmp_path,
        """    type: object
    fields:
      groups:
        type: list
        min_items: 2
        items:
          type: string
    required:
      - groups
    optional: []
""",
    )

    loader = SchemaLoader(
        schema_root=tmp_path
    )

    monkeypatch.setattr(
        "validator.schema.SchemaLoader",
        lambda: loader,
    )

    validator = SchemaValidator()

    result = validator.validate(
        {
            "id": "example.one",
            "type": "example",
            "name": "Example",
            "values": {
                "groups": [
                    "one",
                ],
            },
        }
    )

    assert not result.valid
    assert any(
        "values.groups" in error
        for error in result.errors
    )


def test_existing_list_items_constraint_still_works():
    registry = TypeRegistry()

    assert registry.validate(
        "list",
        [
            "console",
            "handheld",
        ],
        items={
            "type": "string",
            "enum": [
                "console",
                "handheld",
            ],
        },
    )

    assert not registry.validate(
        "list",
        [
            "console",
            "toaster",
        ],
        items={
            "type": "string",
            "enum": [
                "console",
                "handheld",
            ],
        },
    )
