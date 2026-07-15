# RVDB Architecture

## Overview

RVDB (RetroVault Database) is the knowledge foundation behind the RetroVault ecosystem.

The purpose of RVDB is to provide a structured, validated, relationship-aware database containing:

- Retro gaming platforms
- Games
- Developers
- Publishers
- Emulation cores
- Hardware information
- RetroArch configuration metadata
- Visual enhancement data
- Controller information
- BIOS requirements

RVDB is designed as a knowledge graph rather than a simple game list.

---

# Core Architecture

RVDB is separated into multiple layers.

```
                 RetroVault Application
                         |
                         |
                    RVDB Database
                         |
        ---------------------------------
        |               |               |
    Data Layer     Engine Layer    Validation Layer
        |               |               |
       YAML          Graph          Rules
     Entities       Queries        Schemas
```

---

# Data Layer

Location:

```
data/
```

The data layer contains YAML entity definitions.

Examples:

```
data/
├── platforms/
├── games/
├── cores/
├── developers/
├── publishers/
├── genres/
├── controllers/
├── bios/
├── shaders/
├── overlays/
└── themes/
```

YAML files are the source of truth.

---

# Entity System

Every RVDB object is represented as an entity.

Example:

```yaml
id: platform.nintendo.snes
type: platform

name: Super Nintendo

aliases:
  - SNES
  - Super NES
```

Every entity contains:

- Unique ID
- Entity type
- Display name
- Optional aliases
- Optional relationships
- Metadata fields

---

# Relationship Graph

RVDB uses a graph-based architecture.

Entities connect through relationships.

Example:

```
Game
 |
 | developed_by
 |
Developer


Game
 |
 | platform
 |
Platform


Platform
 |
 | supports_core
 |
Core
```

This allows RetroVault to answer questions like:

- What games exist on SNES?
- Which cores support this platform?
- Which developer created this game?
- Which shaders work best for this system?

---

# Engine Layer

Location:

```
engine/
```

The engine provides:

## Entity Loading

Responsible for:

- Discovering YAML files
- Parsing entities
- Creating entity objects


## Graph Construction

Responsible for:

- Building entity nodes
- Creating relationships
- Creating reverse indexes


## Query Engine

Responsible for:

- Searching entities
- Resolving names
- Traversing relationships


## Entity Resolver

Allows natural queries:

Example:

```
rvdb query "Super Nintendo"
```

can resolve:

```
platform.nintendo.snes
```

---

# Validation Layer

Location:

```
validator/
```

Responsible for maintaining database integrity.

Includes:

## Schema Validation

Checks:

- Required fields
- Data types
- Supported entity types
- Unknown fields


## Relationship Validation

Checks:

- Valid relationship names
- Valid target entity types
- Broken references

---

# Command Layer

Location:

```
commands/
```

Provides CLI access.

Current commands include:

```
validate
build
query
list
show
info
related
cores
who-uses
find
```

---

# Build System

The build system converts RVDB into application-ready formats.

Future outputs:

```
build/
├── json/
├── csv/
├── indexes/
├── manifests/
└── application_data/
```

---

# Design Principles

RVDB follows these principles:

1. YAML is the source of truth.
2. Entities are reusable building blocks.
3. Relationships define knowledge.
4. Validation prevents corruption.
5. The database grows independently from applications.
6. RetroVault applications consume RVDB rather than duplicate data.

---

# Future Expansion

Planned additions:

- Complete console database
- Arcade hardware database
- Emulator compatibility database
- Libretro core database
- Shader database
- Overlay database
- Controller database
- BIOS database
- Artwork metadata
- Automated metadata importing
