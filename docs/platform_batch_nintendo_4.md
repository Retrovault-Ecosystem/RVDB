# RVDB Nintendo Handheld Platform Batch 4 Plan

_Last Updated: 2026-08-26_

---

# Status

PLANNED — NO PRODUCTION YAML CREATED

---

# Scope

Nintendo Platform Batch 4 contains three handheld platform entities:

1. Game Boy Advance
2. Nintendo DS
3. Nintendo 3DS

This batch extends the existing Nintendo handheld lineage beyond:

- Game Boy
- Game Boy Color

without introducing a new manufacturer or requiring schema expansion.

---

# Batch Selection Rationale

Nintendo handhelds are selected for Platform Population Batch 4 because:

- `manufacturer.nintendo` already exists
- Nintendo already has canonical platform coverage
- Game Boy and Game Boy Color already establish the handheld namespace
- all three selected systems are handheld platforms
- all three use cartridge or game-card physical media
- the existing `handheld` category supports the batch
- the existing `cartridge` media vocabulary supports the batch
- the selected systems have clear canonical identities
- no new schema vocabulary is required

The batch deliberately avoids reopening Sega Master System / Mark III.

Additional Atari families remain available for later controlled batches.

---

# 1. Game Boy Advance

Canonical ID:

`platform.nintendo.game.boy.advance`

Canonical path:

`data/platforms/nintendo/game_boy_advance.yaml`

Canonical name:

`Game Boy Advance`

Aliases:

- `GBA`

Manufacturer:

- `manufacturer.nintendo`

Release year:

`2001`

Category:

- `handheld`

Media:

- `cartridge`

Proposed extensions:

- `gba`

Deferred fields:

- `family`
- `generation`
- `regions`
- `architecture`

Relationships:

`supports_core` remains empty until an appropriate canonical RVDB core
entity exists.

Entity-boundary note:

Game Boy Advance SP and Game Boy micro are hardware revisions within the
Game Boy Advance software platform and do not automatically become
separate RVDB platform entities.

Extension policy:

`.gba` is retained as the narrow platform-specific software-image
extension.

Generic or emulator-specific alternatives are intentionally omitted.

---

# 2. Nintendo DS

Canonical ID:

`platform.nintendo.ds`

Canonical path:

`data/platforms/nintendo/ds.yaml`

Canonical name:

`Nintendo DS`

Aliases:

- `NDS`

Manufacturer:

- `manufacturer.nintendo`

Release year:

`2004`

Category:

- `handheld`

Media:

- `cartridge`

Proposed extensions:

- `nds`

Deferred fields:

- `family`
- `generation`
- `regions`
- `architecture`

Relationships:

`supports_core` remains empty until an appropriate canonical RVDB core
entity exists.

Entity-boundary note:

Nintendo DS Lite is treated as a hardware revision of the Nintendo DS
software platform and does not become a separate RVDB platform entity.

Nintendo DSi is intentionally excluded from this batch because its
platform boundary requires separate review.

DSi introduces system capabilities and DSiWare behavior beyond the
original Nintendo DS hardware line.

Decision:

Do not create `platform.nintendo.dsi` during Batch 4.

Review DSi separately before deciding whether it is:

- a separate platform entity
- a DS-family platform variant
- or metadata within a future normalized family model

Extension policy:

`.nds` is retained as the canonical Nintendo DS software-image extension.

Formats associated specifically with DSi mode are not added to the
Nintendo DS record during this batch.

---

# 3. Nintendo 3DS

Canonical ID:

`platform.nintendo.3ds`

Canonical path:

`data/platforms/nintendo/3ds.yaml`

Canonical name:

`Nintendo 3DS`

Aliases:

- `3DS`

Manufacturer:

- `manufacturer.nintendo`

Release year:

`2011`

Category:

- `handheld`

Media:

- `cartridge`

Proposed extensions:

- `3ds`

Deferred fields:

- `family`
- `generation`
- `regions`
- `architecture`

Relationships:

`supports_core` remains empty until an appropriate canonical RVDB core
entity exists.

