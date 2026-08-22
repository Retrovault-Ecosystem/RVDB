# RVDB Current Milestone

_Last Updated: 2026-08-22_

---

# Project

RetroVault Database (RVDB)

Repository Branch:

feature/relationship-resolver

Project Status:

Foundation Release 0.2 — Checkpoint C3 Complete

---

# Foundation Release 0.2 Status

## Checkpoint A — Schema Foundation

✔ COMPLETE

Implemented:

- Dynamic SchemaLoader
- Common + entity schema merging
- Schema-driven validation
- TypeRegistry
- Entity reference types
- Entity registry integration
- Canonical schema foundation
- Foundation 0.2 data normalization

Commit:

4ae064d Foundation 0.2 Checkpoint A: complete schema foundation

---

## Checkpoint B — Schema / Type Test Foundation

✔ COMPLETE

Implemented:

- SchemaLoader tests
- TypeRegistry tests
- EntityReferenceValidator tests
- SchemaValidator tests
- Foundation 0.2 pytest test layer

Commit:

9ea4957 Foundation 0.2 Checkpoint B: add schema engine test suite

---

## Checkpoint C1 — Complete Entity Template Layer

✔ COMPLETE

Active entity templates:

- core
- developer
- game
- genre
- manufacturer
- platform
- publisher

Every active Foundation 0.2 entity type has:

- schemas/entities/<type>.yaml
- templates/entities/<type>.yaml

Commit:

f1ec2d7 Foundation 0.2 Checkpoint C1: complete entity template layer

---

## Checkpoint C2 — Generic Schema-Driven Entity Builder

✔ COMPLETE

Implemented:

- Generic EntityBuilder
- Schema-driven field prompting
- Dynamic entity-type discovery
- Generic create command
- Template-based structural defaults
- Canonical ID generation
- Typed entity reference resolution
- Human-readable relationship lookup
- Entity preview
- Save confirmation
- Duplicate-file protection
- Validation before write
- Project-root-aware paths
- CLI operation independent of current working directory

Supported field types:

- string
- integer
- integer_or_null
- boolean
- list
- object
- entity_reference
- entity_reference_list

Checkpoint result:

45 tests passing

Commit:

26cc76c Foundation 0.2 Checkpoint C2: add generic schema-driven entity builder

Tag:

foundation-0.2-c2

---

# Checkpoint C3 — Schema-Driven Relationships

✔ COMPLETE

Checkpoint C3 replaced hardcoded Python relationship rules with
schema-defined relationship architecture.

---

## C3a — Relationship Rules in Entity Schemas

✔ COMPLETE

Implemented:

- Relationship definitions added to entity schemas
- SchemaLoader relationship merging
- SchemaLoader get_relationships()
- RelationshipValidator converted from hardcoded rules
  to schema-driven validation
- Relationship target types defined in YAML
- Core relationship vocabulary normalized to active data/template usage

Current schema-defined relationships include:

### Game

- developed_by → developer
- published_by → publisher
- platform → platform
- genre → genre
- core → core

### Platform

- supports_core → core

### Core

- supports → platform

Commit:

f40bbba Foundation 0.2 Checkpoint C3a: move relationship rules into schemas

---

## C3b — Relationship Schema Validation and Builder Integration

✔ COMPLETE

Implemented:

- SchemaDefinitionError
- Relationship schema validation during SchemaLoader initialization
- Relationship type validation
- Required target entity-type definitions
- Unknown target-type rejection
- entity_type / entity_types mutual-exclusion validation
- Future multi-target relationship support
- EntityBuilder now reads relationship vocabulary from schemas
- Template relationship placeholders are no longer authoritative
- Generic relationship prompting
- Canonical relationship-ID resolution
- Relationship builder tests
- Relationship schema-definition tests

Commit:

3d37f8e Foundation 0.2 Checkpoint C3b: validate and build schema relationships

---

## C3c — Relationship Data Hardening

✔ COMPLETE

Implemented:

- Relationship container validation
- Unknown relationship rejection
- Relationship cardinality enforcement
- entity_reference validation
- entity_reference_list validation
- Empty/reference string validation
- Separation between structural validation and graph validation

Commit:

fa7553e Foundation 0.2 Checkpoint C3c: harden schema relationship data validation

Tag:

foundation-0.2-c3

---

# C3 Final Architecture

Relationship processing now follows:

Entity Schema

↓

SchemaLoader

- loads relationship definitions
- validates schema definitions
- validates target entity-type declarations

↓

EntityBuilder

- reads relationship definitions
- prompts for relationship values
- resolves names and aliases
- stores canonical entity IDs

↓

SchemaValidator

- validates relationship container
- rejects unknown relationship names
- validates relationship cardinality
- validates stored reference shape

↓

RelationshipValidator

- validates source entity type
- validates relationship legality
- validates target entity type

↓

RVGraph

- stores forward edges
- builds reverse edges
- supports relationship traversal

---

# Relationship Responsibility Boundaries

## SchemaLoader

Responsible for:

- relationship schema correctness
- relationship type definitions
- target entity-type declarations

