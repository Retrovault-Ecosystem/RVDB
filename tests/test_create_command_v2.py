"""
=========================================================
RVDB Dynamic Create Command Tests
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/test_create_command_v2.py

Foundation Release:
    0.2

Checkpoint:
    C2 — Generic Entity Builder

=========================================================
"""

from pathlib import Path

import yaml

import commands.create as create_command

from commands.create import (
    _entity_filename,
    _output_directory,
    cmd_create,
    get_supported_entity_types,
)

from engine.paths import DATA_ROOT


# =====================================================
# Supported Types
# =====================================================

def test_supported_entity_types():

    supported = (
        get_supported_entity_types()
    )

    expected = {
        "core",
        "developer",
        "game",
        "genre",
        "manufacturer",
        "platform",
        "publisher",
    }

    assert (
        set(supported)
        == expected
    )


def test_supported_types_are_sorted():

    supported = (
        get_supported_entity_types()
    )

    assert (
        supported
        == sorted(
            supported
        )
    )


# =====================================================
# Output Paths
# =====================================================

def test_output_directory():

    assert (
        _output_directory(
            "platform"
        )
        == (
            DATA_ROOT
            / "platforms"
        )
    )

    assert (
        _output_directory(
            "developer"
        )
        == (
            DATA_ROOT
            / "developers"
        )
    )

    assert (
        _output_directory(
            "publisher"
        )
        == (
            DATA_ROOT
            / "publishers"
        )
    )


def test_output_directory_is_absolute():

    assert (
        _output_directory(
            "platform"
        ).is_absolute()
    )


def test_entity_filename():

    assert (
        _entity_filename(
            "platform.sega.genesis"
        )
        == "platform_sega_genesis.yaml"
    )


# =====================================================
# Script Mode
# =====================================================

def test_script_mode_creates_entity(
    tmp_path,
    monkeypatch,
):

    output_dir = (
        tmp_path
        / "developers"
    )

    monkeypatch.setattr(
        create_command,
        "_output_directory",
        lambda _entity_type: output_dir,
    )

    entity = cmd_create(
        "developer",
        "developer.example.studio",
        "Example Studio",
    )

    assert entity is not None

    output_file = (
        output_dir
        / "developer_example_studio.yaml"
    )

    assert output_file.exists()

    with output_file.open(
        "r",
        encoding="utf-8",
    ) as file:

        saved = yaml.safe_load(
            file
        )

    assert (
        saved["id"]
        == "developer.example.studio"
    )

    assert (
        saved["type"]
        == "developer"
    )

    assert (
        saved["name"]
        == "Example Studio"
    )


def test_duplicate_file_is_not_overwritten(
    tmp_path,
    monkeypatch,
):

    output_dir = (
        tmp_path
        / "developers"
    )

    output_dir.mkdir(
        parents=True,
    )

    output_file = (
        output_dir
        / "developer_example_studio.yaml"
    )

    output_file.write_text(
        "original content\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        create_command,
        "_output_directory",
        lambda _entity_type: output_dir,
    )

    entity = cmd_create(
        "developer",
        "developer.example.studio",
        "Example Studio",
    )

    assert entity is None

    assert (
        output_file.read_text(
            encoding="utf-8"
        )
        == "original content\n"
    )


# =====================================================
# Unsupported Types
# =====================================================

def test_unsupported_entity_type():

    entity = cmd_create(
        "does_not_exist",
        "does.not.exist",
        "Does Not Exist",
    )

    assert entity is None
