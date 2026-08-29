# RVDB Current Milestone

_Last Updated: 2026-08-26_

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

RELEASED

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

Release operation completed:

- `foundation-0.2.1` annotated release tag created and pushed
- release tag points to the finalized Foundation 0.2.1 release commit

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

Phase 2A — Post-P2A1 Platform Catalog Planning

Status:

NEXT

Foundation 0.2.1 is complete, released, tagged, pushed, tested, validated,
and reproducible from a clean clone.

Phase 2A is active.

P2A0 platform architecture and schema-capability audits are complete.

P2A1 Platform Entity Contract v2 is complete, implemented, tested,
validated, and build-verified.

Continue by selecting the next controlled Phase 2A platform-catalog
expansion checkpoint before beginning large-scale platform YAML creation.

---

# Phase 2A — Platform Database Expansion

Status:

IN PROGRESS

Foundation prerequisite:

- Foundation 0.2.1 released
- release tag: `foundation-0.2.1`
- canonical branch: `develop`
- Foundation regression baseline: 110 tests passing
- Foundation validation baseline: 19 valid entities
- schema errors: 0
- relationship errors: 0

## P2A0 — Platform Architecture Audit

Status:

COMPLETE

Completed:

- audited current production platform dataset
- confirmed 4 existing platform entities
- audited platform schema and entity template
- audited common entity schema
- audited schema loader
- audited schema validator
- audited entity builder field handling
- audited relationship schema capabilities
- confirmed supported ordinary schema field types:
  - `string`
  - `integer`
  - `integer_or_null`
  - `boolean`
  - `list`
  - `object`
  - `entity_reference`
  - `entity_reference_list`
- confirmed relationship schema types:
  - `entity_reference`
  - `entity_reference_list`
- confirmed schema-defined relationship target typing
- confirmed current platform schema is intentionally minimal
- confirmed current platform contract is insufficient for the planned
  complete structured platform catalog
- confirmed Foundation regression baseline remains green

Decision:

Expand and formalize the platform entity contract before beginning
large-scale platform data population.

## P2A1 — Platform Entity Contract v2

Status:

COMPLETE

Goal:

Define and implement the canonical RVDB platform metadata contract required
for controlled large-scale platform database expansion.

Completed:

- defined the canonical Platform Entity Contract v2
- classified required and optional platform fields
- made `category` a required platform field
- established controlled category values:
  - `console`
  - `handheld`
  - `computer`
  - `arcade`
- added optional `family`
- added typed `regions`
- added typed `media`
- added typed `extensions`
- added typed `architecture`
- preserved manufacturer reference semantics
- preserved nullable release-year semantics
- preserved nullable generation semantics
- preserved `supports_core` relationship semantics
- added generic reusable schema constraint support
- added schema-definition validation for constraints
- added builder-side constrained-list enforcement
- updated the Platform Entity Template v2
- added Platform Contract v2 regression coverage
- updated existing builder regression fixtures for the new contract
- audited all four Foundation platform entities against Platform v2
- confirmed no forced production YAML migration edits were required
- preserved existing justified NES media and extension data
- preserved all existing platform relationships
- preserved Arcade transitional legacy-manufacturer metadata

Verification:

- regression suite: 144 passed
- production entities checked: 19
- production entities valid: 19
- schema errors: 0
- relationship errors: 0
- canonical graph nodes: 19
- canonical graph edges: 19
- canonical bundle: `rvdb.bundle.json`
- canonical bundle build: PASS
- branch: `develop`

Implementation commits:

- `98609ed` — `feat: add generic schema constraints`
- `eb18ca7` — `feat: implement Platform Entity Contract v2`

Decision:

P2A1 is complete.

Large-scale platform data population may now proceed only through controlled
Phase 2A checkpoints using the finalized Platform Entity Contract v2.

Expected restart point:

Phase 2A — Post-P2A1 Platform Catalog Planning

---

# End of Current Milestone

---

# Phase 2A — Platform Catalog Expansion Progress

## P2A10 — Atari 8-bit Computer Platform Population Batch 9

Status:

COMPLETE

Planning commit:

`ac41acb` — `docs: plan Atari 8-bit computer platform batch 9`

Production commit:

`1e2952e` — `data: add Atari 8-bit computer platform batch 9`

Production entity added:

- `platform.atari.8.bit.computers`

Canonical production path:

- `data/platforms/atari/8_bit_computers.yaml`

Atari Platform Batch 9 expanded the controlled Atari production catalog
with one canonical computer platform representing the Atari 8-bit computer
family.

The batch completed the controlled Phase 2A population sequence:

1. Batch 9 candidate audit
2. Atari 8-bit computer family selection
3. canonical entity-boundary review
4. manufacturer verification
5. canonical ID and filesystem-path decision
6. canonical name review
7. release-year decision
8. computer-category decision
9. media decision
10. conservative software-image extension selection
11. XEGS entity-boundary review
12. Atari 5200 / `a52` boundary verification
13. optional metadata deferral
14. explicit Batch 9 planning
15. plan-only commit and push
16. production YAML creation
17. Platform Entity Contract v2 verification
18. dataset-count baseline synchronization
19. targeted regression verification
20. complete regression verification
21. production validation
22. canonical bundle verification
23. exact production working-set review
24. production commit and push
25. final local/remote synchronization verification

The production record uses only vocabulary already supported by
Platform Entity Contract v2.

No schema expansion was required.

Atari 8-bit Computers uses:

- canonical ID: `platform.atari.8.bit.computers`
- manufacturer: `manufacturer.atari`
- release year: `1979`
- category: `computer`
- media:
  - `cartridge`
  - `floppy`
  - `cassette`
- extensions:
  - `atr`
  - `xfd`
  - `atx`
  - `cas`

No emulator-core relationships were invented.

The production record intentionally retains an empty `supports_core`
relationship list pending separately researched canonical core entities
and relationship work.

The following Atari boundaries were explicitly reviewed during Batch 9:

- Atari 8-bit Computers — production entity added
- Atari 5200 — existing production entity preserved separately
- Atari XEGS / XE Game System — separate entity boundary remains deferred

No separate XEGS or XE Game System production entity was introduced.

The `a52` extension remains exclusive to Atari 5200 and was verified absent
from the Atari 8-bit Computers record.

Optional Platform v2 metadata remains deferred where not yet normalized:

- `family`
- `generation`
- `regions`
- `architecture`

---

# Current Phase 2A Verification Baseline

Branch:

`develop`

Production entities:

38

Platform entities:

23

Production validation:

- entities checked: 39
- valid: 39
- schema errors: 0
- relationship errors: 0

Regression suite:

145 passing

Canonical graph:

- nodes: 38
- edges: 38

Canonical bundle:

`rvdb.bundle.json`

Canonical bundle build:

PASS

Working tree after Atari 8-bit Batch 9 production commit:

CLEAN

Local/remote synchronization:

PASS

Production commit:

`1e2952e` — `data: add Atari 8-bit computer platform batch 9`

---

# Current Platform Catalog

Production platforms:

- `platform.arcade`
- `platform.atari.2600`
- `platform.atari.5200`
- `platform.atari.7800`
- `platform.atari.8.bit.computers`
- `platform.atari.jaguar`
- `platform.atari.lynx`
- `platform.atari.st`
- `platform.nintendo.3ds`
- `platform.nintendo.ds`
- `platform.nintendo.game.boy`
- `platform.nintendo.game.boy.advance`
- `platform.nintendo.game.boy.color`
- `platform.nintendo.gamecube`
- `platform.nintendo.n64`
- `platform.nintendo.nes`
- `platform.nintendo.snes`
- `platform.nintendo.wii`
- `platform.nintendo.wii.u`
- `platform.sega.dreamcast`
- `platform.sega.game.gear`
- `platform.sega.genesis`
- `platform.sega.saturn`

Platform count:

23

---

# Phase 2A Deferred Decisions

The following work remains intentionally deferred.

## Atari XEGS / XE Game System

Do not create a production XEGS entity until RVDB explicitly decides the
canonical entity boundary for the Atari XE Game System relative to the
broader Atari 8-bit computer family.

Do not automatically:

- create `platform.atari.xegs`
- create `platform.atari.xe.game.system`
- create separate XEGS production YAML
- duplicate Atari 8-bit computer metadata into an XEGS record

The Batch 9 production review confirmed that no separate XEGS or XE Game
System entity currently exists.

## Atari Jaguar CD

Do not create a production Jaguar CD entity until RVDB explicitly decides
the canonical entity boundary between the base Atari Jaguar platform and
the Jaguar CD attachment.

Do not automatically:

- create `platform.atari.jaguar.cd`
- create `data/platforms/atari/jaguar_cd.yaml`
- add `optical-disc` to the base Atari Jaguar solely because of Jaguar CD
- add Jaguar CD software-image extensions to the base Atari Jaguar

Jaguar CD may ultimately require a separate platform, add-on, accessory,
hardware relationship, or another future normalized representation.

## Atari ST Family

The following related machines remain outside the completed Atari ST
Batch 8 and require separate canonical entity-boundary review:

- Atari STE
- Atari TT
- Atari Falcon

Do not automatically create:

- `platform.atari.ste`
- `platform.atari.tt`
- `platform.atari.falcon`

Do not merge their machine-specific capabilities into the canonical Atari ST
production record without separate research and modeling.

## Nintendo DSi

Do not create a production DSi entity until RVDB explicitly decides whether
Nintendo DSi is:

- a separate canonical platform
- a DS-family platform variant
- or represented through a future normalized family model

Hardware capability differences and DSiWare support require deliberate
boundary review.

## Sega Master System / Mark III

Do not create production YAML until RVDB explicitly decides the canonical
entity boundary between:

- Sega Mark III
- overseas Master System
- Japanese Master System

## Optional Platform Metadata

Continue deferring unsupported or insufficiently normalized values for:

- `family`
- `generation`
- `regions`
- `architecture`

## Emulator-Core Relationships

Do not invent `supports_core` relationships.

Populate them only after the required canonical core entities exist and the
relationships are researched separately.

## Additional Atari Families

The following Atari platform families remain outside the completed Atari
production batches and require their own controlled planning:

- Atari modern VCS
- Atari arcade hardware families

Atari Jaguar CD remains separately deferred because its entity boundary
requires an explicit modeling decision.

Atari STE, Atari TT, and Atari Falcon remain separately deferred because
their boundaries relative to Atari ST require explicit canonical review.

Atari XEGS / XE Game System remains separately deferred because its boundary
relative to the Atari 8-bit computer family requires explicit canonical
review.

