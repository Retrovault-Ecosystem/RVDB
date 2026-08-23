"""
Regression coverage for the RVDB runtime version command.
"""

from commands.version import VERSION, cmd_version


EXPECTED_VERSION = "0.2.1"


def test_runtime_version_constant():
    assert VERSION == EXPECTED_VERSION


def test_runtime_version_command(capsys):
    cmd_version()

    captured = capsys.readouterr()

    assert captured.out == (
        f"RVDB {EXPECTED_VERSION}\n"
    )


def test_cli_version_matches_runtime_version():
    assert VERSION == "0.2.1"