Not responsible for entity data.

---

## EntityBuilder

Responsible for:

- interactive relationship entry
- relationship lookup
- canonical ID storage

Not responsible for defining relationship vocabulary.

---

## SchemaValidator

Responsible for:

- relationship data structure
- allowed relationship names
- relationship cardinality
- reference string structure

Not responsible for determining whether target IDs actually exist.

---

## RelationshipValidator

Responsible for:

- source → relationship legality
- relationship → target-type legality

Relationship rules come exclusively from schemas.

No hardcoded Python relationship matrix remains.

---

## RVGraph

Responsible for:

- entity nodes
- forward relationship edges
- reverse relationship edges

Graph behavior remains generic and does not define relationship legality.

---

# Current Foundation Health

End-of-C3 verification:

Tests:

73 passed

Database validation:

Entities checked: 19

Valid: 19

Schema Errors: 0

Relationship Errors: 0

Validation:

OK

Working tree:

clean

Remote branch:

origin/feature/relationship-resolver

Status:

synchronized

---

# Current Active Entity Types

Foundation 0.2 currently supports:

- core
- developer
- game
- genre
- manufacturer
- platform
- publisher

Each active entity type has:

- schema support
- template support
- generic builder support
- schema validation support

Relationship-capable types currently include:

- game
- platform
- core

---

# Current Architecture

RVDB entity creation:

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

RelationshipValidator

↓

Preview / Confirmation

↓

YAML output

↓

RVGraph / Reverse Relationship Index

---

# Architectural Principles

1. YAML schemas define entity behavior.

2. Python should implement generic infrastructure rather than
   entity-specific rules.

3. Entity relationship vocabulary belongs in schemas.

4. Canonical entity IDs are stored in RVDB data.

5. Human-readable names and aliases are resolved only during entry.

6. SchemaValidator validates entity structure.

7. RelationshipValidator validates relationship semantics.

8. RVGraph manages relationship traversal and reverse indexes.

9. Templates provide structural/default entity data.

10. Templates must not become a second relationship-definition system.

11. YAML remains the canonical RVDB data representation.

12. RetroVault and future RVDB consumers should use the same schema layer.

---

# Canonical ID Rules

Canonical IDs use dot notation.

Examples:

platform.sega.genesis

game.super.mario.world

developer.nintendo.ead

genre.role.playing.game

Underscores may remain where required by existing canonical IDs or
controlled legacy migration.

---

# Legacy Package Rule

The inner legacy package:

rvdb/

must remain untouched during Foundation Release 0.2.

Legacy cleanup is deferred to:

Foundation Release 0.2.1 — Legacy Cleanup

Do not delete, rename, migrate, or rewrite legacy package files during
Foundation 0.2 without a separate controlled audit.

Legacy files are preserved intentionally.

---

# Deferred Relationship Features

The following are intentionally NOT required for C3 completion:

- required relationships
- minimum relationship cardinality
- maximum relationship cardinality
- automatic bidirectional relationship storage
- inverse relationship declarations
- relationship metadata
- relationship ordering
- relationship weighting

These may be introduced later only when a concrete RVDB requirement
justifies them.

---

# Next Checkpoint

## Foundation 0.2 — Checkpoint C4

### Final Integration and Release Readiness

Status:

NOT STARTED

Primary goal:

Audit Foundation 0.2 as a complete system before declaring the release
candidate ready.

Expected areas:

- CLI integration
- SchemaLoader
- TypeRegistry
- EntityBuilder
- EntityFactory
- SchemaValidator
- RelationshipValidator
- EntityReferenceValidator
- RelationshipLookup
- RVGraph
- reverse relationships
- production data
- tests
- build/export compatibility
- project paths
- documentation

Checkpoint C4 should begin with a read-only integration inventory.

Do not begin legacy cleanup during C4.

---

# Foundation 0.2.1

Planned:

Legacy Cleanup

Potential audit targets include:

- inner rvdb/ package
- duplicate/obsolete modules
- backup Python files
- obsolete CLI implementations
- empty historical files
- stale build artifacts

No file should be deleted merely because it appears obsolete.

Every cleanup candidate must first be:

1. identified
2. dependency-checked
3. Git-history checked
4. backed up
5. explicitly approved for removal

---

# End-of-Session Rules

Before ending a development session:

1. Run the complete pytest suite.
2. Run RVDB production validation.
3. Confirm the intended Git branch.
4. Confirm the working tree is clean.
5. Commit completed checkpoints.
6. Push commits to GitHub.
7. Tag major Foundation checkpoints.
8. Update this milestone document.
9. Push milestone documentation.
10. Never leave temporary entities in data/.
11. Never casually delete legacy files.
12. Prefer small, tested, reversible changes.

---

# Resume Instructions

To continue development:

Continue RVDB Project.

Read docs/current_milestone.md and continue from the current milestone.

Expected restart point:

Foundation 0.2 — Checkpoint C4

Final Integration and Release Readiness

Status:

NOT STARTED

Begin with a read-only Foundation 0.2 integration inventory.