## Nintendo Hardware Revisions

Do not automatically create separate platform entities for:

- Game Boy Advance SP
- Game Boy micro
- Nintendo DS Lite
- Nintendo DSi XL
- Nintendo 2DS
- New Nintendo 3DS
- New Nintendo 3DS XL
- New Nintendo 2DS XL
- Wii RVL-001
- Wii RVL-101
- Wii mini / RVL-201

Hardware revision alone is not sufficient to establish a new canonical
RVDB platform entity.

---

# NEXT CHECKPOINT

## P2A11 — Select and Research Platform Population Batch 10

Status:

NEXT

Goal:

Select the next small, controlled platform population batch before creating
additional production YAML.

Required work:

1. audit remaining manufacturer/platform candidates
2. select a coherent Batch 10 scope
3. verify manufacturer coverage
4. determine canonical entity boundaries
5. determine canonical IDs and filesystem paths
6. research canonical names and justified aliases
7. research release years
8. determine valid platform categories
9. determine controlled media values
10. determine defensible software-image extensions
11. identify any boundary decisions requiring explicit deferral
12. explicitly defer unsupported metadata
13. write and review the Batch 10 plan
14. commit the plan separately before production creation

Candidate directions may include:

- Atari XEGS / XE Game System after explicit boundary review
- additional Atari families after explicit canonical review
- additional Nintendo platforms after explicit entity-boundary review
- Sega Master System only after explicit entity-boundary review
- another manufacturer after creating or verifying its canonical
  manufacturer entity

Population must continue to follow:

- `docs/platform_contract.md`
- `docs/platform_catalog_policy.md`

No Batch 10 production YAML should be created until the Batch 10 planning
checkpoint is complete.

Expected restart point:

P2A11 — Select and Research Platform Population Batch 10


# NEXT CHECKPOINT

## P2A21 — Select and Research Platform Population Batch 12

Status:

COMPLETE

---

# Batch 12 Completion Baseline

The Sega SC-3000 Batch 12 population was completed and committed.

Planning commit:

`2268c70` — `docs: add P2A21 Sega SC-3000 plan`

Production commit:

`71317c1` — `data: add Sega SC-3000 platform batch 12`

Canonical entity:

`platform.sega.sc3000`

Canonical name:

`Sega SC-3000`

Production record:

`data/platforms/sega/sc3000.yaml`

Batch 12 decisions:

- SC-3000 is a distinct canonical platform.
- SC-3000H remains within the SC-3000 platform boundary.
- SG-1000 remains a separate canonical platform.
- category: `computer`
- release year: `1983`
- media: `cartridge`, `cassette`
- extensions: `sc`, `sg`, `bit`
- `supports_core` remains empty.
- unsupported metadata remains omitted.

Verified production baseline:

- entities: 41
- platforms: 26
- graph nodes: 41
- graph edges: 41
- regression tests: 145 passing
- validation: 41 valid
- schema errors: 0
- relationship errors: 0

Batch 12 production and regression verification completed successfully.

---

# Batch 11 Completion Baseline

The Sega SG-1000 Batch 11 population was completed and committed.

Commit:

`499850a` — `data: add Sega SG-1000 platform batch 11`

Canonical entity:

`platform.sega.sg1000`

Canonical name:

`Sega SG-1000`

Production baseline:

- entities: 40
- platforms: 25
- graph nodes: 40
- graph edges: 40
- regression tests: 145 passing
- validation: 40 valid
- schema errors: 0
- relationship errors: 0

The Batch 11 production record is:

`data/platforms/sega/sg1000.yaml`

The canonical bundle is:

`rvdb.bundle.json`

Batch 11 is complete.

---

# Current Objective

Select and research the next small, controlled platform population batch
after completion of Sega SG-1000 Batch 11.

Current candidate direction:

- Sega SC-3000 after explicit canonical entity-boundary review

Additional candidate directions may be considered only after auditing the
remaining platform catalog and existing manufacturer coverage.

---

# Required Work

1. audit remaining manufacturer/platform candidates
2. select a coherent Batch 12 scope
3. verify manufacturer coverage
4. determine canonical entity boundaries
5. determine canonical IDs and filesystem paths
6. research canonical names and justified aliases
7. research release years
8. determine valid platform categories
9. determine controlled media values
10. determine defensible software-image extensions
11. identify any boundary decisions requiring explicit deferral
12. explicitly defer unsupported metadata
13. write and review the Batch 12 planning document
14. commit the planning document before production creation

No Batch 12 production YAML should be created until the Batch 12 planning
checkpoint is complete.


## P2A2 — Controlled Platform Catalog Foundation

Status:

COMPLETE THROUGH NINTENDO PLATFORM BATCH 1

P2A2 established the policy, naming, schema-vocabulary, and controlled
population process required for safe platform catalog expansion.

Completed work includes:

- finalized the canonical Platform Entity Contract v2 documentation
- defined the canonical platform catalog policy
- established manufacturer-specific platform paths:
  `data/platforms/<manufacturer>/<system>.yaml`
- normalized Sega Genesis to:
  `data/platforms/sega/genesis.yaml`
- defined multi-word platform ID and filename policy
- established canonical multi-segment IDs such as:
  `platform.nintendo.game.boy`
- established deterministic filenames such as:
  `data/platforms/nintendo/game_boy.yaml`
- planned Nintendo Platform Batch 1
- defined and implemented the controlled Platform v2 media vocabulary
- aligned the Platform Contract and Nintendo batch documentation with the
  controlled media vocabulary
- created and verified Nintendo Platform Batch 1
- updated dataset-dependent regression baselines
- regenerated and verified the canonical bundle

Controlled Platform v2 media vocabulary:

- `cartridge`
- `floppy`
- `optical-disc`
- `cassette`
- `digital`

Relevant Phase 2A commits:

- `98609ed` — `feat: add generic schema constraints`
- `eb18ca7` — `feat: implement Platform Entity Contract v2`
- `eacbd10` — `docs: finalize Platform Entity Contract v2`
- `5106513` — `docs: define canonical platform catalog policy`
- `efd8909` — `data: normalize Sega Genesis platform path`
- `bef088c` — `docs: define multi-word platform naming policy`
- `03ad37d` — `docs: plan Nintendo platform batch 1`
- `4519892` — `feat: define platform media vocabulary`
- `f515fe0` — `data: add Nintendo platform batch 1`

---

## Nintendo Platform Batch 1

Status:

COMPLETE

Production entities added:

- `platform.nintendo.n64`
- `platform.nintendo.game.boy`
- `platform.nintendo.game.boy.color`

Canonical production paths:

- `data/platforms/nintendo/n64.yaml`
- `data/platforms/nintendo/game_boy.yaml`
- `data/platforms/nintendo/game_boy_color.yaml`

The production platform catalog now contains seven platform entities:

- `platform.arcade`
- `platform.nintendo.game.boy`
- `platform.nintendo.game.boy.color`
- `platform.nintendo.n64`
- `platform.nintendo.nes`
- `platform.nintendo.snes`
- `platform.sega.genesis`

Nintendo Batch 1 deliberately omitted unsupported or insufficiently
researched optional metadata.

Deferred fields include:

- `family`
- `generation`
- `regions`
- `architecture`

No unsupported `supports_core` relationships were introduced.

---

# Current Phase 2A Verification Baseline

Branch:

`develop`

Production entities:

22

Platform entities:

7

Production validation:

- entities checked: 22
- valid entities: 22
- schema errors: 0
- relationship errors: 0

Automated regression suite:

145 passing

Canonical graph:

- nodes: 22
- edges: 22

Canonical bundle:

`rvdb.bundle.json`

Canonical bundle build:

PASS

Nintendo Batch 1 commit:

`f515fe0` — `data: add Nintendo platform batch 1`

---

# Current Phase 2A Decision

The Platform Entity Contract v2 and controlled catalog-population process
have now been exercised successfully against the first new production
platform batch.

Nintendo Platform Batch 1 is complete.

Do not begin uncontrolled or large-scale platform population.

Continue using small, researched, explicitly planned platform batches.

---

# NEXT CHECKPOINT

## P2A3 — Select and Research Platform Population Batch 2

Status:

NEXT

Goal:

Select the next small, controlled platform population batch and research
its canonical identities and defensible metadata before creating production
YAML.

The next batch must be planned before production entities are created.

Required planning work:

1. select the manufacturer or coherent platform family for Batch 2
2. define the exact platform scope
3. verify required manufacturer entities already exist
4. determine canonical platform IDs
5. determine canonical filesystem paths
6. research canonical names and justified aliases
7. research release years
8. determine required platform categories
9. determine controlled media values
10. research defensible software-image extensions
11. identify optional fields that have sufficient evidence
12. explicitly defer unsupported or speculative metadata
13. document the proposed batch before production YAML creation

Population must continue to follow:

- `docs/platform_contract.md`
- `docs/platform_catalog_policy.md`

No Batch 2 production YAML should be created until its planning checkpoint
has been reviewed and accepted.

Expected restart point:

P2A3 — Select and Research Platform Population Batch 2

---

# Phase 2A — Sega Platform Batch 2 Completion

## P2A3 — Sega Platform Population Batch 2

Status:

COMPLETE

Planning commit:

`8dac84d` — `docs: plan Sega platform batch 2`

Production commit:

`70cf931` — `data: add Sega platform batch 2`

Production entities added:

- `platform.sega.game.gear`
- `platform.sega.saturn`
- `platform.sega.dreamcast`

Canonical production paths:

- `data/platforms/sega/game_gear.yaml`
- `data/platforms/sega/saturn.yaml`
- `data/platforms/sega/dreamcast.yaml`

Existing Sega platform preserved:

- `platform.sega.genesis`

Master System / Mark III remains intentionally deferred pending a separate
entity-boundary review.

Sega Batch 2 completed the following controlled process:

1. candidate manufacturer audit
2. Sega batch selection
3. metadata research
4. explicit batch planning
5. plan-only commit and push
6. production YAML creation
7. Platform v2 contract verification
8. dataset-baseline updates
9. production validation
10. complete regression verification
11. canonical bundle regeneration
12. batch documentation alignment
13. production commit and push

---

# Current Phase 2A Verification Baseline

Branch:

`develop`

Production entities:

25

Platform entities:

10

Production validation:

- entities checked: 25
- valid entities: 25
- schema errors: 0
- relationship errors: 0

Automated regression suite:

145 passing

Canonical graph:

- nodes: 25
- edges: 25

Canonical bundle:

`rvdb.bundle.json`

