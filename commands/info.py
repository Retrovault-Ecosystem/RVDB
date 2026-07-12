from engine.context import get_engine


def cmd_info(term):

    try:

        engine = get_engine()

        entity = engine.resolve_entity(term)

        if not entity:
            print(f"No entity found: {term}")
            return


        print("\nENTITY INFORMATION")
        print("------------------")

        print(f"Name: {entity.get('name')}")
        print(f"Type: {entity.get('type')}")
        print(f"ID: {entity.get('id')}")


        aliases = entity.get("aliases", [])

        if aliases:

            print("\nAliases:")
            for alias in aliases:
                print(f"- {alias}")


        relationships = entity.get(
            "relationships",
            {}
        )


        if relationships:

            print("\nRelationships:")
            print("---------------")


            for rel_type, targets in relationships.items():

                print(
                    f"\n{rel_type.upper()}"
                )


                for target_id in targets:

                    target = engine.get_entity(
                        target_id
                    )

                    if target:

                        print(
                            f"- {target.get('name')}"
                        )


    except Exception as e:

        print(
            "Info error:",
            e
        )
