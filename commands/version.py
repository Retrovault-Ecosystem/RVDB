"""
RVDB version command.

The runtime version must identify the current RVDB release rather than
the historical placeholder version from the initial project skeleton.
"""

VERSION = "0.2.1"


def cmd_version():
    print(f"RVDB {VERSION}")