Entity-boundary note:

Nintendo 2DS, New Nintendo 3DS, New Nintendo 3DS XL, and New Nintendo 2DS
XL belong to the broader Nintendo 3DS family.

They must not automatically become separate RVDB platform entities merely
because emulator configuration can select different hardware models.

Any future split requires a separate technical and compatibility boundary
review.

Extension policy:

`.3ds` is retained as the narrow canonical cartridge-image extension for
the initial platform record.

The following emulator-loadable formats are intentionally omitted:

- `3dsx`
- `elf`
- `axf`
- `cci`
- `cxi`
- `app`

Those formats describe executable, container, development, or installed
software representations and should not be introduced merely because an
emulator accepts them.

---

# Canonical Naming Policy

Game Boy Advance extends the existing multi-segment Game Boy namespace.

Canonical ID:

`platform.nintendo.game.boy.advance`

Canonical path:

`data/platforms/nintendo/game_boy_advance.yaml`

Nintendo DS uses the stable product abbreviation as its terminal namespace:

`platform.nintendo.ds`

Canonical path:

`data/platforms/nintendo/ds.yaml`

Nintendo 3DS likewise uses the canonical product identifier:

`platform.nintendo.3ds`

Canonical path:

`data/platforms/nintendo/3ds.yaml`

Existing Nintendo IDs remain unchanged.

---

# Media Policy

All three selected systems use the existing Platform v2 controlled media
value:

`cartridge`

Nintendo's terminology differs by generation:

- Game Boy Advance software uses Game Paks
- Nintendo DS software uses Game Cards
- Nintendo 3DS software uses Game Cards

RVDB normalizes all three physical solid-state removable game-media forms
to:

`cartridge`

No schema change is required.

---

# Extension Policy

Platform-specific extensions are preferred over broad emulator-supported
format lists.

Planned extensions:

Game Boy Advance:

- `gba`

Nintendo DS:

- `nds`

Nintendo 3DS:

- `3ds`

Generic archive formats are excluded.

Executable, development, installed-content, and emulator-specific
container formats are also excluded unless future policy establishes them
as canonical platform software-image representations.

---

# Fields Intentionally Deferred

The following optional Platform v2 fields remain deferred:

- `family`
- `generation`
- `regions`
- `architecture`

No values should be populated simply because technical specifications are
available.

Normalization policy must precede production use.

---

# Relationships

No `supports_core` relationships will be invented.

Although emulator implementations exist for all three systems, the
necessary canonical RVDB core entities do not currently exist.

Production records therefore use:

`supports_core: []`

until a separately researched core-population stage.

---

# Explicitly Deferred Nintendo Boundaries

Batch 4 does not create separate entities for:

- Game Boy Advance SP
- Game Boy micro
- Nintendo DS Lite
- Nintendo DSi
- Nintendo DSi XL
- Nintendo 2DS
- New Nintendo 3DS
- New Nintendo 3DS XL
- New Nintendo 2DS XL

Hardware revision alone is not sufficient to create a new canonical RVDB
platform entity.

Nintendo DSi specifically remains an explicit future boundary decision.

---

# Planned Production Records

Each production record should initially contain:

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

Deferred optional fields remain omitted.

---

# Production Gate

Before Nintendo Platform Batch 4 is committed:

1. create exactly three Nintendo platform YAML files
2. verify canonical IDs
3. verify canonical paths
4. verify `manufacturer.nintendo` references
5. verify `handheld` category values
6. verify controlled `cartridge` media values
7. verify platform-specific extensions
8. verify deferred fields remain omitted
9. verify unsupported relationships remain empty
10. verify no DSi entity was introduced
11. run production validation
12. run the complete regression suite
13. regenerate the canonical bundle
14. update dataset-count regression baselines
15. inspect the complete production diff
16. align this batch document with implementation results
17. commit the production batch separately
18. push to `develop`

---

# Expected Entity Count

Current production entity count:

`28`

Nintendo Batch 4 additions:

`3`

