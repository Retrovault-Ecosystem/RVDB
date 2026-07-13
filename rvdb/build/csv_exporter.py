import csv
import os


class CSVExporter:

    def export_games(
        self,
        games,
        output="dist/games.csv"
    ):

        os.makedirs(
            os.path.dirname(output),
            exist_ok=True
        )

        with open(
            output,
            "w",
            newline=""
        ) as f:

            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "id",
                    "title",
                    "platform",
                    "core",
                    "year",
                    "developer",
                    "publisher",
                ]
            )

            writer.writeheader()

            for game in games:

                writer.writerow({

                    "id": game.id,
                    "title": game.title,
                    "platform": game.platform,
                    "core": game.core,
                    "year": game.year,
                    "developer": game.developer,
                    "publisher": game.publisher,

                })

        return output
