"""
RVDB Entity Creation Command

Creates new RVDB entities from templates.
"""

from pathlib import Path

from engine.factory import EntityFactory


ENTITY_OUTPUT_PATHS = {
    "platform": Path("data/platforms"),
    "game": Path("data/games"),
    "core": Path("data/cores"),
}


def cmd_create(
    entity_type,
    entity_id,
    name,
):

    try:

        if entity_type not in ENTITY_OUTPUT_PATHS:
            print(
                f"Unsupported entity type: {entity_type}"
            )
            return


        factory = EntityFactory()


        entity = factory.create_entity(
            entity_type,
            entity_id,
            name
        )


        output_dir = ENTITY_OUTPUT_PATHS[
            entity_type
        ]


        filename = (
            entity_id
            .replace(".", "_")
            + ".yaml"
        )


        output_file = output_dir / filename


        if output_file.exists():

            print(
                "ERROR:"
            )

            print(
                f"Entity already exists: {output_file}"
            )

            return


        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )


        import yaml


        with output_file.open(
            "w",
            encoding="utf-8"
        ) as file:

            yaml.safe_dump(
                entity,
                file,
                sort_keys=False
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
            f"Name: {name}"
        )

        print(
            f"Created: {output_file}"
        )


    except Exception as e:

        print(
            "Create error:",
            e
        )
