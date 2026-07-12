from engine.context import get_engine


def cmd_show(entity_id):

    try:

        engine = get_engine()

        entity = engine.resolve_entity(
            entity_id
        )


        if not entity:

            print(
                f"Entity not found: {entity_id}"
            )

            return


        print("\nENTITY")
        print("------")


        for key, value in entity.items():

            print(
                f"{key}: {value}"
            )


    except Exception as e:

        print(
            "Show error:",
            e
        )
