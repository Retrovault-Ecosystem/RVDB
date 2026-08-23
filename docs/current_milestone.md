# RVDB Current Milestone

_Last Updated: 2026-08-23_

---

# Project

RetroVault Database (RVDB)

Repository Branch:

develop

Project Status:

Foundation Release 0.2 — COMPLETE

Release Status:

RELEASE READY

---

# Foundation 0.2 Overview

Foundation 0.2 establishes the schema-driven architectural foundation
for the RetroVault Database.

The release moves RVDB away from hardcoded entity definitions,
validation rules, relationship matrices, builder logic, and
working-directory-dependent resource paths.

The Foundation 0.2 architecture is now centered around:

- YAML entity schemas
- YAML entity templates
- Generic entity construction
- Schema-driven validation
- Schema-driven relationships
- Canonical entity IDs
- Canonical project paths
- Entity registry services
- Relationship resolution
- Forward and reverse relationship graphs
- Canonical bundle generation
- Automated regression testing

The goal of Foundation 0.2 was not to expand the database itself.

The goal was to establish a stable architecture upon which the
larger RVDB knowledge base can safely be built.

---

# Core Architectural Principles

RVDB follows a data-driven architecture.

## 1. Schemas Define Entities

Python should not hardcode entity fields.

Entity structure belongs in YAML schemas.

---

## 2. Templates Define New Entity Skeletons

Interactive entity creation should use templates rather than
entity-specific Python builders.

Adding a new entity type should ultimately require:

- one schema
- one template

without requiring a new Python builder.

---

## 3. Validation Is Schema-Driven

Entity validation should derive its rules from the same schemas
that define the entities.

This includes:

- required fields
- optional fields
- field types
- relationship structure

---

## 4. Relationships Are Schema-Driven

Relationship definitions belong in entity schemas.

Python must not maintain a separate hardcoded relationship matrix.

Relationship definitions specify:

- relationship name
- relationship value type
- target entity type

---

## 5. Canonical IDs Use Dot Notation

Examples:

platform.sega.genesis

platform.nintendo.snes

game.super.mario.world

developer.nintendo.ead

genre.role.playing.game

Underscores should not be introduced into canonical IDs unless
explicitly preserved through an ID override or compatibility rule.

---

## 6. Project Resources Use Canonical Paths

Runtime behavior must not depend on the shell's current working
directory.

Project resources are resolved relative to the RVDB project root.

Examples include:

- data
- schemas
- templates
- config
- bundle output

---

## 7. The Entity Registry Is the Runtime Source of Truth

Loaded entities are exposed through the registry layer.

Runtime consumers should use the current registry and graph
architecture rather than historical loaders or duplicated data
structures.

---

## 8. YAML Is the Canonical Source Representation

RVDB entity data is maintained in YAML.

Generated artifacts such as the canonical JSON bundle are derived
from that source data.

---

# Foundation 0.2 Completed Architecture

The following major architectural components are operational.

- SchemaLoader
- SchemaValidator
- RelationshipValidator
- Type Registry
- Entity Reference Validation
- Entity Templates
- EntityFactory
- Generic EntityBuilder
- Namespace ID Generator
- Relationship Lookup
- Entity Resolver
- Entity Registry
- Entity Loader
- Runtime Context
- Forward Relationship Graph
- Reverse Relationship Graph
- Canonical Bundle Build
- Project Path Layer
- CLI Validation Workflow
- CLI Create Workflow
- CLI Build Workflow
- Automated Foundation Test Suite

---

# Foundation 0.2 Checkpoints

## Checkpoint A — Schema Foundation

✔ COMPLETE

Established the Foundation 0.2 schema architecture.

Implemented:

- common entity schema
- entity-specific schemas
- schema loading
- common/entity schema merging
- dynamic field definitions
- schema-based entity type discovery
- schema validation foundation
- type registry
- entity reference validation

Checkpoint commit:

4ae064d Foundation 0.2 Checkpoint A: complete schema foundation

---

## Checkpoint B — Schema Engine Test Suite

✔ COMPLETE

Established regression coverage for the Foundation schema engine.

Coverage includes:

- schema discovery
- common field merging
- entity field merging
- schema isolation
- unknown schemas
- type registry behavior
- entity reference validation
- typed references
- reference lists

Checkpoint commit:

9ea4957 Foundation 0.2 Checkpoint B: add schema engine test suite

---

## Checkpoint C1 — Entity Template Layer

✔ COMPLETE

Completed the schema-aligned entity template layer.

Entity types with both schemas and templates:

