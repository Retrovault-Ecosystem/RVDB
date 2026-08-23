# RetroVault Database (RVDB)

RVDB is the structured knowledge database for the RetroVault ecosystem.

It provides a schema-driven, validated, relationship-aware data layer for
retro-gaming platforms, games, emulator cores, developers, publishers,
genres, BIOS information, controllers, shaders, overlays, themes, and
related metadata.

RVDB is designed as a knowledge graph rather than a simple game list.

## Current Version

RVDB 0.2.1

Foundation 0.2 established the production architecture.

Foundation 0.2.1 focuses on controlled legacy cleanup, runtime
normalization, reproducible installation, and release readiness.

## Architecture

RVDB uses a data-driven architecture built around:

- YAML entity data
- YAML entity schemas
- YAML entity templates
- generic entity construction
- schema-driven validation
- schema-driven relationships
- canonical dot-notation entity IDs
- canonical project paths
- entity registry services
- relationship resolution
- forward and reverse relationship graphs
- canonical bundle generation
- automated regression testing

YAML is the canonical source representation.

Generated artifacts such as `rvdb.bundle.json` are derived from the
validated source data.

## Repository Layout

Key project directories include:

```text
build/       Build and export infrastructure
commands/    CLI command implementations
data/        Canonical YAML entity data
docs/        Project architecture and development documentation
engine/      Loading, querying, graph, entity, and relationship engine
schemas/     YAML entity schemas
services/    Runtime registry services
templates/   YAML entity templates
tests/       Automated regression tests
validator/   Schema and relationship validation
```

## Requirements

RVDB currently requires:

- Python 3.10 or newer
- PyYAML 6.0 or newer

The runtime dependency is declared in `requirements.txt`.

Development and regression testing additionally require `pytest`.

## Installation

Clone the repository:

```bash
git clone https://github.com/Retrovault-Ecosystem/RVDB.git
cd RVDB
```

Create an isolated Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the runtime dependency:

```bash
python -m pip install -r requirements.txt
```

Verify the installation:

```bash
python cli.py version
python cli.py validate
python cli.py build
```

A successful installation should report RVDB 0.2.1 and complete
validation without schema or relationship errors.

## Existing Checkout

If RVDB is already cloned, do not clone it again. Enter the existing
checkout and activate its project virtual environment:

```bash
cd /path/to/RVDB
source .venv/bin/activate
```

Then install or refresh the runtime requirements if needed:

```bash
python -m pip install -r requirements.txt
```

## Development Setup

Install pytest for development:

```bash
python -m pip install pytest
```

Run the complete regression suite:

```bash
python -m pytest -q
```

## Command-Line Interface

Display CLI help:

```bash
python cli.py --help
```

Current commands include:

```text
version
validate
build
query
list
show
info
cores
who-uses
related
find
developed-by
published-by
games-on
create
```

Several commands also provide aliases.

Examples:

```bash
python cli.py version
python cli.py validate
python cli.py build
python cli.py list platform
python cli.py query "Super Nintendo"
python cli.py find "Nintendo"
```

Use command-specific help for additional options. For example:

```bash
python cli.py list --help
python cli.py query --help
```

## Validation

Run production validation with:

```bash
python cli.py validate
```

The validator checks entity structure and relationship integrity against
the canonical schemas.

## Build

Generate the canonical RVDB bundle with:

```bash
python cli.py build
```

The canonical bundle is written to:

```text
rvdb.bundle.json
```

`rvdb.bundle.json` is an output file, not a command.

Build output is generated from the validated YAML source data.

## Entity IDs

Canonical RVDB entity IDs use dot notation.

Examples:

```text
platform.sega.genesis
platform.nintendo.snes
game.super.mario.world
developer.nintendo.ead
genre.role.playing.game
```

Canonical IDs should not introduce underscores unless explicitly
preserved through an override or compatibility rule.

## Project Principles

RVDB follows several core principles:

1. YAML is the source of truth.
2. Schemas define entity structure.
3. Templates define new entity skeletons.
4. Validation derives from schemas.
5. Relationships derive from schemas.
6. Canonical IDs provide stable references.
7. Runtime resources use canonical project paths.
8. The entity registry is the runtime source of truth.
9. Generated artifacts are derived from canonical source data.
10. RVDB remains independent of any single consumer application.

## Documentation

Additional project documentation is available in:

```text
docs/architecture.md
docs/development.md
docs/roadmap.md
docs/changelog.md
docs/current_milestone.md
```

`docs/current_milestone.md` records the detailed architectural history,
checkpoint state, safety rules, and current development milestone.

## Project Status

Foundation 0.2 architecture is stable.

Foundation 0.2.1 has completed the controlled retirement of the
historical inner runtime, subsequent non-runtime cleanup, branch
integration, and clean-clone reproducibility verification.

The project is currently completing its Foundation 0.2.1 release
documentation and metadata.

## License

License metadata has not yet been finalized for the Foundation 0.2.1
release.

See `LICENSE` once the project's license decision has been formally
recorded.
