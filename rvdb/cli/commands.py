from rvdb.build.builder import RVDBBuilder
from rvdb.registry import registry
from rvdb.query import query
from rvdb.relationships import graph
from rvdb.formatter import formatter


def build_command():

    builder = RVDBBuilder()

    return builder.build()



def initialize_database():

    builder = RVDBBuilder()


    #
    # Reset happens BEFORE loading
    #

    graph.clear()


    #
    # Run official build pipeline
    #

    builder.validate()

    builder.load()

    builder.link()

    builder.index()



def search_command(
    term
):

    initialize_database()


    game = query.search_title(
        term
    )


    if not game:

        print(
            "No game found."
        )

        return


    print()

    print(
        "Found:"
    )

    print()

    print(
        f"ID: {game.id}"
    )

    print(
        f"Title: {game.title}"
    )

    print(
        f"Platform: {game.platform}"
    )

    print(
        f"Developer: {game.developer}"
    )

    print(
        f"Publisher: {game.publisher}"
    )



def info_command(
    game_id
):

    initialize_database()


    games = query._resolve_games(
        [
            game_id
        ]
    )


    if not games:

        print(
            "Game not found."
        )

        return


    game = games[0]


    print()

    print(
        f"ID: {game.id}"
    )

    print(
        f"Title: {game.title}"
    )

    print(
        f"Year: {game.year}"
    )

    print(
        f"ROM: {game.rom_path}"
    )



def relationships_command(
    entity_id
):

    initialize_database()


    links = graph.find(
        source=entity_id
    )


    if not links:

        print(
            "No relationships found."
        )

        return


    print(
    formatter.format_game(
        entity_id,
        links
    )
)