- core
- developer
- game
- genre
- manufacturer
- platform
- publisher

The EntityFactory can create template-backed entities for all active
Foundation entity types.

Checkpoint commit:

f1ec2d7 Foundation 0.2 Checkpoint C1: complete entity template layer

---

## Checkpoint C2 — Generic Schema-Driven Entity Builder

✔ COMPLETE

Replaced the entity-specific creation direction with a generic
schema-driven entity builder.

Implemented:

- schema-discovered entity types
- generic template-backed creation
- automatic canonical ID generation
- schema-driven field prompting
- string fields
- integer fields
- nullable integer fields
- boolean fields
- list fields
- object fields
- entity references
- entity reference lists
- relationship lookup integration
- entity preview
- save confirmation
- duplicate-file protection
- project-root-aware output paths
- create command regression tests
- entity builder regression tests

Checkpoint commit:

26cc76c Foundation 0.2 Checkpoint C2: add generic schema-driven entity builder

Safety tag:

foundation-0.2-c2

---

## Checkpoint C3 — Schema-Driven Relationships

✔ COMPLETE

Checkpoint C3 completed the migration of relationship behavior into
the schema architecture.

### C3a — Relationship Rules in Schemas

Implemented:

- relationship definitions in entity schemas
- schema-driven RelationshipValidator
- removal of the hardcoded relationship matrix
- relationship target-type validation
- relationship validator regression tests

Commit:

f40bbba Foundation 0.2 Checkpoint C3a: move relationship rules into schemas

---

### C3b — Relationship Schema Validation and Builder Integration

Implemented:

- relationship schema loading
- relationship schema validation
- relationship metadata access through SchemaLoader
- generic builder relationship prompting
- schema-driven relationship construction
- relationship schema regression tests
- expanded EntityBuilder relationship tests

Commit:

3d37f8e Foundation 0.2 Checkpoint C3b: validate and build schema relationships

---

### C3c — Relationship Data Validation Hardening

Implemented:

- schema-level validation of relationship containers
- relationship value-type validation
- relationship key validation
- malformed relationship detection
- separation between structural schema validation and
  cross-entity relationship validation
- expanded relationship data validation regression coverage

Commit:

fa7553e Foundation 0.2 Checkpoint C3c: harden schema relationship data validation

Safety tag:

foundation-0.2-c3

---

# Checkpoint C4 — Final Integration and Release Readiness

✔ COMPLETE

Checkpoint C4 integrated the Foundation architecture into the active
runtime paths, build system, and resolver test coverage.

---

## C4a — Canonical Runtime Path Integration

✔ COMPLETE

Implemented:

- canonical DATA_ROOT integration
- CWD-independent validation
- CWD-independent engine context
- CWD-independent entity registry
- CWD-independent default entity loading
- canonical project resource paths
- project path regression tests

Commit:

ede762f Foundation 0.2 Checkpoint C4a: complete canonical runtime path integration

---

## C4b — Canonical Bundle Build Integration

✔ COMPLETE

Implemented:

- active CLI build command using the Foundation architecture
- canonical rvdb.bundle.json regeneration
- current EntityLoader → RVGraph → bundle pipeline
- plain entity-data serialization
- canonical project output path
- CWD-independent build execution
- bundle contract regression tests

Canonical bundle contract:

- nodes
- edges

Current production bundle:

Nodes: 19

Edges: 19

Commit:

9174550 Foundation 0.2 Checkpoint C4b: integrate canonical bundle build

---

## C4c — Resolver Integration Coverage

✔ COMPLETE

Implemented regression coverage for:

- exact canonical ID resolution
- exact name resolution
- alias resolution
- case-insensitive alias resolution
- partial-name resolution
- missing-entity behavior
- resolver operation outside the project working directory

Commit:

3254736 Foundation 0.2 Checkpoint C4c: add resolver integration coverage

---

# Foundation 0.2 Final Release Gate

✔ PASSED

The complete Foundation 0.2 release gate was executed after
Checkpoint C4c.

## Compilation

PASS

Foundation Python modules and tests compiled successfully.

---

## Automated Test Suite

Result:

89 passed

Status:

PASS

---

## Production Database Validation

Entities checked:

19

Valid:

19

Schema Errors:

0

Relationship Errors:

0

Result:

Validation OK

Status:

PASS

---

## Canonical Bundle Build

Graph Nodes:

19

Graph Edges:

19

Bundle:

rvdb.bundle.json

Result:

Build complete

Status:

PASS

---

## Bundle Contract

Top-level keys:

- nodes
- edges

Nodes:

