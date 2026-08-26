# RVDB Sega Platform Batch 2 Plan

_Last Updated: 2026-08-26_

---

# Status

PLANNED — NO PRODUCTION YAML CREATED

---

# Scope

Sega Platform Batch 2 contains three platform entities:

1. Game Gear
2. Sega Saturn
3. Dreamcast

The batch deliberately avoids Master System / Mark III until their
canonical entity boundary is reviewed separately.

---

# Batch Selection Rationale

Sega is selected for Platform Population Batch 2 because:

- `manufacturer.sega` already exists
- `platform.sega.genesis` already exists
- the Sega manufacturer namespace is established
- the canonical Sega platform directory already exists
- the batch can be added without creating a new manufacturer entity

Atari remains a valid future batch candidate but currently has no
production platform entities.

---

# 1. Game Gear

Canonical ID:

`platform.sega.game.gear`

Canonical path:

`data/platforms/sega/game_gear.yaml`

Canonical name:

`Game Gear`

Aliases:

- `Sega Game Gear`

Manufacturer:

- `manufacturer.sega`

Release year:

`1990`

Category:

- `handheld`

Media:

- `cartridge`

Proposed extensions:

- `gg`

Deferred fields:

- `family`
- `generation`
- `regions`
- `architecture`

Relationships:

`supports_core` remains empty until an appropriate canonical RVDB core
entity exists.

Entity-boundary note:

Kid's Gear is not a separate platform entity solely because of branding
and minor hardware changes.

---

# 2. Sega Saturn

Canonical ID:

`platform.sega.saturn`

Canonical path:

`data/platforms/sega/saturn.yaml`

Canonical name:

`Sega Saturn`

Aliases:

- `Saturn`

Manufacturer:

- `manufacturer.sega`

Release year:

`1994`

Category:

- `console`

Media:

- `optical-disc`

Proposed extensions:

- `cue`
- `ccd`
- `chd`

Deferred fields:

- `family`
- `generation`
- `regions`
- `architecture`

Relationships:

`supports_core` remains empty until an appropriate canonical RVDB core
entity exists.

Entity-boundary note:

Licensed compatible hardware such as V-Saturn and Hi-Saturn does not
automatically create separate RVDB platform entities.

---

# 3. Dreamcast

Canonical ID:

`platform.sega.dreamcast`

Canonical path:

`data/platforms/sega/dreamcast.yaml`

Canonical name:

`Dreamcast`

Aliases:

- `Sega Dreamcast`

Manufacturer:

- `manufacturer.sega`

Release year:

`1998`

Category:

- `console`

Media:

- `optical-disc`

Proposed extensions:

- `gdi`
- `cdi`
- `chd`

Deferred fields:

- `family`
- `generation`
- `regions`
- `architecture`

Relationships:

`supports_core` remains empty until an appropriate canonical RVDB core
entity exists.

Entity-boundary note:

NAOMI, NAOMI 2, Atomiswave, and System SP are not Dreamcast platform
aliases merely because Flycast emulates them through the same core.

---

# Master System / Mark III Deferral

Master System is intentionally excluded from Sega Batch 2.

Sega's historical documentation shows a non-trivial relationship between:

- Sega Mark III
- overseas Master System / Power Base
- Japanese Master System

The Japanese Master System was an enhanced Mark III configuration, while
the overseas Master System appeared earlier and had hardware and software
format differences.

Decision:

Do not create a Master System production entity until RVDB explicitly
reviews whether Mark III and Master System should be:

- one canonical platform with aliases
- separate platform entities
- or one platform family with distinct entities

This decision must not be made implicitly during routine population work.

---

# Extension Policy

Extensions represent common platform software-image representations rather
than every file type accepted by a multi-system emulator core.

For this batch:

Game Gear:

- `gg`

Sega Saturn:

- `cue`
- `ccd`
- `chd`

Dreamcast:

- `gdi`
- `cdi`
- `chd`

Generic archive extensions such as:

- `zip`
- `7z`

are intentionally excluded.

Generic executable or subsystem formats are also excluded unless later
research establishes them as canonical platform software representations.

---

# Media Policy

The existing controlled Platform v2 media vocabulary is sufficient for
this batch.

Game Gear:

`media: [cartridge]`

Sega Saturn:

`media: [optical-disc]`

Dreamcast:

`media: [optical-disc]`

No Platform schema expansion is required for Sega Batch 2 media.

---

