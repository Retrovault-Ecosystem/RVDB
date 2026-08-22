"""
=========================================================
RVDB Foundation CSV Exporter Tests
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/test_csv_exporter_v2.py

Foundation Release:
    0.2.1

Checkpoint:
    D3 — CSV Export Migration

=========================================================
"""

import csv
import json

from build.csv_exporter import (
    export_entities_csv,
)

from engine.loader import (
    Entity,
    load_entities,
)

from engine.paths import (
    DATA_ROOT,
)


def read_rows(
    path,
):

    with path.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as file:

        return list(
            csv.DictReader(
                file
            )
        )


def test_export_entities_csv_with_explicit_columns(
    tmp_path,
):

    entities = [
        {
            "id": "game.example",
            "type": "game",
            "name": "Example Game",
            "release_year": 1994,
        }
    ]

    output = (
        tmp_path
        / "games.csv"
    )

    result = export_entities_csv(
        entities,
        output,
        columns={
            "id": "id",
            "name": "name",
            "year": "release_year",
        },
    )

    assert result == output

    rows = read_rows(
        output
    )

    assert rows == [
        {
            "id": "game.example",
            "name": "Example Game",
            "year": "1994",
        }
    ]


def test_export_entities_csv_supports_entity_objects(
    tmp_path,
):

    entity = Entity(
        source=(
            tmp_path
            / "example.yaml"
        ),
        data={
            "id": "platform.example",
            "type": "platform",
            "name": "Example Platform",
        },
    )

    output = (
        tmp_path
        / "platforms.csv"
    )

    export_entities_csv(
        [
            entity,
        ],
        output,
        columns={
            "id": "id",
            "name": "name",
        },
    )

    rows = read_rows(
        output
    )

    assert rows[
        0
    ][
        "id"
    ] == "platform.example"

    assert rows[
        0
    ][
        "name"
    ] == "Example Platform"


def test_export_entities_csv_serializes_nested_values(
    tmp_path,
):

    entities = [
        {
            "id": "game.example",
            "relationships": {
                "platform": [
                    "platform.example"
                ],
                "core": [
                    "core.example"
                ],
            },
        }
    ]

    output = (
        tmp_path
        / "games.csv"
    )

    export_entities_csv(
        entities,
        output,
        columns={
            "id": "id",
            "platform": (
                "relationships.platform"
            ),
            "core": (
                "relationships.core"
            ),
        },
    )

    rows = read_rows(
        output
    )

    assert json.loads(
        rows[
            0
        ][
            "platform"
        ]
    ) == [
        "platform.example"
    ]

    assert json.loads(
        rows[
            0
        ][
            "core"
        ]
    ) == [
        "core.example"
    ]


def test_export_entities_csv_missing_values_are_empty(
    tmp_path,
):

    entities = [
        {
            "id": "game.example",
            "name": "Example Game",
        }
    ]

    output = (
        tmp_path
        / "games.csv"
    )

    export_entities_csv(
        entities,
        output,
        columns={
            "id": "id",
            "developer": (
                "relationships.developed_by"
            ),
        },
    )

    rows = read_rows(
        output
    )

    assert rows[
        0
    ][
        "developer"
    ] == ""


def test_export_entities_csv_is_cwd_independent(
    tmp_path,
    monkeypatch,
):

    unrelated = (
        tmp_path
        / "working"
    )

    unrelated.mkdir()

    monkeypatch.chdir(
        unrelated
    )

    output = (
        tmp_path
        / "output"
        / "entities.csv"
    )

    export_entities_csv(
        [
            {
                "id": "genre.example",
                "type": "genre",
                "name": "Example",
            }
        ],
        output,
    )

    assert output.exists()

    rows = read_rows(
        output
    )

    assert rows[
        0
    ][
        "id"
    ] == "genre.example"


def test_export_foundation_games_to_csv(
    tmp_path,
):

    games = load_entities(
        DATA_ROOT
        / "games"
    )

    output = (
        tmp_path
        / "games.csv"
    )

    export_entities_csv(
        games,
        output,
        columns={
            "id": "id",
            "name": "name",
            "release_year": (
                "release_year"
            ),
            "developed_by": (
                "relationships.developed_by"
            ),
            "published_by": (
                "relationships.published_by"
            ),
            "platform": (
                "relationships.platform"
            ),
            "genre": (
                "relationships.genre"
            ),
            "core": (
                "relationships.core"
            ),
        },
    )

    rows = read_rows(
        output
    )

    assert len(
        rows
    ) == 4

    galaga = next(
        row
        for row in rows
        if row[
            "id"
        ] == "game.galaga"
    )

    assert (
        galaga[
            "name"
        ]
        == "Galaga"
    )

    assert (
        galaga[
            "release_year"
        ]
        == "1981"
    )

    assert json.loads(
        galaga[
            "platform"
        ]
    ) == []

    assert json.loads(
        galaga[
            "core"
        ]
    ) == []
