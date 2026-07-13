import json
import os


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

        index = {}

        for game in games:

            index[game.id] = {

                "title": game.title,
                "platform": game.platform,
                "developer": game.developer,
                "publisher": game.publisher,
                "genres": game.genres,

            }

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