# Fields Intentionally Deferred

The following optional fields remain deferred:

- `family`
- `generation`
- `regions`
- `architecture`

They must not be populated merely because hardware specifications are
available.

Normalization policy must precede production use.

---

# Relationships

No new `supports_core` relationships will be invented.

The current production RVDB core catalog does not yet contain canonical
cores appropriate for Game Gear, Saturn, or Dreamcast.

These relationship lists will remain empty.

---

# Planned Production Records

The initial records should contain:

- `id`
- `type`
- `name`
- `aliases`
- `manufacturer`
- `release_year`
- `category`
- `media`
- `extensions`
- `relationships`
- minimal existing-compatible metadata where justified

No speculative optional fields should be introduced.

---

# Production Gate

Before Sega Platform Batch 2 is committed:

1. create exactly three platform YAML files
2. verify canonical IDs and paths
3. verify `manufacturer.sega` references
4. verify required categories
5. verify controlled media values
6. verify proposed extensions
7. verify no deferred fields were introduced
8. verify no unsupported relationships were introduced
9. run production validation
10. run the complete regression suite
11. regenerate the canonical bundle
12. update dataset-count regression baselines
13. inspect the complete production diff
14. commit the batch separately
15. push to `develop`

---

# Expected Entity Count

Current production entity count:

`22`

Sega Batch 2 additions:

`3`

Expected post-batch entity count:

`25`

Current platform count:

`7`

Expected post-batch platform count:

`10`

---

# Expected Canonical Graph

Current graph:

- nodes: 22
- edges: 22

Expected after Sega Batch 2:

- nodes: 25
- edges: 25

No additional relationship edges are expected because each new platform's
`supports_core` list remains empty.

---

# Next Decision

Review and approve the Sega Platform Batch 2 plan before creating:

- `data/platforms/sega/game_gear.yaml`
- `data/platforms/sega/saturn.yaml`
- `data/platforms/sega/dreamcast.yaml`

---

# Implementation Result

Status:

COMPLETE

Sega Platform Batch 2 has been implemented successfully.

Production entities created:

- `platform.sega.game.gear`
- `platform.sega.saturn`
- `platform.sega.dreamcast`

Canonical paths:

- `data/platforms/sega/game_gear.yaml`
- `data/platforms/sega/saturn.yaml`
- `data/platforms/sega/dreamcast.yaml`

The existing Sega Genesis entity remains:

- `platform.sega.genesis`
- `data/platforms/sega/genesis.yaml`

Batch 2 therefore expands the Sega platform catalog without modifying the
existing Genesis entity.

## Implemented Metadata

### Game Gear

Canonical ID:

`platform.sega.game.gear`

Canonical name:

`Game Gear`

Alias:

`Sega Game Gear`

Manufacturer:

`manufacturer.sega`

Release year:

`1990`

Category:

`handheld`

Media:

`cartridge`

Extensions:

- `gg`

### Sega Saturn

Canonical ID:

`platform.sega.saturn`

Canonical name:

`Sega Saturn`

Alias:

`Saturn`

Manufacturer:

`manufacturer.sega`

Release year:

`1994`

Category:

`console`

Media:

`optical-disc`

Extensions:

- `cue`
- `ccd`
- `chd`

### Dreamcast

Canonical ID:

`platform.sega.dreamcast`

Canonical name:

`Dreamcast`

Alias:

`Sega Dreamcast`

Manufacturer:

`manufacturer.sega`

Release year:

`1998`

Category:

`console`

Media:

`optical-disc`

Extensions:

- `gdi`
- `cdi`
- `chd`

## Deferred Metadata

The following optional Platform v2 fields remain deliberately deferred for
this batch:

- `family`
- `generation`
- `regions`
- `architecture`

No speculative values were introduced for these fields.

The `supports_core` relationship remains empty pending a separately
researched emulator-core relationship population stage.

## Dataset Result

After Sega Platform Batch 2:

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

Canonical build:

PASS

All Sega Batch 2 production entities are present in the canonical bundle.

## Batch Result

Sega Platform Batch 2 satisfies the controlled population requirements
defined by:

- `docs/platform_contract.md`
- `docs/platform_catalog_policy.md`

The batch was planned before production data creation, uses canonical
manufacturer references, follows the multi-word platform naming policy,
uses schema-controlled media values, and leaves unsupported optional
metadata unpopulated.

Sega Platform Batch 2 is ready for its production commit.
