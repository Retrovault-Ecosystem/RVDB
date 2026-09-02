"""
=========================================================
RVDB Foundation Bundle Builder Tests
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/test_build_bundle_v2.py

Foundation Release:
    0.2

Checkpoint:
    C4 — Final Integration and Release Readiness

=========================================================
"""

import json

from build.builder import (
    build_bundle,
)

from engine.graph import (
    build_graph,
)

from engine.loader import (
    load_entities,
)


def test_build_bundle_contains_all_entities(
    tmp_path,
):

    entities = load_entities()

    graph = build_graph(
        entities
    )

    output = (
        tmp_path
        / "rvdb.bundle.json"
    )

    result = build_bundle(
        graph,
        output,
    )

    assert result == output

    assert output.exists()

    bundle = json.loads(
        output.read_text(
            encoding="utf-8"
        )
    )

    assert set(
        bundle.keys()
    ) == {
        "nodes",
        "edges",
    }

    assert len(
        bundle["nodes"]
    ) == 47

    assert len(
        bundle["edges"]
    ) == 47


def test_build_bundle_serializes_entity_data(
    tmp_path,
):

    graph = build_graph(
        load_entities()
    )

    output = (
        tmp_path
        / "rvdb.bundle.json"
    )

    build_bundle(
        graph,
        output,
    )

    bundle = json.loads(
        output.read_text(
            encoding="utf-8"
        )
    )

    snes = bundle[
        "nodes"
    ][
        "platform.nintendo.snes"
    ]

    assert (
        snes["id"]
        == "platform.nintendo.snes"
    )

    assert (
        snes["type"]
        == "platform"
    )

    assert (
        snes["name"]
        == "Super Nintendo"
    )

    assert (
        snes[
            "relationships"
        ][
            "supports_core"
        ]
        == [
            "core.bsnes",
            "core.snes9x",
        ]
    )


def test_build_bundle_edges_match_graph(
    tmp_path,
):

    graph = build_graph(
        load_entities()
    )

    output = (
        tmp_path
        / "rvdb.bundle.json"
    )

    build_bundle(
        graph,
        output,
    )

    bundle = json.loads(
        output.read_text(
            encoding="utf-8"
        )
    )

    assert bundle[
        "edges"
    ][
        "platform.nintendo.snes"
    ][
        "supports_core"
    ] == [
        "core.bsnes",
        "core.snes9x",
    ]


def test_build_bundle_is_cwd_independent(
    tmp_path,
    monkeypatch,
):

    unrelated_directory = (
        tmp_path
        / "working"
    )

    unrelated_directory.mkdir()

    monkeypatch.chdir(
        unrelated_directory
    )

    graph = build_graph(
        load_entities()
    )

    output = (
        tmp_path
        / "output"
        / "rvdb.bundle.json"
    )

    build_bundle(
        graph,
        output,
    )

    assert output.exists()

    bundle = json.loads(
        output.read_text(
            encoding="utf-8"
        )
    )

    assert len(
        bundle["nodes"]
    ) == 47
