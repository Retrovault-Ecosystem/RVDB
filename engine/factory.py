"""
RVDB Entity Factory

Creates new RVDB entities from templates.

The factory:
- loads entity templates
- creates entity dictionaries
- validates required structure
- prepares YAML-ready output
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import copy
import yaml


class EntityFactory:

    def __init__(
        self,
        template_directory="templates/entities"
    ):

        self.template_directory = Path(
            template_directory
        )


    def load_template(
        self,
        entity_type: str
    ) -> dict[str, Any]:

        template_file = (
            self.template_directory /
            f"{entity_type}.yaml"
        )

        if not template_file.exists():

            raise FileNotFoundError(
                f"Template not found: {template_file}"
            )


        with template_file.open(
            "r",
            encoding="utf-8"
        ) as file:

            return yaml.safe_load(file)



    def create_entity(
        self,
        entity_type: str,
        entity_id: str,
        name: str,
    ) -> dict[str, Any]:

        template = self.load_template(
            entity_type
        )


        entity = copy.deepcopy(
            template
        )


        entity["id"] = entity_id

        entity["type"] = entity_type

        entity["name"] = name


        return entity



    def save_entity(
        self,
        entity: dict[str, Any],
        output_path: str | Path,
    ):

        output_path = Path(
            output_path
        )


        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        with output_path.open(
            "w",
            encoding="utf-8"
        ) as file:

            yaml.safe_dump(
                entity,
                file,
                sort_keys=False
            )