19

Edges:

19

Entity IDs were verified against their bundle node keys.

Result:

PASS

---

## External Working Directory Validation

The production validator was executed from `/tmp` rather than from
the RVDB project directory.

Result:

Validation OK

Status:

PASS

---

## External Working Directory Build

The production build command was executed from `/tmp`.

The generated bundle was correctly written to the canonical project
location:

/home/oilcan/rvdb/rvdb.bundle.json

No stray `/tmp/rvdb.bundle.json` was created.

Status:

PASS

---

## Active Foundation Import Check

Active Foundation modules were checked for imports from the
historical inner `rvdb/` package.

Result:

NONE

Status:

PASS

---

## Legacy Distribution Artifact Check

The historical `dist/` artifacts were checked after validation and
build execution.

Modifications:

NONE

Status:

PASS

---

## Git State

Branch:

feature/relationship-resolver

Release-gate HEAD:

3254736e7085779acd05040f991da2f559a7e32e

Remote branch:

origin/feature/relationship-resolver

Working tree during release gate:

CLEAN

Local branch synchronized with remote:

YES

Status:

PASS

---

# Foundation Release 0.2

Status:

COMPLETE

Release readiness:

PASS

Foundation 0.2 establishes the production architecture for RVDB.

The release provides:

- schema-driven entities
- schema-driven validation
- schema-driven relationships
- generic entity creation
- canonical IDs
- canonical project paths
- entity registry services
- relationship resolution
- forward relationship graph
- reverse relationship graph
- canonical bundle generation
- CWD-independent runtime behavior
- automated regression testing

Final Foundation 0.2 test count:

89

Final production entity count:

19

Final production validation:

19 valid

0 schema errors

0 relationship errors

Final canonical graph:

19 nodes

19 edge entries

Foundation 0.2 is ready for the final documentation commit and
release tag.

---

# Historical Safety Tags

Foundation checkpoints currently protected by Git tags:

foundation-0.2-c2

foundation-0.2-c3

The final Foundation release will be protected by:

foundation-0.2

---

# Long-Term RVDB Vision

RVDB is evolving from a YAML database into the knowledge layer for
the entire RetroVault ecosystem.

Future applications should consume the same canonical schemas and
data architecture rather than maintaining separate definitions.

Potential consumers include:

- RetroVault desktop application
- CLI tools
- GUI administration tools
- Web APIs
- documentation generators
- search systems
- metadata exporters
- compatibility tools
- emulator configuration tools
- artwork and media tools

The Foundation architecture should remain independent of any single
consumer application.

---

# Next Release

## Foundation 0.2.1 — Legacy Cleanup

Status:

COMPLETE

Primary goal:

Perform a controlled audit and cleanup of obsolete, duplicate,
historical, transitional, and accidentally tracked project files
without disturbing the completed Foundation 0.2 architecture.

All cleanup work must remain:

- dependency-checked
- tested
- reversible
- isolated into small checkpoints
- committed and pushed before proceeding to dependent work

---

# Foundation 0.2.1 Progress

## Cleanup Checkpoints A–C

✔ COMPLETE

Initial cleanup work established the controlled legacy-removal
process and removed confirmed obsolete or accidentally tracked
material.

Completed work includes:

- legacy candidate inventory
- dependency classification
- removal of obsolete validator modules
- untracking of the accidental root virtual environment
- preservation of the local Python environment
- verification of Foundation regression gates after cleanup

Notable commits include:

8683131 Foundation 0.2.1 Checkpoint B: remove obsolete validator modules

76ae41c Foundation 0.2.1 Checkpoint C: untrack accidental root virtual environment

---

## Checkpoint D — Legacy rvdb/ Package Classification

Status:

IN PROGRESS

The historical inner `rvdb/` package is being classified component
by component.

Components are classified as:

- RETAIN
- MIGRATE
- RETIRE

No wholesale deletion of the inner `rvdb/` package is permitted
until useful functionality has been migrated and active dependencies
have been eliminated.

---

## Checkpoint D1 — Restore Hidden Build Source

✔ COMPLETE

The cleanup audit discovered that the active Foundation bundle
builder existed locally under the top-level `build/` directory but
was being hidden from Git by an obsolete `.gitignore` rule.

A fresh clone therefore would not have contained the active
Foundation builder.

Implemented:

- removed obsolete `build/` ignore rule
- restored `build/builder.py` to Git tracking
- created explicit `build/__init__.py`
- restored hidden `rvdb/build/checksum.py`
- verified Foundation build package imports
- verified fresh repository source visibility

Commit:

