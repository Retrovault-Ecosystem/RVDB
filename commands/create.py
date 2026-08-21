"""
=========================================================
RVDB Entity Creation Command
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    commands/create.py

Purpose:
    Creates RVDB entities in either interactive or
    script-driven mode.

    Supported entity types are discovered dynamically.

    An entity type is creatable when both exist:

        schemas/entities/<type>.yaml
        templates/entities/<type>.yaml

Foundation Release:
    0.2

Checkpoint:
    C2 — Generic Entity Builder

=========================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from engine.entity_builder import EntityBuilder
from engine.factory import EntityFactory
from engine.paths import DATA_ROOT
from engine.schema_loader import SchemaLoader
from validator.schema import SchemaValidator


# =====================================================
# Supported Entity Types
# =====================================================

def get_supported_entity_types(
    schema_loader: SchemaLoader | None = None,
    factory: EntityFactory | None = None,
) -> list[str]:
    """
    Return entity types that have both:

        - a YAML schema
        - a YAML entity template

    No entity-type list is hardcoded here.
    """

    if schema_loader is None:

        schema_loader = SchemaLoader()

    if factory is None:

        factory = EntityFactory()

    supported = []

    for entity_type in (
        schema_loader.list_entity_types()
    ):

        template_file = (
            factory.template_directory
            / f"{entity_type}.yaml"
        )

        if template_file.exists():

            supported.append(
                entity_type
            )

    return sorted(
        supported
    )


# =====================================================
# Output Directory
# =====================================================

def _output_directory(
    entity_type: str,
) -> Path:
    """
    Return the canonical data directory for an entity type.

    Foundation 0.2 currently follows the repository
    convention:

        platform      -> data/platforms
        game          -> data/games
        developer     -> data/developers

    A schema-defined storage path can replace this
    convention in a later release if needed.
    """

    return (
        DATA_ROOT
        / f"{entity_type}s"
    )


# =====================================================
# Filename
# =====================================================

def _entity_filename(
    entity_id: str,
) -> str:
    """
    Convert a canonical RVDB ID into a YAML filename.
    """

    return (
        entity_id
        .replace(
            ".",
            "_",
        )
        + ".yaml"
    )


# =====================================================
# Entity Validation
# =====================================================

def _validate_before_write(
    entity: dict[str, Any],
) -> bool:
    """
    Prevent invalid entities from being written to RVDB.
    """

    validator = SchemaValidator()

    result = validator.validate(
        entity
    )

    if result.valid:

        return True

    print()

    print(
        "Entity validation failed"
    )

    print(
        "------------------------"
    )

    for error in result.errors:

        print(
            f"- {error}"
        )

    return False


# =====================================================
# Create Command
# =====================================================

def cmd_create(
    entity_type,
    entity_id=None,
    name=None,
):
    """
    Create an RVDB entity.

    Interactive:

        python3 cli.py create platform

    Script mode:

        python3 cli.py create \
            developer \
            developer.example \
            "Example Developer"
    """

    try:

        entity_type = (
            str(
                entity_type
            )
            .strip()
            .casefold()
        )

        schema_loader = (
            SchemaLoader()
        )

        factory = (
            EntityFactory()
        )

        supported_types = (
            get_supported_entity_types(
                schema_loader,
                factory,
            )
        )

        if (
            entity_type
            not in supported_types
        ):

            print(
                f"Unsupported entity type: "
                f"{entity_type}"
            )

            print()

            print(
                "Supported entity types:"
            )

            for supported in supported_types:

                print(
                    f"  {supported}"
                )

            return None

        # =================================================
        # Interactive Mode
        # =================================================

        if (
            entity_id is None
            or name is None
        ):

            builder = EntityBuilder()

            entity = builder.build(
                entity_type
            )

            if entity is None:

                print()

                print(
                    "Creation cancelled."
                )

                return None

            entity_id = entity[
                "id"
            ]

        # =================================================
        # Script Mode
        # =================================================

        else:

            entity = (
                factory.create_entity(
                    entity_type,
                    entity_id,
                    name,
                )
            )

        # =================================================
        # Validation
        # =================================================

        if not _validate_before_write(
            entity
        ):

            return None

        # =================================================
        # Output
        # =================================================

        output_dir = (
            _output_directory(
                entity_type
            )
        )

        filename = (
            _entity_filename(
                entity_id
            )
        )

        output_file = (
            output_dir
            / filename
        )

        # =================================================
        # Duplicate Protection
        # =================================================

        if output_file.exists():

            print()

            print(
                "ERROR:"
            )

            print(
                "Entity already exists:"
            )

            print(
                output_file
            )

            return None

        # =================================================
        # Write Entity
        # =================================================

        output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        with output_file.open(
            "w",
            encoding="utf-8",
        ) as file:

            yaml.safe_dump(
                entity,
                file,
                sort_keys=False,
                allow_unicode=True,
                default_flow_style=False,
            )

        # =================================================
        # Success
        # =================================================

        print()

        print(
            "Entity created successfully"
        )

        print(
            "--------------------------"
        )

        print(
            f"Type: {entity_type}"
        )

        print(
            f"ID: {entity_id}"
        )

        print(
            f"Name: {entity['name']}"
        )

        print(
            f"Created: {output_file}"
        )

        return entity

    except Exception as error:

        print()

        print(
            "Create error:"
        )

        print(
            error
        )

        return None
