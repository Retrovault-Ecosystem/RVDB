from engine.context import get_resolver


def cmd_query(entity_text):

    try:

        resolver = get_resolver()

        entity = resolver.resolve(
            entity_text
        )

        if not entity:
            print(
                f"No entity found: {entity_text}"
            )
            return


        print("\nRESULT")
        print("------")


        for key, value in entity.items():

            print(
                f"{key}: {value}"
            )


    except Exception as e:

        print(
            "Query error:",
            e
        )
