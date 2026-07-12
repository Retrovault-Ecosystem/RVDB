import os
import yaml
import inspect

from rvdb.registry import registry
from rvdb.entities import (
    Game,
    Platform,
    Core,
    Developer,
    Publisher,
    Genre,
    Region,
)

from rvdb.linker import linker


ENTITY_MAP = {

    "games": Game,
    "platforms": Platform,
    "cores": Core,
    "developers": Developer,
    "publishers": Publisher,
    "genres": Genre,
    "regions": Region,

}


class RVDBLoader:


    def load_file(
        self,
        category,
        filepath
    ):

        with open(
            filepath,
            "r"
        ) as file:

            data = yaml.safe_load(
                file
            )


        entity_class = ENTITY_MAP.get(
            category
        )


        if entity_class is None:

            raise ValueError(
                f"Unknown category: {category}"
            )


        fields = inspect.signature(
            entity_class
        ).parameters


        filtered_data = {

            key: value

            for key, value in data.items()

            if key in fields

        }


        entity = entity_class(
            **filtered_data
        )


        registry.register(
            category,
            entity
        )


        return entity



    def load_directory(
        self,
        category,
        directory
    ):

        results = []


        for filename in sorted(
            os.listdir(directory)
        ):

            if filename.endswith(
                ".yaml"
            ):

                entity = self.load_file(
                    category,
                    os.path.join(
                        directory,
                        filename
                    )
                )

                results.append(
                    entity
                )


        return results



    def load_all(
        self,
        data_directory="data"
    ):

        categories = [

            "platforms",
            "cores",
            "developers",
            "publishers",
            "genres",
            "regions",
            "games",

        ]


        for category in categories:

            directory = os.path.join(
                data_directory,
                category
            )


            if os.path.exists(
                directory
            ):

                self.load_directory(
                    category,
                    directory
                )


        linker.link_all_games()
