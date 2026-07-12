from rvdb.registry import registry
from rvdb.relationships import graph
from rvdb.resolver import resolve_id



class RelationshipLinker:


    def link_game(
        self,
        game
    ):

        if game.platform:

            graph.add(
                game.id,
                "uses_platform",
                resolve_id(
                    "platform",
                    game.platform
                )
            )


        if game.core:

            graph.add(
                game.id,
                "uses_core",
                resolve_id(
                    "core",
                    game.core
                )
            )


        if game.developer:

            graph.add(
                game.id,
                "developed_by",
                resolve_id(
                    "developer",
                    game.developer
                )
            )


        if game.publisher:

            graph.add(
                game.id,
                "published_by",
                resolve_id(
                    "publisher",
                    game.publisher
                )
            )


        for genre in game.genres:

            graph.add(
                game.id,
                "has_genre",
                resolve_id(
                    "genre",
                    genre
                )
            )


        for region in game.regions:

            graph.add(
                game.id,
                "has_region",
                resolve_id(
                    "region",
                    region
                )
            )



    def link_all_games(
        self
    ):

        for game in registry.all(
            "games"
        ):

            self.link_game(
                game
            )



linker = RelationshipLinker()
