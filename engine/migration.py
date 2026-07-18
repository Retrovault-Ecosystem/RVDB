"""
RVDB ID Migration Engine

Handles conversion from legacy RVDB IDs
to canonical namespace IDs.
"""

from pathlib import Path
import yaml

from engine.id_generator import IDGenerator


class IDMigration:


    def __init__(
        self,
        data_path="data"
    ):

        self.data_path = Path(
            data_path
        )

        self.config_path = Path(
            "config"
        )

        self.override_file = (
            self.config_path /
            "id_overrides.yaml"
        )

        self.id_map = {}

        self.overrides = (
            self.load_overrides()
        )


    def load_overrides(self):

        """
        Load canonical ID overrides.
        """

        if not self.override_file.exists():

            return {}


        with open(
            self.override_file,
            "r",
            encoding="utf-8"
        ) as f:

            return yaml.safe_load(f) or {}


    def get_canonical_id(
        self,
        old_id,
        entity_type,
        name
    ):

        """
        Return override ID if defined,
        otherwise generate one.
        """

        if old_id in self.overrides:

            return self.overrides[
                old_id
            ]


        return IDGenerator.generate(
            entity_type,
            name
        )


    def scan_entities(self):

        """
        Scan YAML entities and build
        old -> new ID mapping.
        """

        self.id_map = {}


        for file in self.data_path.rglob(
            "*.yaml"
        ):

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                entity = yaml.safe_load(f)


            if not entity:

                continue


            old_id = entity.get("id")

            entity_type = entity.get("type")

            name = entity.get("name")


            if not all(
                [
                    old_id,
                    entity_type,
                    name
                ]
            ):

                continue


            new_id = self.get_canonical_id(
                old_id,
                entity_type,
                name
            )


            self.id_map[
                old_id
            ] = new_id


        return self.id_map


    def preview(self):

        """
        Display migration changes without modifying files.
        """

        results = self.scan_entities()

        changes = {}


        for old_id, new_id in results.items():

            if old_id != new_id:

                changes[
                    old_id
                ] = new_id


        return changes


    def print_preview(self):

        """
        Human-readable migration preview.
        """

        changes = self.preview()


        if not changes:

            print(
                "No migrations required."
            )

            return


        print()

        print(
            "RVDB MIGRATION PREVIEW"
        )

        print(
            "----------------------"
        )


        for old_id, new_id in changes.items():

            print(
                f"{old_id} -> {new_id}"
            )


        print()

        print(
            f"Changes detected: {len(changes)}"
        )
