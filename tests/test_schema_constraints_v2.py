from pathlib import Path

import pytest

from engine.schema_loader import (
    SchemaDefinitionError,
    SchemaLoader,
)


def _write_common_schema(
    root: Path,
) -> None:

    (root / "entity_schema.yaml").write_text(
        """
schema_version: 1.0

entity:
  required:
    - id
    - type
    - name

  optional:
    - aliases
    - relationships
    - metadata

types:
  test:
    description: Test entity

fields:
  id:
    type: string

  type:
    type: string

  name:
    type: string

  aliases:
    type: list

  relationships:
    type: object

  metadata:
    type: object
""".lstrip(),
        encoding="utf-8",
    )


def _write_entity_schema(
    root: Path,
    body: str,
) -> None:

    entity_dir = (
        root
        / "entities"
    )

    entity_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    (
        entity_dir
        / "test.yaml"
    ).write_text(
        body.lstrip(),
        encoding="utf-8",
    )


def _make_loader(
    tmp_path: Path,
    body: str,
) -> SchemaLoader:

    _write_common_schema(
        tmp_path
    )

    _write_entity_schema(
        tmp_path,
        body,
    )

    return SchemaLoader(
        schema_root=tmp_path
    )


def test_valid_string_enum_schema_loads(
    tmp_path,
):

    loader = _make_loader(
        tmp_path,
        """
required: []

optional:
  - category

fields:
  category:
    type: string
    enum:
      - console
      - handheld

relationships: {}
""",
    )

    schema = loader.get_schema(
        "test"
    )

    assert (
        schema["fields"]["category"]["enum"]
        == [
            "console",
            "handheld",
        ]
    )


def test_enum_must_be_list(
    tmp_path,
):

    with pytest.raises(
        SchemaDefinitionError
    ):

        _make_loader(
            tmp_path,
            """
required: []

optional:
  - category

fields:
  category:
    type: string
    enum: console

relationships: {}
""",
        )


def test_enum_must_not_be_empty(
    tmp_path,
):

    with pytest.raises(
        SchemaDefinitionError
    ):

        _make_loader(
            tmp_path,
            """
required: []

optional:
  - category

fields:
  category:
    type: string
    enum: []

relationships: {}
""",
        )


def test_string_enum_values_must_be_strings(
    tmp_path,
):

    with pytest.raises(
        SchemaDefinitionError
    ):

        _make_loader(
            tmp_path,
            """
required: []

optional:
  - category

fields:
  category:
    type: string
    enum:
      - console
      - 123

relationships: {}
""",
        )


def test_valid_list_items_schema_loads(
    tmp_path,
):

    loader = _make_loader(
        tmp_path,
        """
required: []

optional:
  - regions

fields:
  regions:
    type: list
    items:
      type: string
      enum:
        - north-america
        - japan

relationships: {}
""",
    )

    schema = loader.get_schema(
        "test"
    )

    assert (
        schema["fields"]["regions"]["items"]
        == {
            "type": "string",
            "enum": [
                "north-america",
                "japan",
            ],
        }
    )


def test_items_must_be_mapping(
    tmp_path,
):

    with pytest.raises(
        SchemaDefinitionError
    ):

        _make_loader(
            tmp_path,
            """
required: []

optional:
  - regions

fields:
  regions:
    type: list
    items: string

relationships: {}
""",
        )


def test_items_requires_type(
    tmp_path,
):

    with pytest.raises(
        SchemaDefinitionError
    ):

        _make_loader(
            tmp_path,
            """
required: []

optional:
  - regions

fields:
  regions:
    type: list
    items:
      enum:
        - japan

relationships: {}
""",
        )


def test_items_rejects_unknown_type(
    tmp_path,
):

    with pytest.raises(
        SchemaDefinitionError
    ):

        _make_loader(
            tmp_path,
            """
required: []

optional:
  - regions

fields:
  regions:
    type: list
    items:
      type: imaginary

relationships: {}
""",
        )


def test_nested_enum_values_must_match_item_type(
    tmp_path,
):

    with pytest.raises(
        SchemaDefinitionError
    ):

        _make_loader(
            tmp_path,
            """
required: []

optional:
  - regions

fields:
  regions:
    type: list
    items:
      type: string
      enum:
        - japan
        - 123

relationships: {}
""",
        )


def test_unconstrained_list_remains_valid(
    tmp_path,
):

    loader = _make_loader(
        tmp_path,
        """
required: []

optional:
  - tags

fields:
  tags:
    type: list

relationships: {}
""",
    )

    schema = loader.get_schema(
        "test"
    )

    assert (
        schema["fields"]["tags"]["type"]
        == "list"
    )


def test_enum_rejected_for_non_string_field(
    tmp_path,
):

    with pytest.raises(
        SchemaDefinitionError
    ):

        _make_loader(
            tmp_path,
            """
required: []

optional:
  - generation

fields:
  generation:
    type: integer
    enum:
      - 4
      - 5

relationships: {}
""",
        )


def test_items_rejects_entity_reference_type(
    tmp_path,
):

    with pytest.raises(
        SchemaDefinitionError
    ):

        _make_loader(
            tmp_path,
            """
required: []

optional:
  - manufacturers

fields:
  manufacturers:
    type: list
    items:
      type: entity_reference

relationships: {}
""",
        )


def test_items_rejects_entity_reference_list_type(
    tmp_path,
):

    with pytest.raises(
        SchemaDefinitionError
    ):

        _make_loader(
            tmp_path,
            """
required: []

optional:
  - references

fields:
  references:
    type: list
    items:
      type: entity_reference_list

relationships: {}
""",
        )


def test_entity_reference_list_remains_valid_field_type(
    tmp_path,
):

    loader = _make_loader(
        tmp_path,
        """
required: []

optional:
  - manufacturer

fields:
  manufacturer:
    type: entity_reference_list
    entity_type: test

relationships: {}
""",
    )

    schema = loader.get_schema(
        "test"
    )

    assert (
        schema["fields"]["manufacturer"]["type"]
        == "entity_reference_list"
    )
