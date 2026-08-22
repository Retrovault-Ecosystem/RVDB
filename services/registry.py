"""
=========================================================
RVDB Entity Registry
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    services/registry.py

Purpose:
    Provides a centralized in-memory registry of RVDB
    entities.

    Project data paths are resolved independently of the
    shell's current working directory.

Foundation Release:
    0.2

Checkpoint:
    C4 — Final Integration and Release Readiness

=========================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from engine.paths import DATA_ROOT


class EntityRegistry:
    """
    Centralized in-memory entity registry.
    """

    def __init__(
        self,
        data_path: str | Path | None = None,
    ) -> None:

        self.by_id: dict[
            str,
            dict[str, Any],
        ] = {}

        self.by_name: dict[
            str,
            str,
        ] = {}

        self.by_alias: dict[
            str,
            str,
        ] = {}

        self.by_type: dict[
            str,
            list[str],
        ] = {}

        if data_path is None:

            self.data_path = DATA_ROOT

        else:

            self.data_path = Path(
                data_path
            )

        self.load()

    # =====================================================
    # Load Database
    # =====================================================

    def load(
        self,
    ) -> None:

        self.by_id.clear()

        self.by_name.clear()

        self.by_alias.clear()

        self.by_type.clear()

        if not self.data_path.exists():

            return

        yaml_files = list(
            self.data_path.rglob(
                "*.yaml"
            )
        )

        yaml_files.extend(
            self.data_path.rglob(
                "*.yml"
            )
        )

        for yaml_file in sorted(
            yaml_files
        ):

            entity = self.load_entity(
                yaml_file
            )

            if entity:

                self.register(
                    entity
                )

    # =====================================================
    # Load One Entity
    # =====================================================

    def load_entity(
        self,
        filename: Path,
    ) -> dict[str, Any] | None:

        try:

            with filename.open(
                "r",
                encoding="utf-8",
            ) as file:

                entity = yaml.safe_load(
                    file
                )

        except Exception:

            return None

        if not isinstance(
            entity,
            dict,
        ):

            return None

        return entity

    # =====================================================
    # Register
    # =====================================================

    def register(
        self,
        entity: dict[str, Any],
    ) -> None:

        entity_id = entity.get(
            "id"
        )

        entity_type = entity.get(
            "type"
        )

        name = entity.get(
            "name"
        )

        aliases = entity.get(
            "aliases",
            [],
        )

        if not all(
            [
                entity_id,
                entity_type,
                name,
            ]
        ):

            return

        self.by_id[
            entity_id
        ] = entity

        self.by_name[
            name.casefold()
        ] = entity_id

        if isinstance(
            aliases,
            list,
        ):

            for alias in aliases:

                if not isinstance(
                    alias,
                    str,
                ):

                    continue

                self.by_alias[
                    alias.casefold()
                ] = entity_id

        self.by_type.setdefault(
            entity_type,
            [],
        ).append(
            entity_id
        )

    # =====================================================
    # Public API
    # =====================================================

    def exists(
        self,
        entity_id,
    ) -> bool:

        return (
            entity_id
            in self.by_id
        )

    def get(
        self,
        entity_id,
    ):

        return self.by_id.get(
            entity_id
        )

    def resolve(
        self,
        name,
    ):

        if not name:

            return None

        key = str(
            name
        ).casefold()

        if key in self.by_name:

            return self.by_name[
                key
            ]

        if key in self.by_alias:

            return self.by_alias[
                key
            ]

        return None

    def entities_of_type(
        self,
        entity_type,
    ) -> list[str]:

        return list(
            self.by_type.get(
                entity_type,
                [],
            )
        )
