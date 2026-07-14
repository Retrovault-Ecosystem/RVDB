from rvdb.registry import registry


class RelationshipFormatter:


    labels = {

        "uses_platform": "Platform",

        "uses_core": "Core",

        "developed_by": "Developer",

        "published_by": "Publisher",

        "has_genre": "Genres",

        "has_region": "Region",

    }



    def resolve_name(
        self,
        target
    ):

        parts = target.split(
            "."
        )


        if len(parts) != 2:

            return target


        entity_type = parts[0]

        entity_id = target



        collection_map = {

            "platform": "platforms",

            "core": "cores",

            "developer": "developers",

            "publisher": "publishers",

            "genre": "genres",

            "region": "regions",

        }



        collection = collection_map.get(
            entity_type
        )


        if not collection:

            return target



        entity = registry.get(
            collection,
            entity_id
        )


        if entity and hasattr(
            entity,
            "name"
        ):

            return entity.name



        return target



    def format_game(
        self,
        game_id,
        relationships
    ):

        output = []


        game = registry.get(
            "games",
            game_id
        )


        if game:

            output.append(
                game.title
            )

            output.append(
                "=" * len(game.title)
            )

            output.append(
                ""
            )



        grouped = {}



        for link in relationships:


            label = self.labels.get(
                link["relation"],
                link["relation"]
            )


            grouped.setdefault(
                label,
                []
            ).append(
                self.resolve_name(
                    link["target"]
                )
            )



        for label, values in grouped.items():


            output.append(
                f"{label}:"
            )


            for value in values:

                output.append(
                    f"    {value}"
                )


            output.append(
                ""
            )


        return "\n".join(
            output
        )



formatter = RelationshipFormatter()
