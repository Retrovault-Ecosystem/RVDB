# RVDB Phase 2A — P2A14

## Sega SG-1000 Platform Population — Batch 11 Plan

_Last Updated: 2026-08-26_

---

# Status

ACCEPTED — PRODUCTION READY

The P2A15 planning decision has been accepted.

The controlled Batch 11 production entity is now authorized to be created
under the production boundary defined below.

---

# Objective

Research and determine the canonical RVDB entity boundary for the Sega
SG-1000 platform and its closely related hardware.

The primary questions are:

1. Should SG-1000 be a canonical platform entity?
2. Should SG-1000 II be a separate platform entity?
3. Should SC-3000 be part of the same platform entity?
4. Should Othello Multivision be a separate platform entity?
5. What canonical name, aliases, release year, media, extensions, and
   relationships are justified?

The decision must follow:

- `docs/platform_contract.md`
- `docs/platform_catalog_policy.md`

---

# Existing Manufacturer Coverage

Canonical manufacturer:

`manufacturer.sega`

Existing Sega production platforms include:

- `platform.sega.genesis`
- `platform.sega.game.gear`
- `platform.sega.saturn`
- `platform.sega.dreamcast`
- `platform.sega.master.system`

No new manufacturer entity is required for Batch 11.

---

# Research Findings

## 1. Sega SG-1000

Sega's official hardware history identifies the SG-1000 as Sega's first
consumer game console.

Recognized release date:

`1983-07-15`

Canonical release year:

`1983`

The SG-1000 represents a distinct console platform and is not merely an
alias of the SC-3000.

---

## 2. SG-1000 II

SG-1000 II remains within the canonical SG-1000 platform boundary.

No production entity:

`platform.sega.sg1000.ii`

should be created.

Hardware-specific differences may be represented later through normalized
variant metadata if such a model is introduced.

---

## 3. SC-3000 Boundary

SC-3000 remains a separate computer-oriented platform candidate.

It is not an alias of:

`platform.sega.sg1000`

No SC-3000 production entity is created by Batch 11.

A future SC-3000 platform population should receive its own planning
checkpoint.

---

## 4. Othello Multivision Boundary

SG-1000 software is compatible with Othello Multivision hardware.

Othello Multivision does not become a separate canonical RVDB platform
entity solely because it is separate licensed hardware.

Compatibility and clone relationships may be represented later through a
future hardware/variant relationship model.

---

# Entity-Boundary Decision

**ONE CANONICAL SG-1000 PLATFORM ENTITY**

Canonical ID:

`platform.sega.sg1000`

Canonical name:

`Sega SG-1000`

SG-1000 II remains inside this boundary as a hardware revision.

SC-3000 remains outside this boundary.

Othello Multivision remains outside this boundary as compatible hardware.

---

# Canonical Aliases

Approved aliases:

- `SG-1000`
- `Sega SG1000`

No speculative regional or hardware aliases should be added.

SG-1000 II does not become a canonical alias solely because it is a
hardware revision.


---

# Media Decision

Canonical media:

- `cartridge`

The existing controlled RVDB media vocabulary is sufficient.

No new media vocabulary is introduced by Batch 11.

---

# Extension Decision

Production extension:

- `sg`

Do not add:

- `bin`
- `rom`

solely because emulator cores accept generic extensions.

The RVDB extension field should represent defensible platform
software-image conventions.

Additional extensions may be reconsidered later if independent evidence
justifies them.


---

# Category Decision

Canonical category:

`console`

The SG-1000 is represented as a home video game console.

---

# Release-Year Decision

Canonical release year:

`1983`

The canonical platform begins with the original SG-1000 release.

SG-1000 II's 1984 release is treated as a hardware revision rather than a
new platform creation date.

---

# Emulator-Core Relationships

No supports_core relationships will be created during Batch 11.

SG-1000 support exists in multiple emulator cores, but RVDB core
relationships remain deferred until canonical core entities and a
dedicated relationship-research process are available.

The production relationship state is:

supports_core: []


---

# Optional Metadata

The following fields remain deferred:

- `family`
- `generation`
- `regions`
- `architecture`

These fields must not be populated merely because hardware information
exists.

Regional and hardware distinctions should be normalized before entering
these fields.

---

# Proposed Production Record

If this planning decision is accepted, the production record should use:

ID:

`platform.sega.sg1000`

Type:

`platform`

Name:

`Sega SG-1000`

Manufacturer:

`manufacturer.sega`

Release year:

`1983`

Category:

- `console`

Media:

- `cartridge`

Extensions:

- `sg`

Relationships:

supports_core: []

---

# Production Boundary

P2A14 authorizes planning only.

The following production file must not be created during this checkpoint:

`data/platforms/sega/sg1000.yaml`

No existing production platform is modified by P2A14.

No manufacturer record is added.

No emulator-core relationship is added.

---

# Validation Expectations

After the planning checkpoint is accepted and production data is created,
the expected dataset increase will be:

- entities: +1
- platforms: +1

The expected production entity will be:

`platform.sega.sg1000`

The production record must validate with:

- 0 schema errors
- 0 relationship errors

The complete regression suite must pass before the production record is
committed.

---

# Decision Summary

P2A14 recommends one canonical Sega SG-1000 platform entity.

Canonical ID:

`platform.sega.sg1000`

Canonical name:

`Sega SG-1000`

SG-1000 II is included within the platform boundary.

SC-3000 remains a separate future platform candidate.

Othello Multivision does not receive a duplicate SG-1000 platform entity.

The production record will use:

- manufacturer: `manufacturer.sega`
- release year: `1983`
- category: `console`
- media: `cartridge`
- extension: `sg`
- supports_core: empty

Optional hardware and regional metadata remains deferred.

---

# Next Checkpoint

P2A15 — Review and accept the Batch 11 SG-1000 planning decision.

Only after acceptance should the controlled SG-1000 production record be
created.

---

# End of P2A14

Planning document complete.

No production YAML created.

No commit performed.

