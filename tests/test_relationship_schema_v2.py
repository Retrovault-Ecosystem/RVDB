"""
=========================================================
RVDB Relationship Schema Definition Tests
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/test_relationship_schema_v2.py

Foundation Release:
    0.2

Checkpoint:
    C3 — Schema-Driven Relationships

=========================================================
"""

from pathlib import Path

import pytest

from engine.schema_loader import (
    SchemaDefinitionError,
    SchemaLoader,
)


COMMON_SCHEMA = """
entity:
  required:
    - id
    - type
    - name

fields:

  id:
    type: string

  type:
    type: string

  name:
    type: string
"""


def _write_schema_root(
    tmp_path: Path,
    schemas: dict[str, str],
) -> Path:

    schema_root = (
        tmp_path
        / "schemas"
    )

    entity_root = (
        schema_root
        / "entities"
    )

    entity_root.mkdir(
        parents=True
    )

    (
        schema_root
        / "entity_schema.yaml"
    ).write_text(
        COMMON_SCHEMA,
        encoding="utf-8",
    )

    for (
        entity_type,
        content,
    ) in schemas.items():

        (
            entity_root
            / f"{entity_type}.yaml"
        ).write_text(
            content,
            encoding="utf-8",
        )

    return schema_root


def test_valid_relationship_schema(
    tmp_path,
):

    schema_root = _write_schema_root(
        tmp_path,
        {
            "developer": """
required: []
optional: []
fields: {}
""",
            "game": """
required: []
optional: []
fields: {}

relationships:

  developed_by:
    type: entity_reference_list
    entity_type: developer
""",
        },
    )

    loader = SchemaLoader(
        schema_root
    )

    relationships = (
        loader.get_relationships(
            "game"
        )
    )

    assert (
        relationships[
            "developed_by"
        ][
            "entity_type"
        ]
        == "developer"
    )


def test_invalid_relationship_type(
    tmp_path,
):

    schema_root = _write_schema_root(
        tmp_path,
        {
            "developer": """
required: []
optional: []
fields: {}
""",
            "game": """
required: []
optional: []
fields: {}

relationships:

  developed_by:
    type: nonsense
    entity_type: developer
""",
        },
    )

    with pytest.raises(
        SchemaDefinitionError,
        match="invalid relationship type",
    ):

        SchemaLoader(
            schema_root
        )


def test_missing_target_type(
    tmp_path,
):

    schema_root = _write_schema_root(
        tmp_path,
        {
            "game": """
required: []
optional: []
fields: {}

relationships:

  developed_by:
    type: entity_reference_list
""",
        },
    )

    with pytest.raises(
        SchemaDefinitionError,
        match="must define a target entity type",
    ):

        SchemaLoader(
            schema_root
        )


def test_unknown_target_entity_type(
    tmp_path,
):

    schema_root = _write_schema_root(
        tmp_path,
        {
            "game": """
required: []
optional: []
fields: {}

relationships:

  developed_by:
    type: entity_reference_list
    entity_type: developer
""",
        },
    )

    with pytest.raises(
        SchemaDefinitionError,
        match="unknown target entity type",
    ):

        SchemaLoader(
            schema_root
        )


def test_relationship_definition_must_be_mapping(
    tmp_path,
):

    schema_root = _write_schema_root(
        tmp_path,
        {
            "game": """
required: []
optional: []
fields: {}

relationships:

  developed_by: developer
""",
        },
    )

    with pytest.raises(
        SchemaDefinitionError,
        match="definition must be a mapping",
    ):

        SchemaLoader(
            schema_root
        )


def test_relationships_block_must_be_mapping(
    tmp_path,
):

    schema_root = _write_schema_root(
        tmp_path,
        {
            "game": """
required: []
optional: []
fields: {}

relationships:
  - developed_by
""",
        },
    )

    with pytest.raises(
        SchemaDefinitionError,
        match="'relationships' must be a mapping",
    ):

        SchemaLoader(
            schema_root
        )


def test_entity_type_and_entity_types_cannot_both_exist(
    tmp_path,
):

    schema_root = _write_schema_root(
        tmp_path,
        {
            "developer": """
required: []
optional: []
fields: {}
""",
            "publisher": """
required: []
optional: []
fields: {}
""",
            "game": """
required: []
optional: []
fields: {}

relationships:

  created_by:
    type: entity_reference_list
    entity_type: developer
    entity_types:
      - publisher
""",
        },
    )

    with pytest.raises(
        SchemaDefinitionError,
        match="not both",
    ):

        SchemaLoader(
            schema_root
        )


def test_multiple_target_types_supported(
    tmp_path,
):

    schema_root = _write_schema_root(
        tmp_path,
        {
            "platform": """
required: []
optional: []
fields: {}
""",
            "hardware": """
required: []
optional: []
fields: {}
""",
            "manufacturer": """
required: []
optional: []
fields: {}

relationships:

  produces:
    type: entity_reference_list
    entity_types:
      - platform
      - hardware
""",
        },
    )

    loader = SchemaLoader(
        schema_root
    )

    relationship = (
        loader.get_relationships(
            "manufacturer"
        )[
            "produces"
        ]
    )

    assert relationship[
        "entity_types"
    ] == [
        "platform",
        "hardware",
    ]
