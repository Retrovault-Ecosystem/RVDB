from engine.context import get_engine


# =========================================================
# DEVELOPER -> GAMES
# =========================================================

def cmd_developed_by(developer_id):

    try:

        engine = get_engine()

        developer = engine.resolve_entity(
            developer_id
        )

        if not developer:

            print(
                f"Developer not found: {developer_id}"
            )

            return


        games = engine.get_entities_by_relationship(
            developer["id"],
            "developed_by"
        )


        print("\nGAMES DEVELOPED BY")
        print("------------------")

        print(
            developer["name"]
        )


        if not games:

            print("- No games found")
            return


        for game in games:

            print(
                f"- {game['name']}"
            )


    except Exception as e:

        print(
            "Developed-by error:",
            e
        )



# =========================================================
# PUBLISHER -> GAMES
# =========================================================

def cmd_published_by(publisher_id):

    try:

        engine = get_engine()

        publisher = engine.resolve_entity(
            publisher_id
        )

        if not publisher:

            print(
                f"Publisher not found: {publisher_id}"
            )

            return


        games = engine.get_entities_by_relationship(
            publisher["id"],
            "published_by"
        )


        print("\nGAMES PUBLISHED BY")
        print("------------------")

        print(
            publisher["name"]
        )


        if not games:

            print("- No games found")
            return


        for game in games:

            print(
                f"- {game['name']}"
            )


    except Exception as e:

        print(
            "Published-by error:",
            e
        )



# =========================================================
# PLATFORM -> GAMES
# =========================================================

def cmd_games_on(platform_id):

    try:

        engine = get_engine()

        platform = engine.resolve_entity(
            platform_id
        )

        if not platform:

            print(
                f"Platform not found: {platform_id}"
            )

            return


        games = engine.get_entities_by_relationship(
            platform["id"],
            "platform"
        )


        print("\nGAMES FOUND")
        print("-----------")

        print(
            platform["name"]
        )


        if not games:

            print("- No games found")
            return


        for game in games:

            print(
                f"- {game['name']}"
            )


    except Exception as e:

        print(
            "Games-on error:",
            e
        )