Canonical bundle build:

PASS

Working tree after Sega Batch 2 production commit:

CLEAN

Local/remote synchronization:

PASS

---

# Current Platform Catalog

Production platforms:

- `platform.arcade`
- `platform.nintendo.game.boy`
- `platform.nintendo.game.boy.color`
- `platform.nintendo.n64`
- `platform.nintendo.nes`
- `platform.nintendo.snes`
- `platform.sega.dreamcast`
- `platform.sega.game.gear`
- `platform.sega.genesis`
- `platform.sega.saturn`

Platform count:

10

---

# Phase 2A Deferred Decisions

The following work remains intentionally deferred:

## Sega Master System / Mark III

Do not create production YAML until RVDB explicitly decides the canonical
entity boundary between:

- Sega Mark III
- overseas Master System
- Japanese Master System

## Optional Platform Metadata

Continue deferring unsupported or insufficiently normalized values for:

- `family`
- `generation`
- `regions`
- `architecture`

## Emulator-Core Relationships

Do not invent `supports_core` relationships.

Populate them only after the required canonical core entities exist and the
relationships are researched separately.

---

# NEXT CHECKPOINT

## P2A4 — Select and Research Platform Population Batch 3

Status:

NEXT

Goal:

Select the next small, controlled platform population batch before creating
additional production YAML.

Required work:

1. audit remaining manufacturer/platform candidates
2. select a coherent Batch 3 scope
3. verify manufacturer coverage
4. determine canonical entity boundaries
5. determine IDs and canonical paths
6. research names and aliases
7. research release years
8. determine categories
9. determine controlled media values
10. determine defensible extensions
11. explicitly defer unsupported metadata
12. write and review the Batch 3 plan
13. commit the plan separately before production creation

Candidate directions may include:

- Atari
- additional Nintendo systems
- additional Sega systems after explicit boundary review
- another manufacturer only after creating or verifying its canonical
  manufacturer entity

Population must continue to follow:

- `docs/platform_contract.md`
- `docs/platform_catalog_policy.md`

No Batch 3 production YAML should be created until the Batch 3 planning
checkpoint is complete.

Expected restart point:

P2A4 — Select and Research Platform Population Batch 3

---

# Phase 2A — Atari Platform Batch 3 Completion

## P2A4 — Atari Platform Population Batch 3

Status:

COMPLETE

Planning commit:

`44420ec` — `docs: plan Atari platform batch 3`

Production commit:

`8fdb6ab` — `data: add Atari platform batch 3`

Production entities added:

- `platform.atari.2600`
- `platform.atari.5200`
- `platform.atari.7800`

Canonical production paths:

- `data/platforms/atari/2600.yaml`
- `data/platforms/atari/5200.yaml`
- `data/platforms/atari/7800.yaml`

Atari Batch 3 established Atari's first production platform coverage in
RVDB.

The batch completed the following controlled process:

1. Batch 3 manufacturer/platform candidate audit
2. Atari batch selection
3. three-platform scope definition
4. metadata research
5. explicit plan document creation
6. plan-only commit and push
7. production YAML creation
8. Platform v2 contract verification
9. dataset-count baseline updates
10. production validation
11. complete regression verification
12. canonical bundle regeneration
13. batch documentation alignment
14. production commit and push

---

# Current Phase 2A Verification Baseline

Branch:

`develop`

Production entities:

28

Platform entities:

13

Production validation:

- entities checked: 28
- valid entities: 28
- schema errors: 0
- relationship errors: 0

Automated regression suite:

145 passing

Canonical graph:

- nodes: 28
- edges: 28

Canonical bundle:

`rvdb.bundle.json`

Canonical bundle build:

PASS

Working tree after Atari Batch 3 production commit:

CLEAN

Local/remote synchronization:

PASS

---

# Current Platform Catalog

Production platforms:

- `platform.arcade`
- `platform.atari.2600`
- `platform.atari.5200`
- `platform.atari.7800`
- `platform.nintendo.game.boy`
- `platform.nintendo.game.boy.color`
- `platform.nintendo.n64`
- `platform.nintendo.nes`
- `platform.nintendo.snes`
- `platform.sega.dreamcast`
- `platform.sega.game.gear`
- `platform.sega.genesis`
- `platform.sega.saturn`

Platform count:

13

---

# Phase 2A Deferred Decisions

The following work remains intentionally deferred.

## Sega Master System / Mark III

Do not create production YAML until RVDB explicitly decides the canonical
entity boundary between:

- Sega Mark III
- overseas Master System
- Japanese Master System

## Optional Platform Metadata

Continue deferring unsupported or insufficiently normalized values for:

- `family`
- `generation`
- `regions`
- `architecture`

## Emulator-Core Relationships

Do not invent `supports_core` relationships.

Populate them only after the required canonical core entities exist and
the relationships are researched separately.

## Additional Atari Families

The following Atari platform families remain outside Batch 3 and require
their own controlled planning:

- Atari 8-bit computers
- Atari XEGS
- Atari Lynx
- Atari Jaguar
- Atari Jaguar CD
- Atari ST
- modern Atari VCS
- Atari arcade hardware families

---

# NEXT CHECKPOINT

## P2A5 — Select and Research Platform Population Batch 4

Status:

NEXT

Goal:

Select the next small, controlled platform population batch before creating
additional production YAML.

Required work:

1. audit remaining manufacturer/platform candidates
2. select a coherent Batch 4 scope
3. verify manufacturer coverage
4. determine canonical entity boundaries
5. determine canonical IDs and paths
6. research names and aliases
7. research release years
8. determine valid categories
9. determine controlled media values
10. determine defensible extensions
11. explicitly defer unsupported metadata
12. write and review the Batch 4 plan
13. commit the plan separately before production creation

Candidate directions may include:

- additional Nintendo platforms
- additional Atari platforms
- Sega Master System only after explicit entity-boundary review
- another manufacturer after creating or verifying its canonical
  manufacturer entity

Population must continue to follow:

- `docs/platform_contract.md`
- `docs/platform_catalog_policy.md`

No Batch 4 production YAML should be created until the Batch 4 planning
checkpoint is complete.

Expected restart point:

P2A5 — Select and Research Platform Population Batch 4

---

# Phase 2A — Nintendo Handheld Platform Batch 4 Completion

## P2A5 — Nintendo Handheld Platform Population Batch 4

Status:

COMPLETE

Planning commit:

`a75af50` — `docs: plan Nintendo handheld platform batch 4`

Production commit:

`fd0d0ae` — `data: add Nintendo handheld platform batch 4`

Production entities added:

- `platform.nintendo.game.boy.advance`
- `platform.nintendo.ds`
- `platform.nintendo.3ds`

Canonical production paths:

- `data/platforms/nintendo/game_boy_advance.yaml`
- `data/platforms/nintendo/ds.yaml`
- `data/platforms/nintendo/3ds.yaml`

Nintendo Handheld Batch 4 extends the existing Nintendo handheld lineage
beyond Game Boy and Game Boy Color.

The controlled production scope contains:

- Game Boy Advance
- Nintendo DS
- Nintendo 3DS

Nintendo DSi remains deliberately excluded pending a separate canonical
entity-boundary decision.

The batch completed the following controlled process:

1. Batch 4 candidate audit
2. Nintendo handheld batch selection
3. three-platform scope definition
4. canonical naming and path decisions
5. metadata research
6. Nintendo DSi boundary deferral
7. explicit plan document creation
8. plan-only commit and push
9. production YAML creation
10. Platform v2 contract verification
11. dataset-count baseline updates
12. production validation
13. complete regression verification
14. canonical bundle regeneration
15. batch documentation alignment
16. production commit and push

---

# Current Phase 2A Verification Baseline

Branch:

`develop`

Production entities:

31

Platform entities:

16

Production validation:

- entities checked: 31
- valid entities: 31
- schema errors: 0
- relationship errors: 0

Automated regression suite:

145 passing

Canonical graph:

- nodes: 31
- edges: 31

Canonical bundle:

`rvdb.bundle.json`

Canonical bundle build:

PASS

Working tree after Nintendo Handheld Batch 4 production commit:

CLEAN

Local/remote synchronization:

PASS

---

# Current Platform Catalog

Production platforms:

- `platform.arcade`
- `platform.atari.2600`
- `platform.atari.5200`
- `platform.atari.7800`
- `platform.nintendo.3ds`
- `platform.nintendo.ds`
- `platform.nintendo.game.boy`
- `platform.nintendo.game.boy.advance`
- `platform.nintendo.game.boy.color`
- `platform.nintendo.n64`
- `platform.nintendo.nes`
- `platform.nintendo.snes`
- `platform.sega.dreamcast`
- `platform.sega.game.gear`
- `platform.sega.genesis`
- `platform.sega.saturn`

Platform count:

16

---

# Phase 2A Deferred Decisions

The following work remains intentionally deferred.

## Nintendo DSi

Do not create a production DSi entity until RVDB explicitly decides whether
Nintendo DSi is:

- a separate canonical platform
- a DS-family platform variant
- or represented through a future normalized family model

Hardware capability differences and DSiWare support require deliberate
boundary review.

## Sega Master System / Mark III

Do not create production YAML until RVDB explicitly decides the canonical
entity boundary between:

- Sega Mark III
- overseas Master System
- Japanese Master System

## Optional Platform Metadata

Continue deferring unsupported or insufficiently normalized values for:

- `family`
- `generation`
- `regions`
- `architecture`

## Emulator-Core Relationships

Do not invent `supports_core` relationships.

Populate them only after the required canonical core entities exist and
the relationships are researched separately.

## Additional Atari Families

The following Atari platform families remain outside the completed Atari
Batch 3 and require their own controlled planning:

- Atari 8-bit computers
- Atari XEGS
- Atari Lynx
- Atari Jaguar
- Atari Jaguar CD
- Atari ST
- modern Atari VCS
- Atari arcade hardware families

## Nintendo Hardware Revisions

Do not automatically create separate platform entities for:

- Game Boy Advance SP
- Game Boy micro
- Nintendo DS Lite
- Nintendo DSi XL
- Nintendo 2DS
- New Nintendo 3DS
- New Nintendo 3DS XL
- New Nintendo 2DS XL

Hardware revision alone is not sufficient to establish a new canonical
RVDB platform entity.

---

# NEXT CHECKPOINT

## P2A6 — Select and Research Platform Population Batch 5

Status:

NEXT

Goal:

Select the next small, controlled platform population batch before creating
additional production YAML.

Required work:

