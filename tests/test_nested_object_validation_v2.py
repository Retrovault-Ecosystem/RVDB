"""
=========================================================
RVDB Nested Object Validation Tests
=========================================================

Project:
    RetroVault Database (RVDB)

Checkpoint:
    P2B4-B.26.64

Purpose:
    Verify generic schema-driven structured object
    validation without changing legacy unconstrained
    object behavior.
=========================================================
"""

from validator.schema import SchemaValidator


def _validator_with_schema(monkeypatch, schema):
    validator = SchemaValidator()

    monkeypatch.setattr(
        validator.loader,
        "get_schema",
        lambda entity_type: schema,
    )

    return validator


def _schema(field_definition):
    return {
        "required": [
            "id",
            "type",
            "name",
        ],
        "optional": [
            "evidence",
        ],
        "fields": {
            "id": {
                "type": "string",
            },
            "type": {
                "type": "string",
            },
            "name": {
                "type": "string",
            },
            "evidence": field_definition,
        },
        "relationships": {},
    }


def _entity(evidence):
    return {
        "id": "test.example",
        "type": "test",
        "name": "Example",
        "evidence": evidence,
    }


def _evidence_definition():
    return {
        "type": "list",
        "items": {
            "type": "object",
            "required": [
                "source",
                "reference",
            ],
            "optional": [
                "date_checked",
                "version",
                "notes",
            ],
            "fields": {
                "source": {
                    "type": "string",
                },
                "reference": {
                    "type": "string",
                },
                "date_checked": {
                    "type": "string",
                },
                "version": {
                    "type": "string",
                },
                "notes": {
                    "type": "string",
                },
            },
        },
    }


def test_plain_object_remains_unconstrained(
    monkeypatch,
):
    validator = _validator_with_schema(
        monkeypatch,
        _schema(
            {
                "type": "object",
            }
        ),
    )

    result = validator.validate(
        _entity(
            {
                "anything": {
                    "remains": "allowed",
                }
            }
        )
    )

    assert result.valid
    assert result.errors == []


def test_valid_structured_object_list(
    monkeypatch,
):
    validator = _validator_with_schema(
        monkeypatch,
        _schema(
            _evidence_definition()
        ),
    )

    result = validator.validate(
        _entity(
            [
                {
                    "source": "official",
                    "reference": "https://example.invalid",
                    "date_checked": "2026-08-27",
                    "version": "1.0",
                    "notes": "Verified",
                }
            ]
        )
    )

    assert result.valid
    assert result.errors == []


def test_optional_nested_fields_may_be_omitted(
    monkeypatch,
):
    validator = _validator_with_schema(
        monkeypatch,
        _schema(
            _evidence_definition()
        ),
    )

    result = validator.validate(
        _entity(
            [
                {
                    "source": "official",
                    "reference": "manual",
                }
            ]
        )
    )

    assert result.valid
    assert result.errors == []


def test_missing_nested_required_field_has_path(
    monkeypatch,
):
    validator = _validator_with_schema(
        monkeypatch,
        _schema(
            _evidence_definition()
        ),
    )

    result = validator.validate(
        _entity(
            [
                {
                    "source": "official",
                }
            ]
        )
    )

    assert not result.valid
    assert (
        "evidence[0].reference: "
        "Missing required field"
        in result.errors
    )


def test_unknown_nested_field_has_path(
    monkeypatch,
):
    validator = _validator_with_schema(
        monkeypatch,
        _schema(
            _evidence_definition()
        ),
    )

    result = validator.validate(
        _entity(
            [
                {
                    "source": "official",
                    "reference": "manual",
                    "unexpected": "value",
                }
            ]
        )
    )

    assert not result.valid
    assert (
        "evidence[0].unexpected: "
        "Unknown field"
        in result.errors
    )


def test_invalid_nested_type_has_path(
    monkeypatch,
):
    validator = _validator_with_schema(
        monkeypatch,
        _schema(
            _evidence_definition()
        ),
    )

    result = validator.validate(
        _entity(
            [
                {
                    "source": "official",
                    "reference": 123,
                }
            ]
        )
    )

    assert not result.valid
    assert (
        "evidence[0].reference: "
        "Expected string"
        in result.errors
    )


def test_invalid_object_item_has_indexed_path(
    monkeypatch,
):
    validator = _validator_with_schema(
        monkeypatch,
        _schema(
            _evidence_definition()
        ),
    )

    result = validator.validate(
        _entity(
            [
                "not-an-object",
            ]
        )
    )

    assert not result.valid
    assert (
        "evidence[0]: Expected object"
        in result.errors
    )


