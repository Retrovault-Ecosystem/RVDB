# RVDB Platform Entity Contract

_Last Updated: 2026-08-26_

---

# Purpose

This document defines the canonical metadata contract for RVDB platform
entities during Phase 2A platform-database expansion.

The contract exists to prevent large-scale platform data population from
outgrowing or bypassing the schema-driven RVDB architecture.

Platform data must remain:

- canonical
- schema-driven
- machine-validatable
- relationship-aware
- suitable for large-scale expansion
- independent of any single consumer application

---

# Design Principles

## 1. Canonical identity remains stable

Every platform is an RVDB entity and inherits the common entity contract:

- `id`
- `type`
- `name`
- `aliases`
- `relationships`
- `metadata`

Canonical IDs continue to use dot notation.

Examples:

- `platform.nintendo.nes`
- `platform.nintendo.snes`
- `platform.sega.genesis`

Aliases must not replace canonical identity.

---

## 2. Important platform data belongs in first-class fields

Information required for platform discovery, filtering, comparison,
relationships, validation, or downstream application behavior should not
be hidden inside free-form `metadata`.

First-class platform fields are preferred when the information has a
stable and reusable semantic meaning.

---

## 3. Metadata remains an escape hatch, not the primary schema

The common `metadata` object may retain miscellaneous notes or transitional
information.

It must not become a substitute for proper schema fields.

Important structured information should migrate out of metadata once a
validated schema representation exists.

---

# Platform Entity Contract v2

## Common required fields

Inherited from the common entity schema:

- `id`
- `type`
- `name`

## Common optional fields

Inherited from the common entity schema:

- `aliases`
- `relationships`
- `metadata`

---

# Platform-Specific Fields

## category

Status:

REQUIRED

Purpose:

Classifies the fundamental platform type.

Examples may include:

- console
- handheld
- computer
- arcade

The final normalized vocabulary must be schema-controlled before
large-scale platform population.

---

## manufacturer

Status:

OPTIONAL

Schema type:

`entity_reference_list`

Target:

`manufacturer`

Purpose:

References canonical manufacturer entities associated with the platform.

A list is retained because some hardware may involve multiple relevant
manufacturing organizations.

Unknown, collective, or historically ambiguous manufacturers must not be
represented using fake canonical entity IDs.

---

## family

Status:

OPTIONAL

Schema type:

`string`

Purpose:

Records a stable platform-family classification where useful.

This field is intended for related hardware marketed or technically
organized as one recognizable system family.

The field must not replace explicit platform relationships when those
relationships become appropriate.

---

## release_year

Status:

OPTIONAL

Schema type:

`integer_or_null`

Purpose:

Records the platform's earliest canonical commercial release year.

Regional release information requires a more structured representation and
must not be compressed into this field.

---

## generation

Status:

OPTIONAL

Schema type:

`integer_or_null`

Purpose:

Records an accepted hardware generation when that concept meaningfully
applies.

Platforms for which generation numbering is not meaningful may use null or
omit the field according to the finalized schema rules.

---

## regions

Status:

OPTIONAL

Schema direction:

validated list

Purpose:

Records regions in which the platform had an official or historically
significant release.

The normalized region vocabulary must be schema-controlled before
large-scale platform population.

---

## media

Status:

OPTIONAL

Schema type:

controlled string list

Purpose:

Records canonical software/media formats associated with the platform.

Normalized vocabulary:

- `cartridge`
- `floppy`
- `optical-disc`
- `cassette`
- `digital`

The vocabulary is schema-controlled through `list.items.enum`.

Additional media values must not be introduced directly into production
data without first extending the canonical schema vocabulary deliberately.

---

## extensions

Status:

OPTIONAL

Schema direction:

validated list

Purpose:

Records common file extensions associated with software images or content
for the platform.

Extensions describe common file representations and do not imply that
every listed emulator or core supports every extension.

---

## architecture

Status:

OPTIONAL

Schema direction:

validated list

Purpose:

Records major hardware or CPU architecture classifications useful for
technical discovery and compatibility analysis.

The field must use normalized values rather than arbitrary descriptive
sentences.

---

# Platform Relationships

## supports_core

Schema type:

`entity_reference_list`

Target:

`core`

Purpose:

References Libretro/emulator core entities that support the platform.

This relationship remains part of the canonical platform contract.

