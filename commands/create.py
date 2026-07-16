"""
RVDB Entity Creation Command

Supports both:

    rvdb create platform

and

    rvdb create platform platform.sega.genesis "Sega Genesis"
"""

from pathlib import Path
import yaml

from engine.factory import EntityFactory
from engine.entity_builder import EntityBuilder


ENTITY_OUTPUT_PATHS = {
    "platform": Path("data/platforms"),
    "game": Path("data/games"),
    "core": Path("data/cores"),
}


def cmd_create(
    entity_type,
    entity_id=None,
    name=None,
):

    try:

        if entity_type not in ENTITY_OUTPUT_PATHS:

            print(
                f"Unsupported entity type: {entity_type}"
            )

            return

        # =====================================================
        # INTERACTIVE MODE
        # =====================================================

        if entity_id is None or name is None:

            builder = EntityBuilder()

            entity = builder.build(
                entity_type
            )

            if entity is None:

                print(
                    "\nCreation cancelled."
                )

                return

            entity_id = entity["id"]

        # =====================================================
        # SCRIPT MODE
        # =====================================================

        else:

            factory = EntityFactory()

            entity = factory.create_entity(
                entity_type,
                entity_id,
                name
            )

        # =====================================================
        # WRITE FILE
        # =====================================================

        output_dir = ENTITY_OUTPUT_PATHS[
            entity_type
        ]

        filename = (
            entity_id.replace(".", "_")
            + ".yaml"
        )

        output_file = output_dir / filename

        if output_file.exists():

            print()

            print(
                "ERROR:"
            )

            print(
                f"Entity already exists:\n{output_file}"
            )

            return

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        with output_file.open(
            "w",
            encoding="utf-8"
        ) as file:

            yaml.safe_dump(
                entity,
                file,
                sort_keys=False,
                allow_unicode=True
            )

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

    except Exception as e:

        print()

        print(
            "Create error:"
        )

        print(e)
