# RVDB Phase 2A — P2A11

## Sega Mark III / Master System Platform Population — Batch 10 Plan

_Last Updated: 2026-08-26_

---

# Status

RESEARCHED — DECISION READY

No production platform YAML is authorized by this document.

No canonical Batch 10 production entity should be created until this
planning checkpoint has been reviewed and accepted.

---

# Objective

Research and determine the canonical RVDB entity boundary for the Sega
Mark III and Sega Master System hardware/software ecosystem.

The primary question is whether RVDB should represent:

1. Sega Mark III and Master System as one canonical platform entity
2. Sega Mark III and Master System as separate canonical platform entities
3. a canonical platform plus a future normalized regional/hardware
   relationship
4. another explicitly justified representation

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

No new manufacturer entity is required for Batch 10.

---

# Research Scope

The following areas must be researched before production creation.

## 1. Sega Mark III

Research:

- official name
- Japanese launch date
- hardware architecture
- software compatibility
- cartridge format
- Sega Card / My Card compatibility
- relationship to SG-1000 and SC-3000 software
- regional limitations
- BIOS behavior
- emulator representation

---

## 2. Sega Master System

Research:

- official name
- Japanese Master System history
- overseas Master System history
- hardware differences from Mark III
- software compatibility
- cartridge format
- Sega Card compatibility
- regional differences
- BIOS behavior
- emulator representation

---

## 3. Japanese Master System

Explicitly investigate whether the Japanese Master System should be:

- an alias/variant of Mark III / Master System
- a separate platform
- or represented through future structured regional metadata

Do not create a production entity solely because the Japanese machine
has hardware differences.

---

## 4. Western Master System

Research:

- North American hardware
- European hardware
- cartridge differences
- regional software compatibility
- BIOS and region behavior
- Power Base Converter relationship

Regional branding alone must not create duplicate entities.

---

# Research Findings

## Sega Official Hardware History

Sega's official hardware history identifies the Sega Mark III as a Japanese
home console released on 1985-10-20.

Sega describes the Mark III as retaining compatibility with earlier SC/SG
software while adding substantially improved graphics capability and a
dedicated My Card Mark III slot.

Sega's official Master System documentation identifies the Japanese Master
System as a Mark III-derived system with additional integrated capabilities,
including FM sound, rapid-fire functionality, and direct 3-D glasses support.

Sega also identifies the overseas Master System / Power Base as an overseas
redesign of the Mark III released before the Japanese Master System.

Therefore, the hardware history demonstrates meaningful regional and
hardware distinctions, but also a direct lineage between Mark III and Master
System.

## Sega Official Software Evidence

Sega's official software documentation explicitly groups Sega Mark III and
Master System software together.

Sega's Mark III software documentation lists My Card Mark III and Gold
Cartridge software usable by the Mark III and Master System.

Sega's Master System software documentation likewise describes Gold
Cartridge software usable by both systems.

This is strong evidence that the software ecosystem should not automatically
be split into separate RVDB platform entities.

## RetroArch / Libretro Evidence

RetroArch uses the database identity:

`Sega - Master System - Mark III`

Multiple Libretro cores associate with this same database, including:

- Genesis Plus GX
- SMS Plus GX
- Gearsystem
- Emux SMS
- PicoDrive

Genesis Plus GX additionally exposes separate emulation hardware selections
for:

- Mark III
- Master System
- Master System II

Gearsystem similarly exposes a combined:

`Master System / Mark III`

hardware mode while separately exposing Japanese and export regional
settings.

This demonstrates that hardware and regional distinctions can be preserved
at the emulator/hardware-mode level without requiring separate canonical
RVDB platform entities.

## Regional Hardware Differences

Japanese and Western Master System-family hardware has meaningful regional
and physical differences.

These differences are relevant to future structured metadata, compatibility
information, or hardware relationships.

They do not, by themselves, require separate RVDB platform entities because
the software/emulation ecosystem consistently treats Mark III and Master
System as one closely related platform family.

---

# P2A11 Entity-Boundary Decision

Decision:

**ONE CANONICAL PLATFORM ENTITY**

The canonical RVDB platform will represent the Sega Master System / Mark III
software and emulation platform family.

Canonical ID:

`platform.sega.master.system`

Canonical name:

`Sega Master System`

This name follows the established RVDB platform naming convention while
preserving Mark III through aliases and documentation.

---

# Canonical Aliases

Approved aliases:

- `Sega Mark III`
- `Sega Mark 3`
- `Master System / Mark III`

These aliases identify the closely related historical/emulation identities
without creating duplicate canonical entities.

Japanese Master System and Western Master System are not separate canonical
platform entities.

---

# Master System II Boundary

Sega Master System II remains part of the canonical Master System platform.

It should not become a separate RVDB platform solely because of hardware
revision.

Any meaningful hardware-specific differences may be represented later
through normalized metadata or a future hardware-variant model.

No production entity:

`platform.sega.master.system.ii`

should be created by Batch 10.

---

# Media Decision

Canonical media:

- `cartridge`

