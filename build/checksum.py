"""
=========================================================
RVDB Foundation Checksum Builder
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    build/checksum.py

Purpose:
    Generates SHA-256 checksums for RVDB build artifacts.

    Checksum generation is independent of the legacy
    rvdb/ registry, loader, validator, and entity model.

Foundation Release:
    0.2.1

Checkpoint:
    D2 — Checksum Migration

=========================================================
"""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Iterable

from engine.paths import (
    PROJECT_ROOT,
)


# =========================================================
# Default Output
# =========================================================

DEFAULT_CHECKSUM_PATH = (
    PROJECT_ROOT
    / "dist"
    / "checksums.sha256"
)


# =========================================================
# File Checksum
# =========================================================

def sha256_file(
    path: str | Path,
) -> str:
    """
    Return the SHA-256 checksum for a file.
    """

    file_path = Path(
        path
    )

    digest = hashlib.sha256()

    with file_path.open(
        "rb"
    ) as file:

        for chunk in iter(
            lambda: file.read(
                1024 * 1024
            ),
            b"",
        ):

            digest.update(
                chunk
            )

    return digest.hexdigest()


# =========================================================
# Checksum Manifest
# =========================================================

def build_checksums(
    files: Iterable[str | Path],
    output: str | Path | None = None,
) -> Path:
    """
    Generate a SHA-256 checksum manifest.

    Missing input files are ignored, matching the behavior
    of the legacy checksum builder.

    Each generated line uses the conventional format:

        <sha256>  <filename>

    If output is omitted, the manifest is written to:

        <project-root>/dist/checksums.sha256
    """

    if output is None:

        output_path = (
            DEFAULT_CHECKSUM_PATH
        )

    else:

        output_path = Path(
            output
        )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    lines = []

    for item in files:

        file_path = Path(
            item
        )

        if not file_path.exists():

            continue

        if not file_path.is_file():

            continue

        checksum = sha256_file(
            file_path
        )

        lines.append(
            (
                f"{checksum}  "
                f"{file_path.name}"
            )
        )

    content = "\n".join(
        lines
    )

    if content:

        content += "\n"

    output_path.write_text(
        content,
        encoding="utf-8",
    )

    return output_path
