import json
import os

from rvdb.indexes import indexes



class SearchIndexer:


    def build(
        self,
        games,
        output="dist/search_index.json"
    ):

        os.makedirs(
            os.path.dirname(output),
            exist_ok=True
        )


        #
        # Build runtime indexes
        #

        indexes.build(
            games
        )



        index = {

            "games": {},

            "titles": {},

            "platforms": {},

            "developers": {},

            "publishers": {},

            "genres": {},

            "regions": {},

        }



        for game in games:


            index["games"][game.id] = {

                "title": game.title,

                "platform": game.platform,

                "developer": game.developer,

                "publisher": game.publisher,

                "genres": game.genres,

                "regions": game.regions,

            }



            if game.title:

                index["titles"][
                    game.title.lower()
                ] = game.id



            if game.platform:

                index["platforms"].setdefault(
                    game.platform,
                    []
                ).append(
                    game.id
                )



            if game.developer:

                index["developers"].setdefault(
                    game.developer,
                    []
                ).append(
                    game.id
                )



            if game.publisher:

                index["publishers"].setdefault(
                    game.publisher,
                    []
                ).append(
                    game.id
                )



            for genre in game.genres:

                index["genres"].setdefault(
                    genre,
                    []
                ).append(
                    game.id
                )



            for region in game.regions:

                index["regions"].setdefault(
                    region,
                    []
                ).append(
                    game.id
                )



        with open(
            output,
            "w"
        ) as f:

            json.dump(
                index,
                f,
                indent=4
            )



        return output
