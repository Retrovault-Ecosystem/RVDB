"""
RVDB ID Generator

Generates canonical RVDB namespace IDs.

RVDB ID format:

entity_type.segment.segment.segment

Examples:

game + Super Mario World
    -> game.super.mario.world

platform + Nintendo Super Nintendo
    -> platform.nintendo.super.nintendo

developer + Nintendo EAD
    -> developer.nintendo.ead

core + Snes9x
    -> core.snes9x
"""

from __future__ import annotations

import re


class IDGenerator:
    """
    Generates canonical RVDB entity IDs.
    """


    @staticmethod
    def slugify(text: str) -> str:
        """
        Convert text into namespace segments.
        """

        text = text.lower().strip()


        # Replace separators with spaces
        text = re.sub(
            r"[-_/]+",
            " ",
            text
        )


        # Remove invalid characters
        text = re.sub(
            r"[^a-z0-9 ]",
            "",
            text
        )


        # Collapse whitespace
        text = re.sub(
            r"\s+",
            " ",
            text
        ).strip()


        # Convert words into namespace segments
        return ".".join(
            text.split()
        )


    @classmethod
    def generate(
        cls,
        entity_type: str,
        name: str
    ) -> str:
        """
        Generate canonical RVDB ID.
        """

        entity_type = cls.slugify(
            entity_type
        )

        name = cls.slugify(
            name
        )


        return (
            f"{entity_type}."
            f"{name}"
        )
