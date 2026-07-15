# RVDB Development Guide


## Project Structure

RVDB is organized into separate layers.


## Data Layer

Location:

data/

Contains YAML entity definitions.

Examples:

- platforms
- games
- cores
- developers
- publishers


## Engine Layer

Location:

engine/

Responsible for:

- loading entities
- graph creation
- querying
- resolving relationships


## Validation Layer

Location:

validator/

Responsible for:

- schema validation
- relationship validation
- database integrity


## Command Layer

Location:

commands/

Provides CLI functionality.

Examples:

- validate
- build
- query
- related


## Build System

Build processes generate:

- indexes
- manifests
- exports
- application-ready data


## Development Rules

1. YAML files are the source of truth.
2. Relationships reference entity IDs.
3. Avoid duplicate metadata.
4. Validate after structural changes.
5. Commit completed features to Git.
