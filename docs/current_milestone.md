# RVDB Current Milestone

_Last Updated: 2026-08-21_

---

# Project

RetroVault Database (RVDB)

Repository Branch:

feature/relationship-resolver

Project Status:

Foundation Release 0.2 — Checkpoint C2 Complete

---

# Current Foundation Status

## Checkpoint A — Schema Foundation

✔ COMPLETE

Completed:

- Dynamic SchemaLoader
- Common + entity schema merging
- Schema-driven validation
- TypeRegistry
- Entity reference types
- Entity registry integration
- Canonical schema foundation
- Data normalization required for Foundation 0.2

Commit:

4ae064d Foundation 0.2 Checkpoint A: complete schema foundation

---

## Checkpoint B — Schema / Type Test Foundation

✔ COMPLETE

Completed:

- SchemaLoader tests
- TypeRegistry tests
- EntityReferenceValidator tests
- SchemaValidator tests
- Legacy tests preserved and excluded from Foundation 0.2 pytest collection

Checkpoint result:

30 tests passing

Commit:

9ea4957 Foundation 0.2 Checkpoint B: add schema engine test suite

---

## Checkpoint C1 — Complete Entity Template Layer

✔ COMPLETE

Completed entity templates:

- core
- developer
- game
- genre
- manufacturer
- platform
- publisher

All active entity types now have both:

- schemas/entities/<type>.yaml
- templates/entities/<type>.yaml

Commit:

f1ec2d7 Foundation 0.2 Checkpoint C1: complete entity template layer

---

## Checkpoint C2 — Generic Schema-Driven Entity Builder

✔ COMPLETE

Completed:

- Generic EntityBuilder
- Removed platform-only interactive builder architecture
- Schema-driven field prompting
- Generic support for:
  - string
  - integer
  - integer_or_null
  - boolean
  - list
  - object
  - entity_reference
  - entity_reference_list
- Typed entity relationship resolution
- Canonical ID acceptance
- Entity preview
- Save confirmation
- Template placeholder cleanup
- Dynamic create-command entity discovery
- Create support for all active entity types
- Validation before entity write
- Duplicate-file protection
- Project-root-aware filesystem paths
- CLI no longer depends on current working directory
- Dedicated builder and create-command regression tests

Checkpoint result:

45 tests passing

Database validation:

Entities checked: 19
Valid: 19
Schema Errors: 0
Relationship Errors: 0
Validation OK

Commit:

26cc76c Foundation 0.2 Checkpoint C2: add generic schema-driven entity builder

Tag:

foundation-0.2-c2

---

# Current Active Entity Types

The Foundation 0.2 schema/template system currently supports:

- core
- developer
- game
- genre
- manufacturer
- platform
- publisher

Each active type has:

- a schema
- a template
- generic builder support
- schema validation support

---

# Current Architecture

RVDB now follows this creation path:

CLI

↓

SchemaLoader

↓

EntityBuilder

↓

IDGenerator

↓

EntityFactory

↓

RelationshipLookup / EntityReferenceValidator

↓

SchemaValidator

↓

Preview

↓

Confirmation

↓

YAML output

---

# Project Path Architecture

Foundation 0.2 now uses centralized project paths.

Project resources are resolved from the RVDB codebase itself rather than the shell's current working directory.

Canonical project paths include:

- data/
- schemas/
- schemas/entities/
- templates/
- templates/entities/
- config/

The CLI can therefore be invoked from outside the repository without losing access to schemas, templates, or entity data.

---

# Current Design Decisions

Canonical IDs use dot notation.

Examples:

platform.sega.genesis

game.super.mario.world

developer.nintendo.ead

genre.role.playing.game

No underscores in canonical IDs unless explicitly preserved through ID overrides or legacy migration requirements.

Interactive builders should:

1. Generate canonical IDs automatically.
2. Use schema definitions rather than hardcoded entity fields.
3. Resolve typed entity references.
4. Show a preview.
5. Ask for confirmation before writing.
6. Validate before saving.
7. Protect existing entity files from accidental overwrite.

---

# Architectural Principles

RVDB follows a data-driven architecture.

1. Schemas define entities.

   Python should not hardcode entity-specific fields.

2. The Entity Registry is the source of truth for loaded entities.

3. Stored canonical references are validated through EntityReferenceValidator.

4. Human-entered names and aliases are resolved through RelationshipLookup.

5. Builders are generic.

6. Validation is schema-driven.

7. YAML is the canonical representation of RVDB data.

8. Future applications should consume the same schemas.

This includes:

- CLI
- RetroVault GUI
- Web API
- documentation
- importers
- migration tools
- metadata tools

---

# Legacy Package Rule

The inner legacy package:

rvdb/

must remain untouched during Foundation Release 0.2.

Legacy cleanup is deferred to:

Foundation Release 0.2.1 — Legacy Cleanup

Do not delete, rename, or rewrite legacy components before that controlled cleanup phase.

Legacy tests remain preserved.

---

# Next Checkpoint

## Foundation 0.2 — Checkpoint C3

### Schema-Driven Relationships

Status:

NOT STARTED

Primary goal:

Move relationship definitions out of hardcoded validators and template-only structures and into the schema system.

Expected investigation areas:

- validator/relationships.py
- relationship resolver
- reverse relationship index
- RelationshipLookup
- EntityReferenceValidator
- relationship definitions in templates
- relationship fields in existing data
- relationship-related tests

Checkpoint C3 should begin with a read-only inventory.

Do not modify relationship architecture until the current relationship system has been fully mapped.

---

# Important C3 Design Goal

Relationship behavior should eventually be schema-defined.

Example direction:

```yaml
relationships:

  developed_by:
    type: entity_reference_list
    entity_type: developer

  published_by:
    type: entity_reference_list
    entity_type: publisher

  platform:
    type: entity_reference_list
    entity_type: platform
