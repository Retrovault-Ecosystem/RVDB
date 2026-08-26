"""
=========================================================
RVDB Foundation Manifest Tests
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/test_manifest_v2.py

Foundation Release:
    0.2.1

Checkpoint:
    D5 — Manifest Migration

=========================================================
"""

import json
from datetime import datetime

from build.manifest import (
    DEFAULT_MANIFEST_PATH,
    DEFAULT_MANIFEST_VERSION,
    build_manifest,
)

from engine.graph import (
    build_graph,
)

from engine.loader import (
    load_entities,
)

from engine.paths import (
    PROJECT_ROOT,
)


def read_manifest(
    path,
):

    return json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )


def test_manifest_contains_foundation_identity(
    tmp_path,
):

    graph = build_graph(
        load_entities()
    )

    output = (
        tmp_path
        / "manifest.json"
    )

    build_manifest(
        graph,
        output=output,
    )

    manifest = read_manifest(
        output
    )

    assert (
        manifest[
            "name"
        ]
        == "RetroVault Database"
    )

    assert (
        manifest[
            "version"
        ]
        == DEFAULT_MANIFEST_VERSION
    )


def test_manifest_contains_entity_statistics(
    tmp_path,
):

    graph = build_graph(
        load_entities()
    )

    output = (
        tmp_path
        / "manifest.json"
    )

    build_manifest(
        graph,
        output=output,
    )

    statistics = read_manifest(
        output
    )[
        "statistics"
    ]

    assert (
        statistics[
            "total_entities"
        ]
        == 31
    )

    assert statistics[
        "by_type"
    ] == {
        "core": 2,
        "developer": 2,
        "game": 4,
        "genre": 3,
        "manufacturer": 3,
        "platform": 16,
        "publisher": 1,
    }


def test_manifest_normalizes_project_artifacts(
    tmp_path,
):

    graph = build_graph(
        load_entities()
    )

    output = (
        tmp_path
        / "manifest.json"
    )

    build_manifest(
        graph,
        artifacts=[
            (
                PROJECT_ROOT
                / "rvdb.bundle.json"
            ),
            (
                PROJECT_ROOT
                / "dist"
                / "entities.csv"
            ),
            (
                PROJECT_ROOT
                / "dist"
                / "checksums.sha256"
            ),
        ],
        output=output,
    )

    manifest = read_manifest(
        output
    )

    assert manifest[
        "artifacts"
    ] == [
        "dist/checksums.sha256",
        "dist/entities.csv",
        "rvdb.bundle.json",
    ]


def test_manifest_does_not_embed_external_absolute_paths(
    tmp_path,
):

    graph = build_graph(
        load_entities()
    )

    external = (
        tmp_path
        / "outside.json"
    )

    external.write_text(
        "{}",
        encoding="utf-8",
    )

    output = (
        tmp_path
        / "manifest.json"
    )

    build_manifest(
        graph,
        artifacts=[
            external
        ],
        output=output,
    )

    manifest = read_manifest(
        output
    )

    assert manifest[
        "artifacts"
    ] == [
        "outside.json"
    ]

    assert str(
        tmp_path
    ) not in output.read_text(
        encoding="utf-8"
    )


def test_manifest_timestamp_is_utc(
    tmp_path,
):

    graph = build_graph(
        load_entities()
    )

    output = (
        tmp_path
        / "manifest.json"
    )

    build_manifest(
        graph,
        output=output,
    )

    generated = read_manifest(
        output
    )[
        "generated"
    ]

    assert generated.endswith(
        "Z"
    )

    parsed = datetime.fromisoformat(
        generated.replace(
            "Z",
            "+00:00",
        )
    )

    assert (
        parsed.utcoffset()
        .total_seconds()
        == 0
    )


def test_manifest_version_can_be_overridden(
    tmp_path,
):

    graph = build_graph(
        load_entities()
    )

    output = (
        tmp_path
        / "manifest.json"
    )

    build_manifest(
        graph,
        output=output,
        version="9.9.9",
    )

    manifest = read_manifest(
        output
    )

    assert (
        manifest[
            "version"
        ]
        == "9.9.9"
    )


def test_default_manifest_path_uses_project_root():

    assert (
        DEFAULT_MANIFEST_PATH
        == (
            PROJECT_ROOT
            / "dist"
            / "manifest.json"
        )
    )