1. audit remaining manufacturer/platform candidates
2. select a coherent Batch 5 scope
3. verify manufacturer coverage
4. determine canonical entity boundaries
5. determine canonical IDs and filesystem paths
6. research canonical names and justified aliases
7. research release years
8. determine valid platform categories
9. determine controlled media values
10. determine defensible software-image extensions
11. identify any boundary decisions requiring explicit deferral
12. explicitly defer unsupported metadata
13. write and review the Batch 5 plan
14. commit the plan separately before production creation

Candidate directions may include:

- additional Atari platforms
- additional Nintendo console platforms
- Sega Master System only after explicit entity-boundary review
- another manufacturer after creating or verifying its canonical
  manufacturer entity

Population must continue to follow:

- `docs/platform_contract.md`
- `docs/platform_catalog_policy.md`

No Batch 5 production YAML should be created until the Batch 5 planning
checkpoint is complete.

Expected restart point:

P2A6 — Select and Research Platform Population Batch 5

---

# Phase 2A — Nintendo Console Platform Batch 5 Completion

## P2A6 — Nintendo Console Platform Population Batch 5

Status:

COMPLETE

Planning commit:

`e66d1d6` — `docs: plan Nintendo console platform batch 5`

Production commit:

`3276395` — `data: add Nintendo console platform batch 5`

Documentation repair commit:

`a3dea82` — `docs: remove duplicate Nintendo batch 5 result`

Production entities added:

- `platform.nintendo.gamecube`
- `platform.nintendo.wii`

Canonical production paths:

- `data/platforms/nintendo/gamecube.yaml`
- `data/platforms/nintendo/wii.yaml`

Batch 5 extends Nintendo production coverage with two optical-disc home
console platforms:

- Nintendo GameCube
- Wii

The controlled production process completed:

1. Batch 5 candidate audit
2. Nintendo console batch selection
3. GameCube and Wii entity-boundary review
4. canonical ID and filesystem-path decisions
5. release-year and naming research
6. conservative optical-disc extension selection
7. Wii hardware-revision boundary review
8. Wii U explicit deferral
9. plan document creation
10. plan-only commit and push
11. production YAML creation
12. Platform v2 contract verification
13. dataset-count baseline updates
14. complete regression verification
15. production validation
16. canonical bundle regeneration
17. implementation-result documentation alignment
18. production commit and push
19. duplicate implementation-result cleanup

Wii U remains deliberately excluded from Batch 5 and should receive its own
controlled platform-population decision in a future batch.

Wii hardware models/revisions including RVL-001, RVL-101, and Wii mini
(RVL-201) remain represented by the canonical Wii platform rather than
separate RVDB platform entities.

Optional Platform v2 metadata remains deferred where not yet normalized:

- `family`
- `generation`
- `regions`
- `architecture`

The `supports_core` relationship remains empty pending separately researched
canonical core entities and relationship work.

---

# Current Phase 2A Verification Baseline

Branch:

`develop`

Production entities:

33

Platform entities:

18

Production validation:

- entities checked: 33
- valid entities: 33
- schema errors: 0
- relationship errors: 0

Automated regression suite:

145 passing

Canonical graph:

- nodes: 33
- edges: 33

Canonical bundle:

`rvdb.bundle.json`

Canonical bundle build:

PASS

Working tree after Nintendo Console Batch 5 production and documentation
repair commits:

CLEAN

Local/remote synchronization:

PASS

---

# Current Platform Catalog

Production platforms:

- `platform.arcade`
- `platform.atari.2600`
- `platform.atari.5200`
- `platform.atari.7800`
- `platform.nintendo.3ds`
- `platform.nintendo.ds`
- `platform.nintendo.game.boy`
- `platform.nintendo.game.boy.advance`
- `platform.nintendo.game.boy.color`
- `platform.nintendo.gamecube`
- `platform.nintendo.n64`
- `platform.nintendo.nes`
- `platform.nintendo.snes`
- `platform.nintendo.wii`
- `platform.sega.dreamcast`
- `platform.sega.game.gear`
- `platform.sega.genesis`
- `platform.sega.saturn`

Platform count:

18

---

# Phase 2A Deferred Decisions

The following work remains intentionally deferred.

## Nintendo DSi

Do not create a production DSi entity until RVDB explicitly decides whether
Nintendo DSi is:

- a separate canonical platform
- a DS-family platform variant
- or represented through a future normalized family model

Hardware capability differences and DSiWare support require deliberate
boundary review.

## Wii U

Wii U remains outside Batch 5 and should be handled as a separate canonical
platform in a future controlled batch.

## Sega Master System / Mark III

Do not create production YAML until RVDB explicitly decides the canonical
entity boundary between:

- Sega Mark III
- overseas Master System
- Japanese Master System

## Optional Platform Metadata

Continue deferring unsupported or insufficiently normalized values for:

- `family`
- `generation`
- `regions`
- `architecture`

## Emulator-Core Relationships

Do not invent `supports_core` relationships.

Populate them only after the required canonical core entities exist and
the relationships are researched separately.

## Additional Atari Families

The following Atari platform families remain outside the completed Atari
Batch 3 and require their own controlled planning:

- Atari 8-bit computers
- Atari XEGS
- Atari Lynx
- Atari Jaguar
- Atari Jaguar CD
- Atari ST
- modern Atari VCS
- Atari arcade hardware families

## Nintendo Hardware Revisions

Do not automatically create separate platform entities for:

- Game Boy Advance SP
- Game Boy micro
- Nintendo DS Lite
- Nintendo DSi XL
- Nintendo 2DS
- New Nintendo 3DS
- New Nintendo 3DS XL
- New Nintendo 2DS XL
- Wii RVL-001
- Wii RVL-101
- Wii mini / RVL-201

Hardware revision alone is not sufficient to establish a new canonical
RVDB platform entity.

---

# NEXT CHECKPOINT

## P2A7 — Select and Research Platform Population Batch 6

Status:

NEXT

Goal:

Select the next small, controlled platform population batch before creating
additional production YAML.

Required work:

1. audit remaining manufacturer/platform candidates
2. select a coherent Batch 6 scope
3. verify manufacturer coverage
4. determine canonical entity boundaries
5. determine canonical IDs and filesystem paths
6. research canonical names and justified aliases
7. research release years
8. determine valid platform categories
9. determine controlled media values
10. determine defensible software-image extensions
11. identify any boundary decisions requiring explicit deferral
12. explicitly defer unsupported metadata
13. write and review the Batch 6 plan
14. commit the plan separately before production creation

Candidate directions may include:

- additional Atari platforms
- Wii U as a separate Nintendo platform
- Sega Master System only after explicit entity-boundary review
- another manufacturer after creating or verifying its canonical
  manufacturer entity

Population must continue to follow:

- `docs/platform_contract.md`
- `docs/platform_catalog_policy.md`

No Batch 6 production YAML should be created until the Batch 6 planning
checkpoint is complete.

Expected restart point:

P2A7 — Select and Research Platform Population Batch 6

---

# Phase 2A — Nintendo Wii U Platform Batch 6 Completion

## P2A7 — Nintendo Wii U Platform Population Batch 6

Status:

COMPLETE

Planning commit:

`f1fb06a` — `docs: plan Nintendo Wii U platform batch 6`

Production commit:

`5019ed3` — `data: add Nintendo Wii U platform batch 6`

Production entity added:

- `platform.nintendo.wii.u`

Canonical production path:

- `data/platforms/nintendo/wii_u.yaml`

Nintendo Wii U Batch 6 establishes Wii U as a separate canonical RVDB
platform from Wii.

Canonical production identity:

- ID: `platform.nintendo.wii.u`
- name: `Wii U`
- manufacturer: `manufacturer.nintendo`
- release year: `2012`
- category: `console`
- media: `optical-disc`

Canonical extensions:

- `wud`
- `wux`
- `wua`

The `rpx` extension remains deliberately deferred.

Optional Platform v2 metadata remains deferred where not yet normalized:

- `family`
- `generation`
- `regions`
- `architecture`

The `supports_core` relationship remains empty pending separately researched
canonical core entities and relationship work.

The controlled production process completed:

1. Batch 6 candidate review
2. Wii U platform selection
3. canonical entity-boundary decision
4. canonical ID and filesystem-path decisions
5. release-year and naming research
6. conservative optical-disc extension selection
7. explicit `rpx` extension deferral
8. plan document creation
9. plan-only commit and push
10. production YAML creation
11. Platform v2 contract verification
12. dataset-count baseline updates
13. complete regression verification
14. production validation
15. canonical bundle regeneration
16. implementation-result documentation alignment
17. production commit and push

---

# Current Phase 2A Verification Baseline

Branch:

`develop`

Production entities:

34

Platform entities:

19

Production validation:

- entities checked: 34
- valid entities: 34
- schema errors: 0
- relationship errors: 0

Automated regression suite:

145 passing

Canonical graph:

- nodes: 34
- edges: 34

Canonical bundle:

`rvdb.bundle.json`

Canonical bundle build:

PASS

Working tree after Nintendo Wii U Batch 6 production commit:

CLEAN

Local/remote synchronization:

PASS

---

# Current Platform Catalog

Production platforms:

- `platform.arcade`
- `platform.atari.2600`
- `platform.atari.5200`
- `platform.atari.7800`
- `platform.nintendo.3ds`
- `platform.nintendo.ds`
- `platform.nintendo.game.boy`
- `platform.nintendo.game.boy.advance`
- `platform.nintendo.game.boy.color`
- `platform.nintendo.gamecube`
- `platform.nintendo.n64`
- `platform.nintendo.nes`
- `platform.nintendo.snes`
- `platform.nintendo.wii`
- `platform.nintendo.wii.u`
- `platform.sega.dreamcast`
- `platform.sega.game.gear`
- `platform.sega.genesis`
- `platform.sega.saturn`

Platform count:

19

---

# Phase 2A Deferred Decisions

The following work remains intentionally deferred.

## Nintendo DSi

Do not create a production DSi entity until RVDB explicitly decides whether
Nintendo DSi is:

- a separate canonical platform
- a DS-family platform variant
- or represented through a future normalized family model

Hardware capability differences and DSiWare support require deliberate
boundary review.

## Sega Master System / Mark III

Do not create production YAML until RVDB explicitly decides the canonical
entity boundary between:

- Sega Mark III
- overseas Master System
- Japanese Master System

## Optional Platform Metadata

Continue deferring unsupported or insufficiently normalized values for:

- `family`
- `generation`
- `regions`
- `architecture`

## Emulator-Core Relationships

Do not invent `supports_core` relationships.