328e004 Foundation 0.2.1 Checkpoint D1: restore hidden build source

---

## Checkpoint D2 — Foundation Checksum Migration

✔ COMPLETE

Migrated generic SHA-256 artifact checksum functionality from the
legacy build subsystem into the active Foundation build package.

Implemented:

- `build/checksum.py`
- streaming SHA-256 calculation
- checksum manifest generation
- canonical default output path
- CWD-independent behavior
- missing-file handling
- Foundation public API integration
- checksum regression tests

Commit:

9c2152e Foundation 0.2.1 Checkpoint D2: migrate checksum builder

Regression suite after D2:

94 passed

---

## Checkpoint D3 — Foundation CSV Export Migration

✔ COMPLETE

Migrated CSV export functionality away from the legacy hardcoded
Game object model.

Implemented:

- generic Foundation entity CSV exporter
- support for Foundation Entity objects
- support for plain entity mappings
- dotted nested-field paths
- deterministic JSON serialization of relationship lists and maps
- configurable CSV columns
- CWD-independent output
- Foundation game export coverage

Commit:

8aff719 Foundation 0.2.1 Checkpoint D3: migrate CSV exporter

Regression suite after D3:

100 passed

---

## Checkpoint D4 — Legacy Build Output Assessment

✔ COMPLETE

The remaining legacy build-output components were audited before
removal or migration.

Classification:

### Legacy JSON Exporter

RETIRE

Reason:

The canonical Foundation `rvdb.bundle.json` supersedes the historical
generic JSON export.

### Legacy Search Indexer

RETIRE FOR FOUNDATION 0.2.1

Reason:

The implementation is coupled to the historical Game object model
and duplicates functionality available through the active Foundation
query, relationship, alias, fuzzy-search, and graph architecture.

A serialized search index may be reconsidered later if dataset size
or performance requirements justify it.

### Legacy Manifest Builder

MIGRATE

Reason:

Release/build metadata remains useful, but the historical
implementation depends on the legacy registry, hardcodes an obsolete
version, and references obsolete build artifacts.

---

## Checkpoint D5 — Foundation Manifest Migration

✔ COMPLETE

Migrated manifest generation into the active Foundation build
architecture.

Implemented:

- `build/manifest.py`
- Foundation version metadata
- UTC generation timestamps
- entity statistics derived from the active RVGraph
- entity counts grouped by type
- explicit artifact inventory
- portable project-relative artifact paths
- protection against machine-specific absolute paths
- version override support
- Foundation public API integration
- manifest regression tests

Foundation 0.2.1 manifest version:

0.2.1

Current production entity count:

19

Current entity counts by type:

- core: 2
- developer: 2
- game: 4
- genre: 3
- manufacturer: 3
- platform: 4
- publisher: 1

Regression suite after D5:

107 passed

Production validation:

19 entities checked

19 valid

0 schema errors

0 relationship errors

Canonical graph:

19 nodes

19 edge entries

Checkpoint commit:

Foundation 0.2.1 Checkpoint D5: migrate manifest builder

---

# Foundation 0.2.1 Checkpoint D6 — Legacy Runtime Retirement

✔ COMPLETE THROUGH D6-C4C

Checkpoint D6 completed the controlled retirement of the historical
inner `rvdb/` runtime after useful functionality was migrated or
confirmed superseded by the active Foundation architecture.

The retirement was performed incrementally through dependency-audited,
tested checkpoints rather than as a wholesale deletion.

Completed D6 work includes:

- retirement of superseded legacy build-output modules
- retirement of the historical search-index implementation
- retirement of superseded legacy query functionality
- retirement of the remaining historical entity object model
- retirement of the legacy loader
- retirement of the legacy registry
- retirement of the legacy linker
- retirement of the legacy relationship implementation
- retirement of the legacy resolver
- verification that no active Foundation imports depend on the retired
  runtime

The active Foundation runtime is now authoritative.

Active runtime components include:

- cli.py
- engine/loader.py
- engine/graph.py
- engine/query.py
- engine/resolver.py
- engine/context.py
- services/registry.py
- validator/schema.py
- validator/relationships.py
- build/builder.py
- build/checksum.py
- build/csv_exporter.py
- build/manifest.py

D6-C4C verification baseline:

- active Foundation compilation: PASS
- CLI help: PASS
- query smoke test: PASS
- search smoke test: PASS
- show smoke test: PASS
- related smoke test: PASS
- automated regression suite: 107 passed
- production entities checked: 19
- production entities valid: 19
- schema errors: 0
- relationship errors: 0
- canonical graph nodes: 19
- canonical graph edge entries: 19
- canonical bundle build: PASS
- `git diff --check`: PASS

