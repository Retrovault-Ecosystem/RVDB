from engine.type_registry import TypeRegistry


def test_string_enum_accepts_allowed_value():
    registry = TypeRegistry()

    assert registry.validate(
        "string",
        "console",
        enum=[
            "console",
            "handheld",
            "computer",
            "arcade",
        ],
    )


def test_string_enum_rejects_unknown_value():
    registry = TypeRegistry()

    assert not registry.validate(
        "string",
        "toaster",
        enum=[
            "console",
            "handheld",
            "computer",
            "arcade",
        ],
    )


def test_string_without_enum_remains_backward_compatible():
    registry = TypeRegistry()

    assert registry.validate(
        "string",
        "arbitrary-value",
    )


def test_list_items_type_accepts_matching_items():
    registry = TypeRegistry()

    assert registry.validate(
        "list",
        [
            "north-america",
            "japan",
        ],
        items={
            "type": "string",
        },
    )


def test_list_items_type_rejects_wrong_item_type():
    registry = TypeRegistry()

    assert not registry.validate(
        "list",
        [
            "north-america",
            123,
        ],
        items={
            "type": "string",
        },
    )


def test_list_items_enum_accepts_allowed_values():
    registry = TypeRegistry()

    assert registry.validate(
        "list",
        [
            "cartridge",
            "optical-disc",
        ],
        items={
            "type": "string",
            "enum": [
                "cartridge",
                "floppy",
                "optical-disc",
                "digital",
                "cassette",
            ],
        },
    )


def test_list_items_enum_rejects_unknown_value():
    registry = TypeRegistry()

    assert not registry.validate(
        "list",
        [
            "cartridge",
            "magic-crystal",
        ],
        items={
            "type": "string",
            "enum": [
                "cartridge",
                "floppy",
                "optical-disc",
                "digital",
                "cassette",
            ],
        },
    )


def test_list_without_items_remains_backward_compatible():
    registry = TypeRegistry()

    assert registry.validate(
        "list",
        [
            "anything",
            123,
            True,
            None,
        ],
    )


def test_empty_constrained_list_is_valid():
    registry = TypeRegistry()

    assert registry.validate(
        "list",
        [],
        items={
            "type": "string",
            "enum": [
                "console",
                "handheld",
            ],
        },
    )
