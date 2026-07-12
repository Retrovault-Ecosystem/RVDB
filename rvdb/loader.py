import os
import yaml

from rvdb.registry import registry

from rvdb.entities import (
    Game,
    Platform,
    Core,
    Developer,
    Publisher,
    Region,
)


ENTITY_MAP = {

    "games": Game,
    "platforms": Platform,
    "cores": Core,
    "developers": Developer,
    "publishers": Publisher,
    "regions": Region,

}


class RVDBLoader:


    def load_entity(
        self,
        category,
        entity
    ):

        registry.register(
            category,
            entity
        )


    def load_yaml_file(
        self,
        category,
        filepath
    ):

        with open(
            filepath,
            "r"
        ) as file:

            data = yaml.safe_load(file)


        entity_class = ENTITY_MAP.get(
            category
        )


        if not entity_class:

            raise ValueError(
                f"Unknown category {category}"
            )


        entity = entity_class(
            **data
        )


        self.load_entity(
            category,
            entity
        )


        return entity



    def load_directory(
        self,
        category,
        directory
    ):

        loaded = []


        for filename in os.listdir(directory):

            if filename.endswith(
                ".yaml"
            ) or filename.endswith(
                ".yml"
            ):

                entity = self.load_yaml_file(
                    category,
                    os.path.join(
                        directory,
                        filename
                    )
                )

                loaded.append(
                    entity
                )


        return loaded