Populate them only after the required canonical core entities exist and the
relationships are researched separately.

## Additional Atari Families

The following Atari platform families remain outside the completed Atari
Batch 3 and require their own controlled planning:

- Atari 8-bit computers
- Atari XEGS
- Atari Lynx
- Atari Jaguar
- Atari Jaguar CD
- Atari ST
- modern Atari VCS
- Atari arcade hardware families

## Nintendo Hardware Revisions

Do not automatically create separate platform entities for:

- Game Boy Advance SP
- Game Boy micro
- Nintendo DS Lite
- Nintendo DSi XL
- Nintendo 2DS
- New Nintendo 3DS
- New Nintendo 3DS XL
- New Nintendo 2DS XL
- Wii RVL-001
- Wii RVL-101
- Wii mini / RVL-201

Hardware revision alone is not sufficient to establish a new canonical
RVDB platform entity.

---

# NEXT CHECKPOINT

## P2A8 — Select and Research Platform Population Batch 7

Status:

NEXT

Goal:

Select the next small, controlled platform population batch before creating
additional production YAML.

Required work:

1. audit remaining manufacturer/platform candidates
2. select a coherent Batch 7 scope
3. verify manufacturer coverage
4. determine canonical entity boundaries
5. determine canonical IDs and filesystem paths
6. research canonical names and justified aliases
7. research release years
8. determine valid platform categories
9. determine controlled media values
10. determine defensible software-image extensions
11. identify any boundary decisions requiring explicit deferral
12. explicitly defer unsupported metadata
13. write and review the Batch 7 plan
14. commit the plan separately before production creation

Candidate directions may include:

- additional Atari platforms
- additional Nintendo platforms after explicit entity-boundary review
- Sega Master System only after explicit entity-boundary review
- another manufacturer after creating or verifying its canonical
  manufacturer entity

Population must continue to follow:

- `docs/platform_contract.md`
- `docs/platform_catalog_policy.md`

No Batch 7 production YAML should be created until the Batch 7 planning
checkpoint is complete.

Expected restart point:

P2A8 — Select and Research Platform Population Batch 7

---

# Phase 2A — Atari Platform Batch 7 Completion

## P2A8 — Atari Platform Population Batch 7

Status:

COMPLETE

Planning commit:

`89fddab` — `docs: plan Atari Lynx and Jaguar platform batch 7`

Production commit:

`f117bab` — `data: add Atari platform batch 7`

Production entities added:

- `platform.atari.lynx`
- `platform.atari.jaguar`

Production files added:

- `data/platforms/atari/lynx.yaml`
- `data/platforms/atari/jaguar.yaml`

Atari Platform Batch 7 expanded the existing Atari production catalog with
two additional canonical platforms:

- Atari Lynx
- Atari Jaguar

The batch completed the controlled Phase 2A population process:

1. remaining platform candidate audit
2. Atari Lynx and Jaguar batch selection
3. manufacturer verification
4. canonical entity-boundary review
5. canonical ID and filesystem-path decisions
6. canonical name and alias review
7. release-year research
8. category decisions
9. media decisions
10. conservative software-image extension decisions
11. Jaguar CD boundary deferral
12. optional metadata deferral
13. explicit plan creation and review
14. separate planning commit
15. production YAML creation
16. production validation
17. regression verification
18. canonical bundle rebuild
19. baseline-test synchronization
20. production commit and push

The production platform records use only vocabulary already supported by
Platform Entity Contract v2.

No schema expansion was required.

Atari Lynx uses:

- category: `handheld`
- media: `cartridge`
- extension: `lnx`

Atari Jaguar uses:

- category: `console`
- media: `cartridge`
- extensions:
  - `jag`
  - `j64`

No emulator-core relationships were invented.

Both records intentionally retain empty `supports_core` relationships.

Atari Jaguar CD was not created.

Its canonical entity boundary remains explicitly deferred.

---

# Current Phase 2A Verification Baseline

Branch:

`develop`

Production entities:

36

Platform entities:

21

Production validation:

- entities checked: 36
- valid: 36
- schema errors: 0
- relationship errors: 0

Regression suite:

145 passing

Canonical graph:

- nodes: 36
- edges: 36

Canonical bundle:

`rvdb.bundle.json`

Canonical bundle build:

PASS

Working tree after Atari Batch 7 production commit:

CLEAN

Local/remote synchronization:

PASS

---

# Current Platform Catalog

Production platforms:

- `platform.arcade`
- `platform.atari.2600`
- `platform.atari.5200`
- `platform.atari.7800`
- `platform.atari.jaguar`
- `platform.atari.lynx`
- `platform.nintendo.3ds`
- `platform.nintendo.ds`
- `platform.nintendo.game.boy`
- `platform.nintendo.game.boy.advance`
- `platform.nintendo.game.boy.color`
- `platform.nintendo.gamecube`
- `platform.nintendo.n64`
- `platform.nintendo.nes`
- `platform.nintendo.snes`
- `platform.nintendo.wii`
- `platform.nintendo.wii.u`
- `platform.sega.dreamcast`
- `platform.sega.game.gear`
- `platform.sega.genesis`
- `platform.sega.saturn`

Platform count:

21

---

# Phase 2A Deferred Decisions

The following work remains intentionally deferred.

## Atari Jaguar CD

Do not create a production Jaguar CD entity until RVDB explicitly decides
the canonical entity boundary between the base Atari Jaguar platform and
the Jaguar CD attachment.

Do not automatically:

- create `platform.atari.jaguar.cd`
- create `data/platforms/atari/jaguar_cd.yaml`
- add `optical-disc` to the base Atari Jaguar solely because of Jaguar CD
- add Jaguar CD software-image extensions to the base Atari Jaguar

Jaguar CD may ultimately require a separate platform, add-on, accessory,
hardware relationship, or another future normalized representation.

## Nintendo DSi

Do not create a production DSi entity until RVDB explicitly decides whether
Nintendo DSi is:

- a separate canonical platform
- a DS-family platform variant
- or represented through a future normalized family model

Hardware capability differences and DSiWare support require deliberate
boundary review.

## Sega Master System / Mark III

Do not create production YAML until RVDB explicitly decides the canonical
entity boundary between:

- Sega Mark III
- overseas Master System
- Japanese Master System

## Optional Platform Metadata

Continue deferring unsupported or insufficiently normalized values for:

- `family`
- `generation`
- `regions`
- `architecture`

## Emulator-Core Relationships

Do not invent `supports_core` relationships.

Populate them only after the required canonical core entities exist and the
relationships are researched separately.

## Additional Atari Families

The following Atari platform families remain outside the completed Atari
production batches and require their own controlled planning:

- Atari 8-bit computers
- Atari XEGS
- Atari ST
- modern Atari VCS
- Atari arcade hardware families

Atari Jaguar CD remains separately deferred because its entity boundary
requires an explicit modeling decision.

## Nintendo Hardware Revisions

Do not automatically create separate platform entities for:

- Game Boy Advance SP
- Game Boy micro
- Nintendo DS Lite
- Nintendo DSi XL
- Nintendo 2DS
- New Nintendo 3DS
- New Nintendo 3DS XL
- New Nintendo 2DS XL
- Wii RVL-001
- Wii RVL-101
- Wii mini / RVL-201

Hardware revision alone is not sufficient to establish a new canonical
RVDB platform entity.

---

# NEXT CHECKPOINT

## P2A9 — Select and Research Platform Population Batch 8

Status:

NEXT

Goal:

Select the next small, controlled platform population batch before creating
additional production YAML.

Required work:

1. audit remaining manufacturer/platform candidates
2. select a coherent Batch 8 scope
3. verify manufacturer coverage
4. determine canonical entity boundaries
5. determine canonical IDs and filesystem paths
6. research canonical names and justified aliases
7. research release years
8. determine valid platform categories
9. determine controlled media values
10. determine defensible software-image extensions
11. identify any boundary decisions requiring explicit deferral
12. explicitly defer unsupported metadata
13. write and review the Batch 8 plan
14. commit the plan separately before production creation

Candidate directions may include:

- Atari 8-bit computer family after explicit boundary review
- Atari XEGS after explicit boundary review
- Atari ST after explicit boundary review
- additional Nintendo platforms after explicit entity-boundary review
- Sega Master System only after explicit entity-boundary review
- another manufacturer after creating or verifying its canonical
  manufacturer entity

Population must continue to follow:

- `docs/platform_contract.md`
- `docs/platform_catalog_policy.md`

No Batch 8 production YAML should be created until the Batch 8 planning
checkpoint is complete.

Expected restart point:

P2A9 — Select and Research Platform Population Batch 8

---

# Phase 2A — Atari ST Platform Batch 8 Completion

## P2A9 — Atari ST Platform Population Batch 8

Status:

COMPLETE

Planning commit:

`dfcc9a5` — `docs: plan Atari ST platform batch 8`

Production commit:

`cb3d190` — `data: add Atari ST platform batch 8`

Production entity added:

- `platform.atari.st`

Production file added:

- `data/platforms/atari/st.yaml`

Atari ST Platform Batch 8 expanded the controlled Atari production
catalog with one canonical computer platform:

- Atari ST

The batch completed the controlled Phase 2A population sequence:

1. candidate audit
2. Atari ST batch selection
3. manufacturer verification
4. canonical ID and path selection
5. ST-family entity-boundary review
6. release-year decision
7. computer-category decision
8. floppy-media decision
9. conservative extension selection
10. emulator-core relationship deferral
11. optional metadata deferral
12. explicit plan creation and review
13. separate planning commit and push
14. Atari ST production YAML creation
15. targeted platform-contract validation
16. full production validation
17. canonical bundle rebuild
18. exact stale-baseline discovery
19. count-sensitive regression baseline synchronization
20. complete regression verification
21. implementation-result documentation
22. final production review
23. separate production commit and push

The production record uses only vocabulary already supported by
Platform Entity Contract v2.

No schema expansion was required.

Atari ST uses:

- canonical ID: `platform.atari.st`
- manufacturer: `manufacturer.atari`
- release year: `1985`
- category: `computer`
- media: `floppy`
- extensions:
  - `st`
  - `msa`
  - `stx`

No emulator-core relationships were invented.

The production record intentionally retains an empty `supports_core`
relationship list.

The following ST-family entities remain deliberately absent:

- `platform.atari.ste`
- `platform.atari.tt`
- `platform.atari.falcon`

These boundaries remain deferred for separate canonical review.

---

# Current Phase 2A Verification Baseline

Branch:

`develop`

Production entities:

