# RVDB Phase 2A — P2A21

## Sega SC-3000 Platform Population — Batch 12 Plan

_Last Updated: 2026-08-26_

---

# Status

RESEARCHED — DECISION READY

No production platform YAML is authorized by this document.

No Batch 12 production entity should be created until this planning
checkpoint has been reviewed and accepted.

---

# Objective

Research and determine the canonical RVDB entity boundary for the Sega
SC-3000 and its closely related hardware.

The primary questions are:

1. Should SC-3000 be a canonical platform entity?
2. Should SC-3000H be a separate platform entity?
3. Should SC-3000 be merged with SG-1000?
4. What canonical name, aliases, release year, category, media,
   extensions, and relationships are justified?

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
- `platform.sega.sg1000`

No new manufacturer entity is required for Batch 12.

---

# Research Findings

## 1. Sega SC-3000

Sega identifies the SC-3000 as a "game computer" with an integrated
keyboard.

Official Sega documentation gives the original release date as:

`1983-07-15`

Canonical release year:

`1983`

The SC-3000 was designed to operate as a personal computer connected to a
television and supported programming through BASIC cartridges.

The official hardware documentation identifies:

- integrated keyboard
- cartridge slot
- cassette/data-recorder connection
- printer connection
- joystick connection
- television/RF video connectivity

The platform therefore has a meaningful computer-oriented identity.

It is not merely an alternate name for the SG-1000.

---

# 2. SC-3000H Boundary

SC-3000H remains inside the canonical SC-3000 platform boundary.

Sega identifies SC-3000H as a hardware-improved version of SC-3000 with
the keyboard changed from rubber keys to plastic hard keys.

Sega describes the remaining performance as substantially equivalent.

SC-3000H release:

`1983-12-09`

This is a hardware revision rather than a sufficiently distinct platform
for RVDB's canonical platform model.

No production entity:

`platform.sega.sc3000.h`

should be created.

The SC-3000H remains represented as a hardware revision within:

`platform.sega.sc3000`

---

# 3. SG-1000 Boundary

SC-3000 and SG-1000 share substantial underlying hardware and software
compatibility.

However, Sega explicitly distinguishes their intended platform roles.

SC-3000 is Sega's home/game computer with an integrated keyboard.

SG-1000 is Sega's dedicated home game machine derived from the SC-3000
hardware concept.

Therefore:

`platform.sega.sc3000`

and

`platform.sega.sg1000`

remain separate canonical entities.

SC-3000 must not become an alias of SG-1000.

SG-1000 must not become an alias of SC-3000.

Shared hardware architecture or software compatibility does not by itself
justify collapsing distinct platform identities.

---

# 4. Software Compatibility

The SC/SG software ecosystem demonstrates meaningful compatibility
between the systems.

Compatibility does not require the two hardware platforms to be collapsed
into one canonical RVDB entity.

Shared software should eventually be represented through appropriate
software/game relationships rather than by merging platform identity.

---

# Entity-Boundary Decision

**ONE CANONICAL SC-3000 PLATFORM ENTITY**

Canonical ID:

`platform.sega.sc3000`

Canonical name:

`Sega SC-3000`

SC-3000H remains inside this platform boundary.

SG-1000 remains a separate canonical platform.

No SC-3000H production entity is created.

No SG-1000 merge is performed.


# Canonical Aliases

Approved aliases:

- `SC-3000`
- `Sega SC-3000`

No speculative regional or hardware aliases should be added.

`SC-3000H` is not added as a canonical alias solely because it is a
hardware revision.

---

# Category Decision

Canonical category:

`computer`

Rationale:

Sega explicitly describes SC-3000 as a "game computer."

Its integrated keyboard, BASIC programming capability, television
connection, data-recorder interface, and peripheral expansion reinforce
its computer-oriented identity.

The presence of cartridge-based games does not require classification as a
console.

---

# Release-Year Decision

Canonical release year:

`1983`

The canonical platform begins with the original SC-3000 release.

SC-3000H's December 1983 release remains a hardware revision within the
same platform boundary.

---

# Media Decision

Canonical media:

- `cartridge`
- `cassette`

Rationale:

Sega's official SC-3000 hardware documentation identifies a cartridge
slot and a cassette/data-recorder connection.

Sega's software documentation identifies cartridge software for the
SC/SG series and documents data-recorder-compatible software.

No new controlled media vocabulary is introduced by Batch 12.

The existing RVDB media vocabulary is authoritative:

- `cartridge`
- `floppy`
- `optical-disc`
- `cassette`
- `digital`

---

# Extension Decision

Defensible production extensions:

- `sc`
- `sg`
- `bit`

## `sc`

`.sc` is an established SC-3000 software-image extension in the emulation
ecosystem.

It is appropriate as an SC-3000-specific canonical extension.

