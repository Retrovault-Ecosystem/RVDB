"""
RVDB Entity Loader

Loads RVDB YAML entity files into structured Python objects.

The loader is responsible for:
- discovering YAML files
- parsing YAML content
- creating entity objects
- basic integrity checking

Schema validation is handled separately.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(slots=True)
class Entity:
    """
    Represents a single RVDB entity.
    """

    source: Path
    data: dict[str, Any]

    @property
    def id(self) -> str:
        return self.data["id"]

    @property
    def entity_type(self) -> str:
        return self.data["type"]

    @property
    def name(self) -> str:
        return self.data["name"]


class EntityLoader:
    """
    Loads RVDB YAML entities from disk.
    """

    REQUIRED_FIELDS = {
        "id",
        "type",
        "name",
    }

    def __init__(self, directory: str | Path):
        self.directory = Path(directory)

    def discover_files(self) -> list[Path]:
        """
        Find YAML files recursively.
        """

        yaml_files = list(self.directory.rglob("*.yaml"))
        yaml_files.extend(self.directory.rglob("*.yml"))

        return sorted(yaml_files)

    def load(self) -> list[Entity]:
        """
        Load all discovered entities.
        """

        entities = []

        for file_path in self.discover_files():
            entities.append(
                self.load_file(file_path)
            )

        return entities

    def load_file(self, file_path: Path) -> Entity:
        """
        Load a single YAML entity.
        """

        with file_path.open(
            "r",
            encoding="utf-8"
        ) as file:

            data = yaml.safe_load(file)

        if not isinstance(data, dict):
            raise ValueError(
                f"{file_path} must contain YAML mapping data"
            )

        self.validate_basic_fields(
            data,
            file_path
        )

        return Entity(
            source=file_path,
            data=data,
        )

    def validate_basic_fields(
        self,
        data: dict[str, Any],
        file_path: Path,
    ) -> None:
        """
        Check minimum entity requirements.
        """

        missing = (
            self.REQUIRED_FIELDS -
            data.keys()
        )

        if missing:
            raise ValueError(
                f"{file_path} missing fields: {missing}"
            )