37

Platform entities:

22

Production validation:

- entities checked: 37
- valid: 37
- schema errors: 0
- relationship errors: 0

Regression suite:

145 passing

Canonical graph:

- nodes: 37
- edges: 37

Canonical bundle:

`rvdb.bundle.json`

Canonical bundle build:

PASS

Working tree after Atari ST Batch 8 production commit:

CLEAN

Local/remote synchronization:

PASS

---

# Current Platform Catalog

Production platforms:

- `platform.arcade`
- `platform.atari.2600`
- `platform.atari.5200`
- `platform.atari.7800`
- `platform.atari.jaguar`
- `platform.atari.lynx`
- `platform.atari.st`
- `platform.nintendo.3ds`
- `platform.nintendo.ds`
- `platform.nintendo.game.boy`
- `platform.nintendo.game.boy.advance`
- `platform.nintendo.game.boy.color`
- `platform.nintendo.gamecube`
- `platform.nintendo.n64`
- `platform.nintendo.nes`
- `platform.nintendo.snes`
- `platform.nintendo.wii`
- `platform.nintendo.wii.u`
- `platform.sega.dreamcast`
- `platform.sega.game.gear`
- `platform.sega.genesis`
- `platform.sega.saturn`

Platform count:

22

---

# Phase 2A Deferred Decisions

The following work remains intentionally deferred.

## Atari Jaguar CD

Do not create a production Jaguar CD entity until RVDB explicitly decides
the canonical entity boundary between the base Atari Jaguar platform and
the Jaguar CD attachment.

Do not automatically:

- create `platform.atari.jaguar.cd`
- create `data/platforms/atari/jaguar_cd.yaml`
- add `optical-disc` to the base Atari Jaguar solely because of Jaguar CD
- add Jaguar CD software-image extensions to the base Atari Jaguar

Jaguar CD may ultimately require a separate platform, add-on, accessory,
hardware relationship, or another future normalized representation.

## Atari ST Family

The following related machines remain outside the completed Atari ST
Batch 8 and require separate canonical entity-boundary review:

- Atari STE
- Atari TT
- Atari Falcon

Do not automatically create:

- `platform.atari.ste`
- `platform.atari.tt`
- `platform.atari.falcon`

Do not merge their machine-specific capabilities into the canonical Atari ST
production record without separate research and modeling.

## Nintendo DSi

Do not create a production DSi entity until RVDB explicitly decides whether
Nintendo DSi is:

- a separate canonical platform
- a DS-family platform variant
- or represented through a future normalized family model

Hardware capability differences and DSiWare support require deliberate
boundary review.

## Sega Master System / Mark III

Do not create production YAML until RVDB explicitly decides the canonical
entity boundary between:

- Sega Mark III
- overseas Master System
- Japanese Master System

## Optional Platform Metadata

Continue deferring unsupported or insufficiently normalized values for:

- `family`
- `generation`
- `regions`
- `architecture`

## Emulator-Core Relationships

Do not invent `supports_core` relationships.

Populate them only after the required canonical core entities exist and the
relationships are researched separately.

## Additional Atari Families

The following Atari platform families remain outside the completed Atari
production batches and require their own controlled planning:

- Atari 8-bit computers
- Atari XEGS
- modern Atari VCS
- Atari arcade hardware families

Atari Jaguar CD remains separately deferred because its entity boundary
requires an explicit modeling decision.

Atari STE, Atari TT, and Atari Falcon remain separately deferred because
their boundaries relative to Atari ST require explicit canonical review.

## Nintendo Hardware Revisions

Do not automatically create separate platform entities for:

- Game Boy Advance SP
- Game Boy micro
- Nintendo DS Lite
- Nintendo DSi XL
- Nintendo 2DS
- New Nintendo 3DS
- New Nintendo 3DS XL
- New Nintendo 2DS XL
- Wii RVL-001
- Wii RVL-101
- Wii mini / RVL-201

Hardware revision alone is not sufficient to establish a new canonical
RVDB platform entity.

---

# NEXT CHECKPOINT

## P2A10 — Select and Research Platform Population Batch 9

Status:

NEXT

Goal:

Select the next small, controlled platform population batch before creating
additional production YAML.

Required work:

1. audit remaining manufacturer/platform candidates
2. select a coherent Batch 9 scope
3. verify manufacturer coverage
4. determine canonical entity boundaries
5. determine canonical IDs and filesystem paths
6. research canonical names and justified aliases
7. research release years
8. determine valid platform categories
9. determine controlled media values
10. determine defensible software-image extensions
11. identify any boundary decisions requiring explicit deferral
12. explicitly defer unsupported metadata
13. write and review the Batch 9 plan
14. commit the plan separately before production creation

Candidate directions may include:

- Atari 8-bit computer family after explicit boundary review
- Atari XEGS after explicit boundary review
- another Atari family after explicit canonical review
- additional Nintendo platforms after explicit entity-boundary review
- Sega Master System only after explicit entity-boundary review
- another manufacturer after creating or verifying its canonical
  manufacturer entity

Population must continue to follow:

- `docs/platform_contract.md`
- `docs/platform_catalog_policy.md`

No Batch 9 production YAML should be created until the Batch 9 planning
checkpoint is complete.

Expected restart point:

P2A10 — Select and Research Platform Population Batch 9

## P2B4-B.26.64 — Generic Nested Object Schema Contracts

Status:

COMPLETE

Commit:

- `f012549` — `feat: add nested object schema contracts`

Implemented:

- generic nested structured-object schema contracts
- nested `required`, `optional`, and `fields` support
- recursive list/object runtime validation
- deterministic nested validation paths
- indexed list-item error reporting
- unknown nested-field rejection for contracted objects
- backward compatibility for unconstrained legacy objects
- preservation of legacy `required: false` object definitions
- schema-definition validation for malformed nested contracts
- recursive nested-list validation

Validation:

- 230 tests passed
- 41 production entities checked
- 41 valid
- 0 schema errors
- 0 relationship errors
- runtime version remains `RVDB 0.2.1`

Architecture decision:

Structured compatibility evidence will use the generic nested-object
schema capability rather than a compatibility-specific validator.

The next authorized implementation area is the first-class
compatibility claim entity contract.

No production compatibility data has been added yet.


## P2B4-B.26.67 — Generic Multi-Target Entity References

Status:

COMPLETE

Commit:

- `a9dde62` — `feat: add multi-target entity references`

Implemented:

- generic multi-target constraints for `entity_reference` fields
- `entity_types` schema support for references that may target more than
  one canonical entity type
- preservation of existing singular `entity_type` reference semantics
- mutual exclusivity between `entity_type` and `entity_types`
- schema-definition validation for malformed `entity_types` constraints
- rejection of empty multi-target lists
- rejection of non-string and empty target-type values
- rejection of duplicate target entity types
- rejection of unknown target entity types
- runtime validation against any allowed target entity type
- backward compatibility for existing singular typed references
- dedicated multi-target entity-reference regression coverage

Validation:

- 247 tests passed
- 41 production entities checked
- 41 valid
- 0 schema errors
- 0 relationship errors
- runtime version remains `RVDB 0.2.1`

Architecture decision:

Compatibility claims may reference more than one canonical subject class
without introducing compatibility-specific reference logic.

The generic `entity_types` contract will support compatibility modeling
where a reference may legitimately target entities such as emulators,
cores, frontends, or other explicitly authorized entity classes.

The next authorized implementation area remains the first-class
compatibility claim entity contract.

No production compatibility data has been added yet.


## P2B4-B.26.70 — Generic List Minimum Constraint

Status:

COMPLETE

Commit:

- `a82b848` — `feat: add generic list minimum constraint`

Implemented:

- generic `min_items` constraint for list field definitions
- non-negative integer schema contract for `min_items`
- explicit support for `min_items: 0`
- rejection of negative, float, string, null, and boolean `min_items` values
- rejection of `min_items` on non-list field definitions
- runtime enforcement of minimum list cardinality
- nested-list support for the same generic constraint
- preservation of existing list `items` constraint behavior
- dedicated generic `min_items` regression coverage
- no compatibility-specific validation logic
- no production schema or data changes

Validation:

- 265 tests passed
- 41 production entities checked
- 41 valid
- 0 schema errors
- 0 relationship errors
- runtime version remains `RVDB 0.2.1`

Architecture decision:

Compatibility evidence may now use the generic list cardinality contract to
require at least one evidence item through `min_items: 1`, without introducing
compatibility-specific list validation.

The generic nested-object, multi-target entity-reference, and list minimum
constraint prerequisites are now available for the first-class compatibility
claim entity contract.

The next authorized implementation area remains the first-class
compatibility claim entity contract.

Compatibility implementation itself has not begun, and no production
compatibility data has been added yet.

## P2B4-B.26.77 — First-Class Compatibility Contract Design

Status:

DESIGN ACCEPTED — IMPLEMENTATION NOT YET STARTED

Purpose:

Freeze the minimum first-class compatibility entity contract before
introducing its production schema.

Architecture decisions:

- canonical entity type: `compatibility`
- compatibility represents an evidence-backed operational compatibility
  assertion between one emulator/core implementation and one platform
- common entity fields remain inherited:
  - `id`
  - `type`
  - `name`

Required compatibility fields:

- `subject`
- `platform`
- `playability`
- `evidence`

Optional compatibility fields:

- `version`
- `notes`

Subject contract:

- `subject` is a singular `entity_reference`
- authorized subject entity types:
  - `emulator`
  - `core`
- `frontend` is intentionally excluded from the initial operational
  compatibility subject contract
- frontend discovery/integration does not independently establish
  emulator/core operational compatibility

Platform contract:

- `platform` is a singular `entity_reference`
- target entity type is `platform`

Playability contract:

The controlled compatibility playability vocabulary is:

- `playable`
- `playable_limited`
- `experimental`
- `historical_only`
- `unknown`

Playability belongs to the compatibility claim rather than becoming a
universal property of the platform.

No separate `compatibility_state` field is introduced in this checkpoint.

Version contract:

- `version` is an optional string
- version-aware compatibility is supported without creating new emulator,
  core, or platform identities for ordinary software releases
- evidence items may also carry a version when the evidence itself is
  version-specific

Evidence contract:

- `evidence` is required
- evidence is a list of structured objects
- evidence requires `min_items: 1`
- each evidence object requires:
  - `source`
  - `url`
  - `checked_at`
- each evidence object may optionally contain:
  - `version`
  - `notes`

Initial evidence scalar representation:

- `source`: string
- `url`: string
- `checked_at`: string
- `version`: string
- `notes`: string