## `sg`

`.sg` is established in the SG-1000/SC-3000 software ecosystem for
compatible cartridge images.

Its inclusion is justified because SC-3000 and SG-series software
compatibility is directly documented by Sega.

## `bit`

MAME's current Castool documentation identifies `.bit` specifically as
the Sega SC-3000 cassette-image format.

This is the strongest directly documented cassette-image extension for the
SC-3000.

---

# Deferred Extensions

The following are deliberately excluded from the initial canonical
extension list:

- `bin`
- `cas`
- `wav`
- `zip`
- `7z`

Reasons:

- `bin` is a generic binary-image extension rather than an
  SC-3000-specific canonical format.
- `cas` represents cassette data in some emulation ecosystems but requires
  additional format-level normalization before becoming canonical RVDB
  metadata.
- `wav` is a raw audio/container format rather than a platform-specific
  software-image format.
- `zip` and `7z` are archive formats rather than native software-image
  formats.

Frontend or emulator acceptance alone is not sufficient justification for
adding these values to the canonical RVDB production record.

---

# Emulator-Core Relationships

No `supports_core` relationships will be created during Batch 12.

SC-3000 support exists in emulator software, but RVDB core relationships
remain deferred until canonical emulator-core entities exist and the core
entity model and relationship research process are stable.

Therefore the production relationship state remains:

`supports_core: []`

---

# Unsupported / Deferred Metadata

The following metadata remains intentionally deferred from the initial
SC-3000 production record unless independently justified by the existing
RVDB contract:

- `family`
- `generation`
- `regions`
- `architecture`

No unsupported values should be invented merely to make the record appear
more complete.

The SC-3000H revision relationship is also deferred because the current
platform contract does not establish a dedicated hardware-revision entity
model.

---

# Filesystem Decision

Canonical production path:

`data/platforms/sega/sc3000.yaml`

The filename follows the established Sega platform naming convention and
the canonical ID:

`platform.sega.sc3000`

No alternate filename such as `sc-3000.yaml`, `sc_3000.yaml`, or
`sc3000h.yaml` should be used for the canonical platform record.

---

# Production Entity Shape

The planned production entity should contain only fields supported by the
existing Platform Entity Contract and justified by this research.

Planned identity:

- ID: `platform.sega.sc3000`
- Name: `Sega SC-3000`
- Manufacturer: `manufacturer.sega`
- Category: `computer`
- Release year: `1983`

Planned media:

- `cartridge`
- `cassette`

Planned extensions:

- `sc`
- `sg`
- `bit`

Planned relationships:

`supports_core: []`

Optional metadata without sufficient independent justification remains
omitted.
# Batch Scope

Batch 12 contains exactly one production platform entity:

`platform.sega.sc3000`

The following are explicitly outside Batch 12 production scope:

- SC-3000H as a separate entity
- SG-1000 replacement or merge
- additional Sega platforms
- emulator-core entities
- game/software entities
- speculative metadata
- unsupported media values
- generic archive extensions

This keeps Batch 12 a small, controlled population change.

---

# Acceptance Criteria

The planning checkpoint is considered ready for production only if all of
the following are accepted:

1. SC-3000 is recognized as a distinct canonical platform.
2. SC-3000H is treated as a hardware revision within SC-3000.
3. SG-1000 remains a separate canonical platform.
4. Canonical ID is `platform.sega.sc3000`.
5. Canonical name is `Sega SC-3000`.
6. Category is `computer`.
7. Release year is `1983`.
8. Media values are `cartridge` and `cassette`.
9. Extensions are limited to `sc`, `sg`, and `bit`.
10. `supports_core` remains empty.
11. Unsupported metadata remains omitted.
12. Production path is `data/platforms/sega/sc3000.yaml`.
13. Batch 12 contains only the SC-3000 platform entity.
14. Production YAML is created only after this planning document is
    reviewed and accepted.

---

# Research Conclusion

The research supports adding Sega SC-3000 as a distinct canonical RVDB
platform entity.

The recommended production decision is:

**ACCEPT**

Canonical entity:

`platform.sega.sc3000`

Canonical name:

`Sega SC-3000`

Category:

`computer`

Release year:

`1983`

Media:

- `cartridge`
- `cassette`

Extensions:

- `sc`
- `sg`
- `bit`

SC-3000H remains within the SC-3000 platform boundary.

SG-1000 remains a separate canonical entity.

No emulator-core relationships are introduced.

No unsupported metadata is invented.

---

# Planning Checkpoint Decision

**P2A21 — READY FOR REVIEW**

This document defines the proposed Batch 12 scope and canonical entity
boundary.

It does not authorize production creation by itself.

The next operation after review is a controlled production creation
checkpoint for:

`platform.sega.sc3000`

No other Batch 12 production entity is authorized by this plan.
