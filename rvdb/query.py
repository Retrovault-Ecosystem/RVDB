from rvdb.registry import registry
from rvdb.relationships import graph


class RVDBQuery:


    def games_by_platform(
        self,
        platform_id
    ):

        results = []

        for link in graph.find(
            relation="uses_platform"
        ):

            if link["target"] == platform_id:

                game = registry.get(
                    "games",
                    link["source"]
                )

                if game:
                    results.append(game)

        return results



    def games_by_developer(
        self,
        developer_id
    ):

        results = []

        for link in graph.find(
            relation="developed_by"
        ):

            if link["target"] == developer_id:

                game = registry.get(
                    "games",
                    link["source"]
                )

                if game:
                    results.append(game)

        return results



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
                    results.append(game)

        return results



    def related(
        self,
        entity_id
    ):

        return graph.find(
            source=entity_id
        )



query = RVDBQuery()