The generic nested-object schema contract will validate evidence structure.
The generic list `min_items` contract will enforce at least one evidence
record.

Deferred compatibility areas:

- compatibility confidence vocabulary
- machine-readable evidence authority/source classification
- BIOS/firmware requirements
- detailed BIOS schema
- additional compatibility target classes
- frontend as an operational compatibility subject
- dedicated compatibility resolver behavior
- compatibility-specific query commands
- production compatibility population

Confidence is intentionally deferred because P2B3 identifies possible future
values but requires explicit schema design before production use.

Relationship decision:

- the first compatibility contract does not require schema `relationships`
  entries
- `subject` and `platform` use typed entity-reference fields
- duplicate relationship declarations are avoided

Registration / creation boundary:

- adding `schemas/entities/compatibility.yaml` will register compatibility
  with schema discovery
- the generic `create` command requires both a schema and matching template
- therefore schema introduction alone must not automatically authorize
  interactive production compatibility creation
- compatibility template/data population remains separately controlled

Production safety:

- no compatibility production YAML is authorized yet
- no mass compatibility assertions are authorized
- no census/population work is authorized
- schema implementation must receive dedicated regression coverage before
  production compatibility data is introduced

Next implementation checkpoint:

P2B4-B.26.78 — First-Class Compatibility Schema Contract

That checkpoint may introduce the schema and dedicated schema-validation
tests only after this design record is reviewed.

## P2B4-B.26.78 — First-Class Compatibility Schema Contract

Status:

COMPLETE

Commit:

- `cd46239` — `feat: add compatibility entity schema`

Implemented:

- first-class `compatibility` entity schema
- compatibility schema registered through normal schema discovery
- required compatibility fields:
  - `subject`
  - `platform`
  - `playability`
  - `evidence`
- optional compatibility fields:
  - `version`
  - `notes`
- `subject` is a singular `entity_reference`
- authorized `subject` target entity types:
  - `emulator`
  - `core`
- `platform` is a singular `entity_reference`
- `platform` target entity type is `platform`
- controlled playability vocabulary:
  - `playable`
  - `playable_limited`
  - `experimental`
  - `historical_only`
  - `unknown`
- `evidence` is a required list
- evidence requires `min_items: 1`
- each evidence item is a structured object
- required evidence fields:
  - `source`
  - `url`
  - `checked_at`
- optional evidence fields:
  - `version`
  - `notes`
- all initial evidence scalar fields use string representation
- top-level `version` remains optional
- top-level `notes` remains optional
- no compatibility-specific schema relationships introduced
- deferred fields remain excluded:
  - `confidence`
  - `compatibility_state`
  - `bios`
  - `firmware`
- dedicated compatibility schema regression coverage added
- no compatibility-specific engine or validator changes required
- no compatibility template introduced
- no production compatibility data introduced

Normalized schema contract:

Required:

- `id`
- `type`
- `name`
- `subject`
- `platform`
- `playability`
- `evidence`

Optional:

- `aliases`
- `relationships`
- `metadata`
- `version`
- `notes`

Relationships:

- `{}`

Validation:

- 12 dedicated compatibility schema tests passed
- 277 total tests passed
- 41 production entities checked
- 41 valid
- 0 schema errors
- 0 relationship errors
- runtime version remains `RVDB 0.2.1`

Architecture decision:

The first-class compatibility schema is now implemented using only generic
schema-engine capabilities established by the earlier nested-object,
multi-target entity-reference, and `min_items` checkpoints.

Compatibility remains evidence-backed and operationally scoped to emulator/core
subjects targeting canonical platform entities.

Schema registration alone does not authorize compatibility population.

Production safety remains in effect:

- no compatibility template has been introduced
- no production compatibility YAML is authorized yet
- no mass compatibility assertions are authorized
- no compatibility census/population work is authorized

The next authorized work must remain controlled and must not introduce
production compatibility data without a separate explicit checkpoint.

## P2B4-B.26.84 — Compatibility Creation and Population Boundary

Status:

DESIGN ACCEPTED — IMPLEMENTATION NOT YET STARTED

Purpose:

Freeze the creation, storage, and initial population boundary for first-class
compatibility entities before introducing a compatibility template or any
production compatibility assertions.

Repository evidence:

- `compatibility` is registered through
  `schemas/entities/compatibility.yaml`
- the generic `create` command requires both:
  - a registered entity schema
  - a matching entity template
- `templates/entities/compatibility.yaml` does not currently exist
- compatibility therefore remains unavailable through normal interactive
  entity creation
- no production compatibility directory currently exists
- no production compatibility YAML currently exists
- current canonical compatibility-capable subjects include:
  - `core.bsnes`
  - `core.snes9x`
- no production `emulator` entities currently exist
- canonical platform entities are already available for controlled future
  compatibility assertions

Creation boundary:

- compatibility creation must remain disabled until a dedicated
  `templates/entities/compatibility.yaml` checkpoint is explicitly authorized
- schema registration by itself does not authorize interactive creation
- introducing the compatibility template will constitute an explicit change
  to the supported `create` entity-type surface
- template introduction must receive dedicated regression coverage
- no compatibility entity may be written merely as a side effect of template
  introduction or template testing

Canonical storage decision:

- production compatibility entities will use:
  `data/compatibilities/`
- the plural directory follows the generic create-command convention for the
  singular entity type `compatibility`
- nested organization beneath `data/compatibilities/` may be introduced later
  if production scale justifies it
- no compatibility production directory is created by this design checkpoint

Compatibility identity:

- compatibility remains a first-class entity and therefore receives its own
  canonical RVDB ID
- IDs continue to use the generic RVDB ID-generation contract
- the initial canonical namespace is:
  `compatibility.<slug>`
- compatibility IDs must identify the compatibility assertion itself rather
  than replacing the canonical IDs of its subject or platform
- the exact human-readable naming convention used to generate compatibility
  IDs must be frozen before the first production assertion is added

Template boundary:

A future compatibility template may represent the established schema fields:

- `id`
- `type`
- `name`
- `aliases`
- `subject`
- `platform`
- `playability`
- `evidence`
- `version`
- `notes`
- `relationships`
- `metadata`

The template must not introduce fields outside the registered compatibility
schema.

The template must not introduce deferred fields such as:

- `confidence`
- `compatibility_state`
- `bios`
- `firmware`

Reference-entry behavior:

- `subject` must resolve to an existing canonical `core` or `emulator`
- `platform` must resolve to an existing canonical `platform`
- frontend entities remain excluded as compatibility subjects
- compatibility creation must use the generic typed entity-reference machinery
  rather than compatibility-specific reference logic

Evidence-entry behavior:

- compatibility remains evidence-backed
- at least one evidence item is required
- each evidence item requires:
  - `source`
  - `url`
  - `checked_at`
- evidence may optionally include:
  - `version`
  - `notes`
- template implementation must not weaken the existing `min_items: 1`
  evidence contract
- placeholder/template evidence must not be mistaken for production evidence

Production population boundary:

Template implementation does not authorize production compatibility
population.

The first production compatibility assertion requires a separate explicit
checkpoint after template behavior has been implemented and regression-tested.

That first production checkpoint must:

1. select one existing canonical core subject
2. select one existing canonical platform target
3. establish a human-readable compatibility entity name
4. establish its generated canonical compatibility ID
5. research the operational compatibility claim
6. capture at least one qualifying evidence record
7. select the playability value supported by that evidence
8. validate the resulting entity through the normal production validator
9. review the assertion before any broader compatibility population begins

Population remains deliberately incremental.

The first successful compatibility assertion must not authorize:

- bulk generation
- compatibility census work
- automatic inference of compatibility from existing relationships
- conversion of every `supports` or `supports_core` relationship into a
  compatibility claim
- emulator compatibility population before canonical emulator entities exist

Evidence policy boundary:

Existing platform/core relationships are discovery hints only.

A relationship such as a core supporting a platform does not, by itself,
satisfy the compatibility evidence contract.

Compatibility assertions require independently reviewable evidence captured in
the compatibility entity itself.

Still deferred:

- compatibility confidence vocabulary
- machine-readable evidence authority/source classification
- BIOS/firmware compatibility modeling
- additional compatibility target classes
- frontend as an operational compatibility subject
- compatibility-specific resolver behavior
- compatibility-specific query commands
- bulk compatibility population
- compatibility census automation

Next implementation checkpoint:

P2B4-B.26.85 — Compatibility Creation Template Contract

That checkpoint may introduce:

- `templates/entities/compatibility.yaml`
- dedicated tests proving compatibility becomes available through the generic
  create surface
- dedicated tests proving template creation obeys the existing compatibility
  schema and typed-reference contracts

That checkpoint must not introduce production compatibility YAML.

---

# Phase 2B — Compatibility Creation Template Milestone

## P2B4-B.26.85 — Compatibility Creation Template Contract

Status:

COMPLETE

The compatibility entity creation boundary has been extended through the
generic RVDB creation workflow without introducing production compatibility
claims.

Completed work includes:

- added the canonical compatibility entity creation template
- integrated compatibility creation with the generic `create` command
- preserved schema-driven entity construction
- added compatibility-aware output-directory handling
- established the canonical compatibility production directory name:
  `data/compatibilities`
- preserved existing output-directory behavior for other entity types
- added dedicated compatibility template regression coverage
- expanded generic create-command regression coverage
- verified compatibility schema, template, and create-command integration
- confirmed that no production compatibility entity was created

Implementation commit:

`b83412e` — `feat: add compatibility creation template`

Implementation parent:

`af7dd8c` — `docs: define compatibility creation boundary`

Verification baseline:

- focused compatibility/create tests: 32 passing
- complete regression suite: 289 passing
- production entities checked: 41
- production entities valid: 41
- schema errors: 0
- relationship errors: 0
- RVDB version: 0.2.1
- working tree after implementation commit: clean
- local `develop` after implementation commit: one commit ahead of
  `origin/develop`
- production compatibility data: none

Verified absent production paths:

- `data/compatibility`
- `data/compatibilitys`
- `data/compatibilities`

The compatibility template establishes a creation contract only.

It does not authorize speculative compatibility claims or uncontrolled
production compatibility population.

Compatibility production data must remain evidence-based and must be
introduced only through separately planned, reviewed, tested, and validated
checkpoints.

# NEXT CHECKPOINT

## P2B4-B — Compatibility Production Modeling Planning

Status:

NEXT

Goal:

Determine the next controlled compatibility-modeling checkpoint now that the
compatibility schema and generic creation-template foundation are operational.

