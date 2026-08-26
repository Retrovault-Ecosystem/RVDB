# RVDB Nintendo Platform Batch 1 Plan

_Last Updated: 2026-08-26_

---

# Status

COMPLETE — PRODUCTION BATCH IMPLEMENTED

---

# Scope

Nintendo Platform Batch 1 contains three platform entities:

1. Nintendo 64
2. Game Boy
3. Game Boy Color

The batch deliberately remains small so canonical identity, metadata
quality, validation behavior, and commit cadence can be verified before
larger platform population begins.

---

# Evidence Policy

Canonical records must use verified information rather than mechanically
copying one external catalog.

Primary factual evidence for this batch comes from:

- Nintendo corporate history
- Nintendo historical hardware/support documentation
- Nintendo product documentation
- current Libretro documentation for common emulation file extensions

Optional RVDB fields are omitted when a normalized RVDB representation has
not yet been finalized.

---

# 1. Nintendo 64

Canonical ID:

`platform.nintendo.n64`

Canonical path:

`data/platforms/nintendo/n64.yaml`

Canonical name:

`Nintendo 64`

Aliases:

- `N64`

Manufacturer:

- `manufacturer.nintendo`

Release year:

`1996`

Category:

- `console`

Verified media candidate:

- `cartridge`

Proposed RVDB extensions:

- `n64`
- `v64`
- `z64`

Deferred fields:

- `family`
- `generation`
- `regions`
- `architecture`

Relationships:

`supports_core` remains empty until an appropriate canonical RVDB core
entity exists.

Notes:

Libretro core support for Transfer Pak `.gb` content does not make `.gb`
a Nintendo 64 platform extension.

64DD `.ndd` content is not included in this Nintendo 64 record because
64DD platform identity requires separate entity-boundary review.

---

# 2. Game Boy

Canonical ID:

`platform.nintendo.game.boy`

Canonical path:

`data/platforms/nintendo/game_boy.yaml`

Canonical name:

`Game Boy`

Aliases:

None required for the initial canonical record.

Manufacturer:

- `manufacturer.nintendo`

Release year:

`1989`

Category:

- `handheld`

Verified media candidate:

- `cartridge`

Proposed RVDB extensions:

- `gb`

Deferred fields:

- `family`
- `generation`
- `regions`
- `architecture`

Relationships:

`supports_core` remains empty until an appropriate canonical RVDB core
entity exists.

Entity-boundary decision:

Game Boy Pocket and cosmetic Game Boy revisions are not separate platform
entities solely because of case size, styling, or hardware revision.

---

# 3. Game Boy Color

Canonical ID:

`platform.nintendo.game.boy.color`

Canonical path:

`data/platforms/nintendo/game_boy_color.yaml`

Canonical name:

`Game Boy Color`

Aliases:

None required for the initial canonical record.

Manufacturer:

- `manufacturer.nintendo`

Release year:

`1998`

Category:

- `handheld`

Verified media candidate:

- `cartridge`

Proposed RVDB extensions:

- `gbc`

Deferred fields:

- `family`
- `generation`
- `regions`
- `architecture`

Relationships:

`supports_core` remains empty until an appropriate canonical RVDB core
entity exists.

Entity-boundary decision:

Game Boy Color remains a distinct platform entity because it has its own
hardware capabilities and platform-specific software while retaining
backward compatibility with original Game Boy software.

---

# Fields Intentionally Deferred

## generation

Generation numbering is not sufficiently canonical for this batch and is
not required by Platform Entity Contract v2.

Do not populate it merely from conventional console-generation labels.

## regions

Region values remain deferred until RVDB defines a normalized region
vocabulary.

## architecture

Hardware specifications are known, but RVDB has not yet finalized a
canonical architecture vocabulary.

Raw descriptions such as processor bit width must not be substituted for
normalized architecture identifiers.

## family

Family classification remains optional.

Do not introduce family strings until a reusable normalized family policy
is established.

---

# Media Vocabulary Result

Nintendo documentation establishes cartridge/Game Pak media for all three
systems.

Canonical normalized value:

`cartridge`

P2A2G resolved the Platform v2 media-vocabulary gate.

The Platform schema now controls media values through `list.items.enum`.

Initial canonical media vocabulary:

- `cartridge`
- `floppy`
- `optical-disc`
- `cassette`
- `digital`

Decision:

Nintendo Batch 1 may populate:

`media: [cartridge]`

for Nintendo 64, Game Boy, and Game Boy Color.

---

# Extensions Policy

Extensions represent common platform software-image representations.

For this batch:

Nintendo 64:

- `n64`
- `v64`
- `z64`

Game Boy:

- `gb`

Game Boy Color:

- `gbc`

Generic or cross-platform extensions should not be added merely because a
particular emulator core can load them.

Peripheral/subsystem content must not be confused with the platform's
ordinary software-image extensions.

---

# Relationships

No new `supports_core` relationships will be invented.

The current production RVDB core catalog contains only the existing
Foundation core entities.

Nintendo Batch 1 platforms will retain empty `supports_core` lists until
matching canonical core entities are added and validated.

---

# Planned Production Records

The initial records should contain only:

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

Deferred optional fields must remain omitted.

---

# Production Gate

Before Nintendo Batch 1 is committed:

1. create exactly three platform YAML files
2. verify canonical IDs and paths
3. verify manufacturer references
4. verify required categories
5. verify controlled media values
6. verify proposed extensions
7. verify no speculative optional fields were introduced
8. run production validation
9. run the complete regression suite
10. build the canonical bundle
11. inspect the exact production diff
12. commit the batch separately
13. push to `develop`

---

# Expected Entity Count

Current production entity count:

`19`

Nintendo Batch 1 additions:

`3`

Expected post-batch entity count:

`22`

Current platform count:

`4`

Expected post-batch platform count:

`7`

---

# Completion Result

Nintendo Platform Batch 1 is implemented.

Production entities added:

- `platform.nintendo.n64`
- `platform.nintendo.game.boy`
- `platform.nintendo.game.boy.color`

Production paths:

- `data/platforms/nintendo/n64.yaml`
- `data/platforms/nintendo/game_boy.yaml`
- `data/platforms/nintendo/game_boy_color.yaml`

Final verification baseline:

- production entities: 22
- valid entities: 22
- platform entities: 7
- schema errors: 0
- relationship errors: 0
- regression suite: 145 passed
- canonical graph nodes: 22
- canonical graph edges: 22
- canonical bundle build: PASS

Deferred fields remain omitted:

- `family`
- `generation`
- `regions`
- `architecture`

No unsupported `supports_core` relationships were introduced.

Next:

Select and research the next controlled Phase 2A platform population batch.
