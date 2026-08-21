"""
=========================================================
RVDB EntityReferenceValidator Tests
=========================================================
"""

from engine.entity_reference import (
    EntityReferenceValidator,
)


def test_existing_entity_reference():

    validator = (
        EntityReferenceValidator()
    )

    assert validator.validate(
        "manufacturer.nintendo"
    )


def test_existing_typed_reference():

    validator = (
        EntityReferenceValidator()
    )

    assert validator.validate(
        "manufacturer.nintendo",
        "manufacturer",
    )


def test_wrong_entity_type():

    validator = (
        EntityReferenceValidator()
    )

    assert not validator.validate(
        "publisher.nintendo",
        "manufacturer",
    )


def test_missing_entity_reference():

    validator = (
        EntityReferenceValidator()
    )

    assert not validator.validate(
        "manufacturer.does_not_exist",
        "manufacturer",
    )


def test_reference_list():

    validator = (
        EntityReferenceValidator()
    )

    assert validator.validate_list(
        [
            "core.bsnes",
            "core.snes9x",
        ],
        "core",
    )


def test_reference_list_wrong_type():

    validator = (
        EntityReferenceValidator()
    )

    assert not validator.validate_list(
        [
            "core.bsnes",
            "manufacturer.nintendo",
        ],
        "core",
    )


def test_reference_list_must_be_list():

    validator = (
        EntityReferenceValidator()
    )

    assert not validator.validate_list(
        "core.bsnes",
        "core",
    )