The controlled RVDB media vocabulary does not currently define a separate
Sega Card / My Card media value.

Sega's official documentation establishes that My Card Mark III software
was part of the Mark III / Master System software ecosystem.

Therefore Batch 10 will retain the existing controlled `cartridge` value
rather than expanding the media vocabulary during platform population.

No new media vocabulary is introduced.

---

# Extension Decision

Production extension:

- `sms`

Do NOT add:

- `bin`
- `rom`

solely because individual emulators accept those generic file extensions.

The RVDB extension field should represent defensible platform software-image
conventions rather than every generic filename accepted by an emulator.

Additional extensions may be reconsidered later if independent software-image
evidence justifies them.

---

# Category Decision

Canonical category:

`console`

The Master System / Mark III family is a home video game console platform.

---

# Release-Year Decision

Canonical release year:

`1985`

The canonical platform family begins with the Sega Mark III release in Japan
on 1985-10-20.

The later 1986 overseas Master System release and 1987 Japanese Master System
release are treated as regional/hardware lineage events rather than separate
canonical platform creation dates.

---

# Emulator-Core Relationships

No `supports_core` relationships will be created during Batch 10.

Core relationships remain deferred until canonical core entities and a
separate relationship-research process are available.

---

# Optional Metadata

The following remain deferred:

- `family`
- `generation`
- `regions`
- `architecture`

Regional distinctions identified during P2A11 research should not be
encoded into these fields until normalized vocabulary and schema semantics
are established.

---

# Final Entity-Boundary Decision

RVDB will use:

`platform.sega.master.system`

to represent the canonical Sega Master System / Mark III platform family.

The following will NOT be created as separate canonical platform entities:

- Sega Mark III
- Japanese Master System
- Western Master System
- Master System II

The distinctions remain documented through aliases, historical context, and
future normalized metadata/variant modeling where appropriate.

This decision is supported by:

1. Sega's own documentation grouping Mark III and Master System software.
2. Sega's documented hardware lineage between Mark III and Master System.
3. RetroArch's `Sega - Master System - Mark III` database identity.
4. Multiple Libretro cores using the same database identity.
5. Emulator support for distinct hardware modes without requiring separate
   software-platform database identities.

---

# Proposed Production Record

If this planning decision is accepted, the production record should use:

ID:

`platform.sega.master.system`

Name:

`Sega Master System`

Manufacturer:

`manufacturer.sega`

Release year:

`1985`

Category:

`console`

Media:

- `cartridge`

Extensions:

- `sms`

Relationships:

- `supports_core: []`

Optional metadata:

deferred.

---

# Production Authorization

P2A11 research requirements are satisfied.

Production YAML may be created only after the planning document itself is
committed and pushed.

The production step must remain a separate checkpoint from this planning
commit.

---

# Next Step

Commit this researched P2A11 planning checkpoint separately.

After the planning commit is pushed and verified, create the Batch 10
production YAML in a separate controlled checkpoint.

---


---


---


---


---


---

# Emulator-Core Relationships

Do not create `supports_core` relationships during Batch 10.

Required canonical core entities do not yet form part of the controlled
Batch 10 production scope.

Relationship research may be recorded separately after the platform
boundary is finalized.

---

# Optional Metadata

Do not populate speculative values for:

- `family`
- `generation`
- `regions`
- `architecture`

These remain deferred unless sufficient evidence and normalized vocabulary
exist.

---

# Entity-Boundary Decision Criteria

A separate RVDB platform entity should only be created if the distinction
materially affects one or more of:

- software compatibility
- execution environment
- hardware architecture
- software distribution format
- emulator/core compatibility
- recognized emulation-platform identity

Regional branding alone is insufficient.

Hardware revision alone is insufficient.

---

# Required Final Research Questions

Before production YAML is authorized, answer:

1. Are Mark III and Master System software sufficiently unified to justify
   one RVDB platform entity?

2. Do the Japanese and Western cartridge interfaces create a sufficiently
   meaningful platform boundary?

3. How does RetroArch classify Mark III and Master System software?

4. How do major emulation cores represent Mark III and Master System?

5. Are Mark III and Master System ROM/image extensions represented through
   a common convention?

6. Should Sega Cards / My Cards be represented as `cartridge` media?

7. Is Master System II a hardware revision or a separate emulation
   platform for RVDB purposes?

8. Should Japanese Master System remain an alias/variant rather than a
   separate entity?

9. Does the Power Base Converter represent an accessory relationship
   rather than a platform?

10. What canonical ID best preserves long-term RVDB identity?

---


---

# Production Authorization Gate

Production YAML creation requires all of the following:

- entity boundary explicitly decided
- canonical ID approved
- canonical name approved
- filesystem path approved
- manufacturer verified
- category verified
- media verified
- extensions researched
- aliases researched
- unsupported metadata explicitly deferred
- emulator-core relationships explicitly deferred or separately justified
- Batch 10 plan committed before production creation

---

# Next Step

Complete the P2A11 research review.

Then update this plan with the final entity-boundary decision.

Only after the planning commit is complete may Batch 10 production YAML
be created.
