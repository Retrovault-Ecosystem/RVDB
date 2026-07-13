from rvdb.registry import registry
from rvdb.relationships import graph
from rvdb.indexes import indexes


class RVDBQuery:


    def search_title(
        self,
        title
    ):

        game_id = indexes.title.get(
            title.lower()
        )


        if not game_id:

            return None


        return registry.get(
            "games",
            game_id
        )



    def games_by_platform(
        self,
        platform_id
    ):

        game_ids = indexes.platform.get(
            platform_id,
            []
        )


        return self._resolve_games(
            game_ids
        )



    def games_by_developer(
        self,
        developer_id
    ):

        game_ids = indexes.developer.get(
            developer_id,
            []
        )


        return self._resolve_games(
            game_ids
        )



    def games_by_publisher(
        self,
        publisher_id
    ):

        game_ids = indexes.publisher.get(
            publisher_id,
            []
        )


        return self._resolve_games(
            game_ids
        )



    def games_by_genre(
        self,
        genre_id
    ):

        game_ids = indexes.genre.get(
            genre_id,
            []
        )


        return self._resolve_games(
            game_ids
        )



    def games_by_region(
        self,
        region_id
    ):

        game_ids = indexes.region.get(
            region_id,
            []
        )


        return self._resolve_games(
            game_ids
        )



    def games_by_core(
        self,
        core_id
    ):

        results = []


        for link in graph.find(
            relation="uses_core"
        ):

            if link["target"] == core_id:

                game = registry.get(
                    "games",
                    link["source"]
                )


                if game:

                    results.append(
                        game
                    )


        return results



    def related(
        self,
        entity_id
    ):

        return graph.find(
            source=entity_id
        )



    def _resolve_games(
        self,
        game_ids
    ):

        results = []


        for game_id in game_ids:

            game = registry.get(
                "games",
                game_id
            )


            if game:

                results.append(
                    game
                )


        return results



query = RVDBQuery()
