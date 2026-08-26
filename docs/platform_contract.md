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

Schema direction:

validated list

Purpose:

Records canonical software/media formats associated with the platform.

Examples may include:

- cartridge
- floppy
- optical-disc
- digital
- cassette

The final vocabulary must be normalized and schema-controlled.

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
currently validates these ordinary types:

- `string`
- `integer`
- `integer_or_null`
- `boolean`
- `list`
- `object`
- `entity_reference`
- `entity_reference_list`

The current `object` type validates only that a value is a mapping.

The current generic `list` type does not provide Platform v2 controlled
vocabulary semantics.

Before large-scale platform population, the schema architecture should be
extended carefully enough to support normalized structured platform data.

Required capability work should remain generic and reusable rather than
platform-specific.

Candidate capabilities include:

- typed list items
- controlled list vocabularies
- controlled string vocabularies
- typed mapping values
- structured object validation where justified

Exact implementation details must be determined through tests before
changing production schemas.

---

# Initial Migration Scope

The current Foundation dataset contains four platform entities:

- Arcade
- Nintendo Entertainment System
- Super Nintendo
- Sega Genesis

These entities will be migrated only after the Platform Entity Contract v2
schema is implemented and tested.

No mass platform YAML population should begin before that migration passes:

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

Design audit:

COMPLETE

Contract specification:

PROPOSED

Next:

Define and test the minimum generic schema capabilities required to enforce
the Platform Entity Contract v2.