def test_nested_list_recurses(
    monkeypatch,
):
    definition = {
        "type": "object",
        "required": [
            "labels",
        ],
        "optional": [],
        "fields": {
            "labels": {
                "type": "list",
                "items": {
                    "type": "string",
                },
            },
        },
    }

    validator = _validator_with_schema(
        monkeypatch,
        _schema(definition),
    )

    result = validator.validate(
        _entity(
            {
                "labels": [
                    "one",
                    2,
                ]
            }
        )
    )

    assert not result.valid
    assert (
        "evidence.labels[1]: "
        "Expected string"
        in result.errors
    )


def test_schema_loader_accepts_structured_object(
    tmp_path,
):
    from engine.schema_loader import SchemaLoader

    schema_root = tmp_path / "schemas"
    entity_dir = schema_root / "entities"
    entity_dir.mkdir(parents=True)

    (schema_root / "entity_schema.yaml").write_text(
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
""",
        encoding="utf-8",
    )

    (entity_dir / "test.yaml").write_text(
        """
required: []
optional:
  - evidence

fields:
  evidence:
    type: list
    items:
      type: object
      required:
        - source
      optional:
        - notes
      fields:
        source:
          type: string
        notes:
          type: string
""",
        encoding="utf-8",
    )

    loader = SchemaLoader(
        schema_root=schema_root,
    )

    evidence = (
        loader.get_schema("test")
        ["fields"]
        ["evidence"]
    )

    assert (
        evidence["items"]["type"]
        == "object"
    )

    assert (
        evidence["items"]["required"]
        == ["source"]
    )


def test_schema_loader_rejects_missing_nested_fields_mapping(
    tmp_path,
):
    import pytest

    from engine.schema_loader import (
        SchemaDefinitionError,
        SchemaLoader,
    )

    schema_root = tmp_path / "schemas"
    entity_dir = schema_root / "entities"
    entity_dir.mkdir(parents=True)

    (schema_root / "entity_schema.yaml").write_text(
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
""",
        encoding="utf-8",
    )

    (entity_dir / "test.yaml").write_text(
        """
required: []
optional:
  - evidence

fields:
  evidence:
    type: object
    required:
      - source
""",
        encoding="utf-8",
    )

    with pytest.raises(
        SchemaDefinitionError
    ):

        SchemaLoader(
            schema_root=schema_root,
        )


def test_schema_loader_rejects_undeclared_required_nested_field(
    tmp_path,
):
    import pytest

    from engine.schema_loader import (
        SchemaDefinitionError,
        SchemaLoader,
    )

    schema_root = tmp_path / "schemas"
    entity_dir = schema_root / "entities"
    entity_dir.mkdir(parents=True)

    (schema_root / "entity_schema.yaml").write_text(
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
""",
        encoding="utf-8",
    )

    (entity_dir / "test.yaml").write_text(
        """
required: []
optional:
  - evidence

fields:
  evidence:
    type: object
    required:
      - source
    fields:
      notes:
        type: string
""",
        encoding="utf-8",
    )

    with pytest.raises(
        SchemaDefinitionError
    ):

        SchemaLoader(
            schema_root=schema_root,
        )


def test_schema_loader_preserves_legacy_boolean_required_object(
    tmp_path,
):
    from engine.schema_loader import SchemaLoader

    schema_root = (
        tmp_path
        / "schemas"
    )

    entity_dir = (
        schema_root
        / "entities"
    )

    entity_dir.mkdir(
        parents=True
    )

    (
        schema_root
        / "entity_schema.yaml"
    ).write_text(
        """
entity:
  required:
    - id
    - type
    - name
  optional:
    - relationships

fields:
  id:
    type: string
  type:
    type: string
  name:
    type: string
  relationships:
    type: object
    required: false
    description: Legacy unconstrained object field
""",
        encoding="utf-8",
    )

    (
        entity_dir
        / "test.yaml"
    ).write_text(
        """
required: []
optional: []
fields: {}
relationships: {}
""",
        encoding="utf-8",
    )

    loader = SchemaLoader(
        schema_root=schema_root,
    )

    schema = loader.get_schema(
        "test"
    )

    relationships = (
        schema[
            "fields"
        ][
            "relationships"
        ]
    )

    assert (
        relationships["type"]
        == "object"
    )

    assert (
        relationships["required"]
        is False
    )