Core-side platform relationships must remain consistent with the graph and
relationship-validation architecture.

---

# Regional Naming

Regional names are important platform data but must not yet be introduced
as an unconstrained free-form object.

Examples of information eventually required include:

- regional display names
- alternate marketed names
- region-to-name association

The current `aliases` field remains usable for searchable alternate names,
but it does not encode the region associated with an alias.

A structured regional-name representation should be introduced only when
the schema engine can validate the internal structure of mapping values.

---

# Regional Release Information

The `release_year` field represents the earliest canonical platform
release year.

Detailed regional release information should eventually represent
region-specific release data.

That information must not be added as an arbitrary free-form object merely
because the current schema engine accepts mappings.

A validated structured representation is required first.

---

# Schema Capability Requirements

The Phase 2 platform audit confirmed that the Foundation schema engine
supports these ordinary types:

- `string`
- `integer`
- `integer_or_null`
- `boolean`
- `list`
- `object`
- `entity_reference`
- `entity_reference_list`

P2A1 added generic reusable schema constraints without introducing
platform-specific validator logic.

Implemented generic constraint capabilities include:

- string `enum` constraints
- typed `list.items`
- controlled string vocabularies inside list items
- schema-definition validation for malformed constraints
- builder-side enforcement of constrained list values

Constraint grammar is intentionally bounded:

- `enum` is supported for string fields
- `items` is supported for list fields
- list item types are limited to ordinary non-reference item types
- entity-reference lists continue to use `entity_reference_list`
- relationship target typing continues to use `entity_type`

The current `object` type still validates only that a value is a mapping.

Typed mapping values and structured object validation remain deferred until
a concrete Platform v2 requirement justifies extending the schema language.

---

# Initial Migration Result

The Foundation dataset contains four platform entities:

- Arcade
- Nintendo Entertainment System
- Super Nintendo
- Sega Genesis

The four entities were audited against Platform Entity Contract v2 after
the schema and builder changes were implemented.

Migration result:

NO FORCED DATA EDITS REQUIRED

All four existing platform entities already satisfy the finalized required
Platform v2 contract.

The new Platform v2 fields are optional and were not added with empty,
guessed, or speculative values merely to match the entity template.

Existing justified data was preserved:

- all four platforms already provide a valid canonical `category`
- NES retains its existing `media` value
- NES retains its existing `extensions` value
- existing manufacturer relationships remain unchanged
- existing `supports_core` relationships remain unchanged
- Arcade retains transitional `legacy_manufacturer` metadata

The migration gate passed:

- schema validation
- relationship validation
- full regression testing
- canonical bundle build

---

# Non-Goals for P2A1

P2A1 does not attempt to:

- populate the complete platform database
- populate emulator entities
- populate all Libretro cores
- create game metadata
- redesign the relationship graph
- introduce consumer-specific RetroVault application fields
- store artwork or media assets
- place unvalidated complex data into metadata as a shortcut

---

# P2A1 Completion Criteria

Platform Entity Contract v2 is complete when:

1. canonical platform fields are finalized
2. required and optional fields are classified
3. normalized vocabulary requirements are defined
4. required generic schema capabilities are tested
5. platform schema changes are implemented
6. platform template changes are implemented
7. the four Foundation platform entities are migrated
8. production validation passes
9. the complete regression suite passes
10. the canonical bundle builds successfully
11. the milestone documentation records the completed checkpoint

Only after these gates pass should RVDB begin large-scale platform data
population.

---

# Current Status

Phase:

Phase 2A — Platform Database Expansion

Checkpoint:

P2A1 — Platform Entity Contract v2

Status:

COMPLETE

Design audit:

COMPLETE

Contract specification:

FINALIZED

Implementation:

COMPLETE

Verification baseline:

- generic schema constraints implemented
- Platform Schema v2 implemented
- Platform Entity Template v2 implemented
- schema-driven builder constraint enforcement implemented
- four Foundation platform entities audited
- forced production migration edits required: none
- production entities checked: 19
- production entities valid: 19
- schema errors: 0
- relationship errors: 0
- regression suite: 144 passed
- canonical graph nodes: 19
- canonical graph edges: 19
- canonical bundle build: PASS

Next:

Begin the next Phase 2A checkpoint for controlled large-scale platform
catalog expansion.
