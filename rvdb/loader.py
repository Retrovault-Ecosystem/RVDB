import os
import yaml

from rvdb.registry import registry
from rvdb.resolver import resolve_id

from rvdb.entities import (
    Game,
    Platform,
    Core,
    Developer,
    Publisher,
    Genre,
    Region,
)


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


        entity = entity_class(
            **data
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
