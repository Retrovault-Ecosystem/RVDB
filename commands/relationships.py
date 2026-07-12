from engine.context import get_engine, get_resolver

# =========================================================
# PLATFORM -> CORES
# =========================================================

def cmd_cores(platform_id):

    try:

        engine = get_engine()
        resolver = get_resolver()

        platform = resolver.resolve(platform_id)

        if not platform:

            print(f"Platform not found: {platform_id}")
            return


        cores = engine.get_supported_cores(
            platform["id"]
        )


        if not cores:

            print(
                f"No cores found for: {platform_id}"
            )

            return


        print("\nSUPPORTED CORES")
        print("----------------")


        for core in cores:

            print(f"- {core}")


    except Exception as e:

        print(
            "Cores error:",
            e
        )



# =========================================================
# CORE -> PLATFORMS
# =========================================================

def cmd_who_uses(core_id):

    try:

        engine = get_engine()
        resolver = get_resolver()

        core = resolver.resolve(core_id)


        if not core:

            print(
                f"Core not found: {core_id}"
            )

            return


        platforms = engine.get_platforms_by_core(
            core["id"]
        )


        if not platforms:

            print(
                f"No platforms found using {core_id}"
            )

            return


        print("\nPLATFORMS USING CORE")
        print("--------------------")


        for platform in platforms:

            print(f"- {platform}")


    except Exception as e:

        print(
            "Who-uses error:",
            e
        )



# =========================================================
# ENTITY -> RELATED ENTITIES
# =========================================================

def cmd_related(entity_id):

    try:

        engine = get_engine()
        resolver = get_resolver()

        entity = resolver.resolve(entity_id)


        if not entity:

            print(
                f"Entity not found: {entity_id}"
            )

            return


        related = engine.get_related_entities(
            entity["id"]
        )


        print("\nRELATED ENTITIES")
        print("----------------")


        if not related:

            print(
                "No relationships found."
            )

            return


        for relationship_type, entities in related.items():

            print()

            print(
                relationship_type.upper()
            )

            print(
                "-" * len(relationship_type)
            )


            for item in entities:

                print(
                    f"- {item['name']}"
                )


    except Exception as e:

        print(
            "Related error:",
            e
        )
