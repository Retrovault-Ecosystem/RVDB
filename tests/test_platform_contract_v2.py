from engine.schema_loader import SchemaLoader


def _platform_schema():
    loader = SchemaLoader()

    return loader.get_schema(
        "platform"
    )


def test_platform_category_is_required():

    schema = _platform_schema()

    assert "category" in schema[
        "required"
    ]


def test_platform_category_is_controlled_string_list():

    schema = _platform_schema()

    category = schema[
        "fields"
    ][
        "category"
    ]

    assert category["type"] == "list"

    assert category["items"] == {
        "type": "string",
        "enum": [
            "console",
            "handheld",
            "computer",
            "arcade",
        ],
    }


def test_platform_family_is_optional_string():

    schema = _platform_schema()

    assert "family" in schema[
        "optional"
    ]

    assert (
        schema["fields"]["family"]["type"]
        == "string"
    )


def test_platform_regions_is_typed_string_list():

    schema = _platform_schema()

    regions = schema[
        "fields"
    ][
        "regions"
    ]

    assert regions["type"] == "list"

    assert regions["items"] == {
        "type": "string",
    }


def test_platform_media_is_typed_string_list():

    schema = _platform_schema()

    media = schema[
        "fields"
    ][
        "media"
    ]

    assert media["type"] == "list"

    assert media["items"] == {
        "type": "string",
    }


def test_platform_extensions_is_typed_string_list():

    schema = _platform_schema()

    extensions = schema[
        "fields"
    ][
        "extensions"
    ]

    assert extensions["type"] == "list"

    assert extensions["items"] == {
        "type": "string",
    }


def test_platform_architecture_is_typed_string_list():

    schema = _platform_schema()

    architecture = schema[
        "fields"
    ][
        "architecture"
    ]

    assert architecture["type"] == "list"

    assert architecture["items"] == {
        "type": "string",
    }


def test_platform_manufacturer_contract_is_preserved():

    schema = _platform_schema()

    manufacturer = schema[
        "fields"
    ][
        "manufacturer"
    ]

    assert (
        manufacturer["type"]
        == "entity_reference_list"
    )

    assert (
        manufacturer["entity_type"]
        == "manufacturer"
    )


def test_platform_release_fields_are_preserved():

    schema = _platform_schema()

    assert (
        schema["fields"]["release_year"]["type"]
        == "integer_or_null"
    )

    assert (
        schema["fields"]["generation"]["type"]
        == "integer_or_null"
    )


def test_platform_supports_core_relationship_is_preserved():

    schema = _platform_schema()

    supports_core = schema[
        "relationships"
    ][
        "supports_core"
    ]

    assert (
        supports_core["type"]
        == "entity_reference_list"
    )

    assert (
        supports_core["entity_type"]
        == "core"
    )