The historical inner `rvdb/` Python runtime has therefore completed
its controlled retirement from the Foundation architecture.

Historical `dist/` output files remain non-canonical artifacts and
must continue to be handled separately from the tracked canonical
`rvdb.bundle.json`.

---

# Current Foundation 0.2.1 State

Foundation architecture:

STABLE

Legacy runtime retirement:

COMPLETE

Automated tests:

107 passing

Production entities:

19

Production validation:

PASS

Canonical bundle build:

PASS

The active Foundation implementation is the runtime source of truth.

---

# CURRENT FOUNDATION 0.2.1 RELEASE-HARDENING STATE

## Post-D6 Cleanup and Reproducibility

Status:

COMPLETE

Completed work includes:

- retired obsolete historical tests
- retired obsolete ID migration scaffolding
- retired historical Phase-D scaffolding
- corrected the canonical runtime version to 0.2.1
- retired empty root skeleton files
- normalized the `services` package
- defined the runtime dependency contract as `PyYAML>=6.0`
- fast-forwarded `develop` to the completed Foundation branch
- verified a true clean clone from the default GitHub branch
- verified isolated `.venv` creation from a clean clone
- verified runtime installation from `requirements.txt`
- verified pytest remains a development-only dependency
- added and verified the canonical project README

Verified Foundation baseline:

- RVDB version: 0.2.1
- production entities: 19
- valid entities: 19
- schema errors: 0
- relationship errors: 0
- graph nodes: 19
- graph edge entries: 19
- automated regression tests: 110 passing
- canonical branch: `develop`
- clean-clone reproducibility: PASS

## Foundation 0.2.1 Release Closure

Status:

RELEASE READY

Completed release-hardening decisions and gates:

- conventional installed-package metadata is deferred beyond Foundation 0.2.1
- Foundation 0.2.1 ships without an explicit open-source license
- final compile gate: PASS
- final regression suite: 110 passing
- final production validation: 19 valid / 0 schema errors / 0 relationship errors
- final canonical build: 19 nodes / 19 edge entries
- final build cleanliness: PASS
- canonical branch: `develop`
- local/remote synchronization: PASS

Remaining release operation:

- create and push the `foundation-0.2.1` release tag

Architectural feature work and large-scale data expansion remain deferred
until the Foundation 0.2.1 release-hardening sequence is complete.

Safety, reproducibility, and independently verified checkpoints continue
to take priority over minimizing checkpoint count.

---

# End-of-Session Rules

These steps are MANDATORY before intentionally ending an RVDB
development session.

1. Finish the current atomic checkpoint whenever practical.
2. Run the complete relevant test suite.
3. Run production database validation.
4. Run the canonical build when build-related code has changed.
5. Run `git diff --check`.
6. Review `git status`.
7. Review the exact staged files.
8. Commit every completed and verified checkpoint.
9. Push completed checkpoint commits to GitHub.
10. Create and push safety tags at major architectural boundaries
    when appropriate.
11. Update `docs/current_milestone.md` with all work completed during
    the session.
12. Record the exact NEXT checkpoint in
    `docs/current_milestone.md`.
13. Record the current regression-test count and production
    validation/build state.
14. Commit the milestone-document update separately.
15. Push the milestone-document commit to GitHub.
16. Verify the local branch is synchronized with the remote.
17. Leave the working tree clean whenever possible.
18. Verify the final HEAD commit before ending the session.

IMPORTANT:

The milestone documentation update is the FINAL CHECKPOINT of every
development session.

A session must not intentionally be considered wrapped up until the
completed work has been committed, pushed, the milestone document
has been updated and pushed, and the repository state has been
verified clean.

Temporary test entities must not be committed.

Generated test artifacts must not replace canonical production data.

Large cleanup operations must remain separate from architectural
feature work.

Do not delete a legacy component merely because it appears obsolete.

Every cleanup candidate must first be dependency-checked and tested.

---

# Resume Instructions

To continue development in a future ChatGPT session, use:

Continue RVDB Project.

Read docs/current_milestone.md and continue from the current milestone.

Expected restart point:

Foundation 0.2.1 — Release Tag

Status:

NEXT

Foundation 0.2.1 implementation, cleanup, documentation, release metadata
decisions, clean-clone reproducibility verification, and final release
gates are complete.

The next operation is to create and push the `foundation-0.2.1` tag from
the finalized `develop` HEAD.

---

# End of Current Milestone