Expected post-batch entity count:

`31`

Current platform count:

`13`

Expected post-batch platform count:

`16`

---

# Expected Canonical Graph

Current graph:

- nodes: 28
- edges: 28

Expected after Nintendo Batch 4:

- nodes: 31
- edges: 31

No additional relationship edges are expected because all three
`supports_core` lists remain empty.

---

# Next Decision

Review and approve the Nintendo Handheld Platform Batch 4 plan before
creating:

- `data/platforms/nintendo/game_boy_advance.yaml`
- `data/platforms/nintendo/ds.yaml`
- `data/platforms/nintendo/3ds.yaml`

No Batch 4 production YAML should exist before the planning checkpoint is
committed.

---

# Implementation Result

Status:

COMPLETE

Nintendo Handheld Platform Batch 4 has been implemented successfully.

Production entities created:

- `platform.nintendo.game.boy.advance`
- `platform.nintendo.ds`
- `platform.nintendo.3ds`

Canonical paths:

- `data/platforms/nintendo/game_boy_advance.yaml`
- `data/platforms/nintendo/ds.yaml`
- `data/platforms/nintendo/3ds.yaml`

This extends Nintendo's production handheld platform coverage from the
Game Boy and Game Boy Color lineage through the Game Boy Advance,
Nintendo DS, and Nintendo 3DS.

## Implemented Metadata

### Game Boy Advance

Canonical ID:

`platform.nintendo.game.boy.advance`

Canonical name:

`Game Boy Advance`

Alias:

`GBA`

Manufacturer:

`manufacturer.nintendo`

Release year:

`2001`

Category:

`handheld`

Media:

`cartridge`

Extension:

- `gba`

### Nintendo DS

Canonical ID:

`platform.nintendo.ds`

Canonical name:

`Nintendo DS`

Alias:

`NDS`

Manufacturer:

`manufacturer.nintendo`

Release year:

`2004`

Category:

`handheld`

Media:

`cartridge`

Extension:

- `nds`

### Nintendo 3DS

Canonical ID:

`platform.nintendo.3ds`

Canonical name:

`Nintendo 3DS`

Alias:

`3DS`

Manufacturer:

`manufacturer.nintendo`

Release year:

`2011`

Category:

`handheld`

Media:

`cartridge`

Extension:

- `3ds`

## Explicit Nintendo DSi Boundary

Nintendo DSi remains deliberately outside Batch 4.

No production entity was created at:

`data/platforms/nintendo/dsi.yaml`

No canonical ID was introduced for Nintendo DSi.

Nintendo DSi requires a separate entity-boundary decision before any
production representation is added.

This preserves the boundary established during Batch 4 planning and avoids
silently treating Nintendo DSi as either:

- merely an alias of Nintendo DS
- automatically a separate canonical platform

without explicit research and policy review.

## Deferred Metadata

The following optional Platform v2 fields remain deliberately omitted:

- `family`
- `generation`
- `regions`
- `architecture`

No speculative values were introduced.

The `supports_core` relationship remains empty for all three new platforms
pending a separately researched Nintendo core-population stage.

## Dataset Result

After Nintendo Handheld Platform Batch 4:

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

Canonical build:

PASS

All Nintendo Handheld Batch 4 entities are present in the canonical bundle.

Nintendo DSi remains absent as required by the Batch 4 boundary.

## Batch Result

Nintendo Handheld Platform Batch 4 satisfies the controlled population
requirements defined by:

- `docs/platform_contract.md`
- `docs/platform_catalog_policy.md`

The batch:

- was planned before production creation
- uses canonical `manufacturer.nintendo` references
- follows the approved Nintendo platform IDs
- follows canonical Nintendo filesystem paths
- uses the controlled `handheld` category
- uses the controlled `cartridge` media value
- uses platform-specific software-image extensions
- leaves unsupported optional metadata omitted
- introduces no unsupported core relationships
- preserves the explicit Nintendo DSi boundary

Nintendo Handheld Platform Batch 4 is ready for its production commit.