Required next-step constraints:

1. do not create speculative compatibility production claims
2. preserve the canonical compatibility entity contract
3. preserve the generic creation workflow
4. determine the first evidence-backed compatibility production scope before
   creating production YAML
5. review source and target entity requirements before introducing claims
6. keep compatibility production work separate from schema/template
   infrastructure work
7. run focused regression coverage before any production commit
8. run the complete regression suite before any production commit
9. run production validation before any production commit
10. update this milestone document after the next completed atomic checkpoint

Current restart baseline:

- branch: `develop`
- implementation HEAD: `b83412e`
- remote base before milestone documentation commit: `af7dd8c`
- regression suite: 289 passing
- production validation: 41 / 41 valid
- schema errors: 0
- relationship errors: 0
- RVDB version: 0.2.1
- production compatibility entities: 0

Expected restart point:

P2B4-B — Compatibility Production Modeling Planning

---

## P2B4-B — First Production Compatibility Claim

Status:

COMPLETE

Completed production claim:

- `compatibility.core.snes9x.platform.nintendo.snes`

Canonical endpoints:

- subject: `core.snes9x`
- platform: `platform.nintendo.snes`

Playability:

- `playable`

Evidence policy applied:

- official Libretro core documentation
- official Snes9x project repository
- official Libretro SNES compatibility documentation
- evidence checked on 2026-08-28
- no unsupported version value was invented

Production result:

- first production compatibility entity added under:
  `data/compatibilities/`
- production entity count increased from 41 to 42
- compatibility entity count increased from 0 to 1
- manifest and bundle baselines updated accordingly

Resolver correction:

Introducing the first compatibility entity exposed an ordering-dependent
partial-name collision because generic partial resolution returned the first
matching graph node.

The resolver was corrected so that partial human-name matching uses
entity-type precedence instead of raw graph insertion order.

This preserves:

- exact compatibility ID resolution
- exact platform/core name resolution
- alias resolution
- canonical platform precedence for ambiguous partial human-name searches

Verified example:

- `Super Nint` -> `platform.nintendo.snes`
- exact compatibility ID ->
  `compatibility.core.snes9x.platform.nintendo.snes`

Regression baseline:

- tests: 291 passed
- production entities checked: 42
- valid: 42
- schema errors: 0
- relationship errors: 0
- RVDB version: 0.2.1

Atomic implementation commit:

- `b59bc9a`
- `feat: add first production compatibility claim`

Repository state after completion:

- branch: `develop`
- local HEAD == `origin/develop`
- worktree clean

### P2B4-B Completion Boundary

This checkpoint proves that RVDB can now safely carry an evidence-backed
production compatibility entity without corrupting generic resolution,
manifest statistics, bundle generation, or validation.

It does not authorize uncontrolled compatibility population.

The next compatibility expansion must remain evidence-driven and
incremental.

---

## Next Milestone

### P2B4-C — Controlled Compatibility Population Planning

Goal:

Define the next small, evidence-backed compatibility population set before
creating additional production YAML.

Requirements:

- review currently available core subjects
- review canonical supported platform targets
- identify authoritative evidence for each proposed claim
- assign playability only where evidence justifies it
- omit unsupported version precision
- preserve exact-ID compatibility resolution
- preserve canonical entity precedence in generic human-name resolution
- run focused tests, full regression, and production validation before every
  commit

Current known production core subjects:

- `core.bsnes`
- `core.snes9x`

Current production compatibility claims:

- `compatibility.core.snes9x.platform.nintendo.snes`

No additional compatibility production YAML is authorized until the
P2B4-C planning checkpoint is reviewed.

---

# P2B4-C — Compatibility Production Population Closure

Status:

COMPLETE

P2B4-C established the first production population of the first-class
compatibility entity model.

The compatibility contract had already been implemented and protected by
schema, template, creation-surface, validation, resolver, build, manifest,
and regression infrastructure before production population began.

P2B4-C then introduced compatibility claims through controlled,
evidence-backed population rather than bulk speculative data entry.

## Production Compatibility Claims

The current production compatibility population contains exactly two
claims:

- `compatibility.core.snes9x.platform.nintendo.snes`
  - subject: `core.snes9x`
  - platform: `platform.nintendo.snes`
  - playability: `playable`

- `compatibility.core.bsnes.platform.nintendo.snes`
  - subject: `core.bsnes`
  - platform: `platform.nintendo.snes`
  - playability: `playable`

Each claim is backed by three source records and intentionally does not
assert unsupported version precision.

## Controlled Population Sequence

The first production claim established:

- production compatibility loading
- evidence-backed operational playability
- canonical core/platform references
- exact-ID resolver behavior
- preservation of canonical human-name resolution
- deterministic build and manifest integration

The second production claim demonstrated controlled population expansion
without changing the compatibility schema or introducing special-case
runtime behavior.

The second claim increased production inventory from:

- 42 to 43 total entities
- 1 to 2 compatibility entities

Only deterministic regression baselines affected by the intentional
production-count increase required correction.

## Current Compatibility Topology

Post-population architecture inspection established:

- canonical core entities: 2
- modeled platform-to-core topology pairs: 2
- production compatibility claims: 2
- unclaimed modeled topology pairs: 0
- compatibility claims without matching topology: 0

The modeled topology is therefore fully represented by production
compatibility claims.

Current modeled pairs:

- `core.bsnes` -> `platform.nintendo.snes`
- `core.snes9x` -> `platform.nintendo.snes`

Current production claims exactly correspond to those two pairs.

## Population Boundary

P2B4-C does not justify inventing additional compatibility claims merely
to increase production volume.

Further compatibility population requires one of the following first:

- canonical core population expansion
- canonical emulator population where an emulator-level compatibility
  claim is appropriate
- canonical platform/core topology expansion supported by evidence

Compatibility claims remain evidence-backed assertions over canonical
entities. They must not be used to create topology implicitly or to
substitute for missing canonical entity population.

## Final P2B4-C Baseline

At closure:

- production entities: 43
- compatibility entities: 2
- modeled topology pairs: 2
- claimed topology pairs: 2
- unclaimed topology pairs: 0
- orphan compatibility claims: 0
- regression suite: 291 passed
- production validation: 43 / 43
- schema errors: 0
- relationship errors: 0
- runtime version: RVDB 0.2.1

P2B4-C is complete.

The next Phase 2B operation should be selected from the remaining
milestone architecture rather than adding unsupported compatibility
claims beyond the currently modeled canonical topology.

---

# P2B5-B — First Production Frontend

Status:

COMPLETE

P2B5-B is complete.

The first production frontend entity has been added to RVDB:

- canonical ID: `frontend.retroarch`
- canonical name: `RetroArch`
- canonical production path: `data/frontends/retroarch.yaml`

The production frontend currently declares:

- `launches_core -> core.bsnes`
- `launches_core -> core.snes9x`

This establishes the first production use of the validated frontend entity contract and the `launches_core` relationship family.

The production population is now:

- production entities: 44
- frontend entities: 1
- compatibility entities: 2
- core entities: 2
- platform entities: 26

Regression and validation baseline:

- regression suite: 291 passed
- production validation: 44 / 44
- schema errors: 0
- relationship errors: 0
- runtime version: RVDB 0.2.1

Production commit:

- `c27f092` — `data: add RetroArch frontend`

Repository state after the production commit:

- branch: `develop`
- local `develop` synchronized with `origin/develop`
- worktree clean

P2B5-B therefore establishes RetroArch as RVDB's first production frontend while preserving the existing SNES, bsnes, Snes9x, and compatibility production topology.

The next milestone must begin from this committed and validated 44-entity production baseline.

---

# P2B6 — Production Emulator Population

Status:

IN PROGRESS

Purpose:

Begin production population of RVDB's existing Emulator entity architecture while preserving schema, relationship, validation, creation, and regression guarantees.

The Emulator entity type already existed as a registered schema contract before P2B6, but it had no production entities and was not exposed through the generic schema/template-driven creation surface.

P2B6 begins by establishing that creation surface before introducing any production Emulator entity.

---

## P2B6-A.1 — Emulator Production Creation Surface

Status:

COMPLETE

Implementation commit:

`0e00c27` — `feat: enable emulator creation surface`

Implementation parent:

`c9a664c` — `docs: record first production frontend milestone`

Purpose:

Expose the existing Emulator entity type through RVDB's generic creation infrastructure without introducing production Emulator data.

Changes:

- added `templates/entities/emulator.yaml`
- added `tests/test_emulator_creation_v2.py`
- updated `tests/test_create_command_v2.py`
- added Emulator to the exact supported generic creation-type baseline
- increased supported creation types from 9 to 10
- preserved schema/template-driven entity construction
- preserved canonical plural output routing to `data/emulators`
- verified `EntityFactory.create_entity()` can construct a schema-valid Emulator entity
- verified Emulator template vocabulary matches the registered Emulator schema
- verified Emulator template relationship keys match the registered relationship contract
- verified creation itself does not write production data

Emulator template defaults now expose:

- `id`
- `type`
- `name`
- `aliases`
- `developer`
- `operating_systems`
- `launch_mechanisms`
- `official_website`
- `source_repository`
- `status`
- `relationships.supports_platform`
- `relationships.supports_core`
- `metadata`

Generic creation types after P2B6-A.1:

1. `compatibility`
2. `core`
3. `developer`
4. `emulator`
5. `frontend`
6. `game`
7. `genre`
8. `manufacturer`
9. `platform`
10. `publisher`

Regression baseline after implementation:

- 300 tests passing
- production validation: 44 / 44
- schema errors: 0
- relationship errors: 0
- RVDB runtime version: 0.2.1

Production population boundary after implementation:

- total production entities: 44
- production Emulator entities: 0
- production Emulator YAML files: 0

Important architectural boundary:

P2B6-A.1 establishes Emulator creation capability only.

It does not select, model, or add the first production Emulator entity.

No production relationship is introduced merely because the schema permits it.

Future Emulator population must continue to justify relationships against canonical RVDB entities and the actual architecture of the represented software.

Repository state immediately after the implementation commit:

- branch: `develop`
- implementation HEAD: `0e00c279ecc875a924f7cf592e321d8c2fd255f2`
- `origin/develop`: `0e00c279ecc875a924f7cf592e321d8c2fd255f2`
- worktree clean
- implementation pushed successfully

Next milestone:

Select and model the first production Emulator entity from the committed P2B6-A.1 creation-surface baseline.

Do not assume which Emulator will be selected until the candidate and relationship evidence are audited.

---
