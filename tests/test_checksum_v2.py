"""
=========================================================
RVDB Foundation Checksum Builder Tests
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    tests/test_checksum_v2.py

Foundation Release:
    0.2.1

Checkpoint:
    D2 — Checksum Migration

=========================================================
"""

import hashlib

from build.checksum import (
    DEFAULT_CHECKSUM_PATH,
    build_checksums,
    sha256_file,
)

from engine.paths import (
    PROJECT_ROOT,
)


def test_sha256_file(
    tmp_path,
):

    source = (
        tmp_path
        / "artifact.json"
    )

    content = b"RetroVault Database"

    source.write_bytes(
        content
    )

    expected = hashlib.sha256(
        content
    ).hexdigest()

    assert (
        sha256_file(
            source
        )
        == expected
    )


def test_build_checksums_creates_manifest(
    tmp_path,
):

    first = (
        tmp_path
        / "first.json"
    )

    second = (
        tmp_path
        / "second.json"
    )

    first.write_text(
        "first",
        encoding="utf-8",
    )

    second.write_text(
        "second",
        encoding="utf-8",
    )

    output = (
        tmp_path
        / "dist"
        / "checksums.sha256"
    )

    result = build_checksums(
        [
            first,
            second,
        ],
        output,
    )

    assert result == output

    assert output.exists()

    lines = (
        output
        .read_text(
            encoding="utf-8"
        )
        .splitlines()
    )

    assert len(
        lines
    ) == 2

    assert lines[0] == (
        f"{sha256_file(first)}  "
        "first.json"
    )

    assert lines[1] == (
        f"{sha256_file(second)}  "
        "second.json"
    )


def test_build_checksums_skips_missing_files(
    tmp_path,
):

    existing = (
        tmp_path
        / "existing.json"
    )

    missing = (
        tmp_path
        / "missing.json"
    )

    existing.write_text(
        "existing",
        encoding="utf-8",
    )

    output = (
        tmp_path
        / "checksums.sha256"
    )

    build_checksums(
        [
            existing,
            missing,
        ],
        output,
    )

    lines = (
        output
        .read_text(
            encoding="utf-8"
        )
        .splitlines()
    )

    assert lines == [
        (
            f"{sha256_file(existing)}  "
            "existing.json"
        )
    ]


def test_build_checksums_is_cwd_independent(
    tmp_path,
    monkeypatch,
):

    source = (
        tmp_path
        / "artifact.json"
    )

    source.write_text(
        "artifact",
        encoding="utf-8",
    )

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
        / "checksums.sha256"
    )

    build_checksums(
        [
            source,
        ],
        output,
    )

    assert output.exists()

    assert (
        output.read_text(
            encoding="utf-8"
        ).strip()
        == (
            f"{sha256_file(source)}  "
            "artifact.json"
        )
    )


def test_default_checksum_path_uses_project_root():

    assert (
        DEFAULT_CHECKSUM_PATH
        == (
            PROJECT_ROOT
            / "dist"
            / "checksums.sha256"
        )
    )
