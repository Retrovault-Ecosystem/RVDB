# RVDB Nintendo Wii U Platform Batch 6 Plan

Status:

PLANNED — NO PRODUCTION YAML CREATED

Phase:

Phase 2A — Platform Database Expansion

Checkpoint:

P2A7 — Platform Population Batch 6

---

# Purpose

Nintendo Platform Batch 6 introduces Wii U as a separate canonical RVDB
platform entity.

Batch 6 contains exactly one platform:

- Wii U

The one-platform scope is deliberate because Wii U has already been
identified as a distinct platform boundary from Wii and should be reviewed
independently.

Production YAML must not be created until this plan is reviewed and
committed separately.

---

# Batch Scope

Manufacturer:

`manufacturer.nintendo`

Platform:

`platform.nintendo.wii.u`

Canonical production path:

`data/platforms/nintendo/wii_u.yaml`

Batch size:

1 platform entity

Current production entity count:

33

Current production platform count:

18

Expected post-batch entity count:

34

Expected post-batch platform count:

19

Expected post-batch canonical graph:

- nodes: 34
- edges: 34

---

# Manufacturer Coverage

The canonical Nintendo manufacturer entity already exists:

`manufacturer.nintendo`

Canonical manufacturer path:

`data/manufacturers/nintendo.yaml`

No new manufacturer entity is required.

The Wii U production record will reference:

`manufacturer.nintendo`

---

# Canonical Identity

Canonical ID:

`platform.nintendo.wii.u`

Canonical path:

`data/platforms/nintendo/wii_u.yaml`

Canonical name:

`Wii U`

Aliases:

none required

The multi-segment canonical ID follows the existing Nintendo namespace
precedent used by entities such as:

- `platform.nintendo.game.boy`
- `platform.nintendo.game.boy.color`
- `platform.nintendo.game.boy.advance`

The filesystem representation uses `wii_u.yaml` so the multi-segment
system name remains readable without introducing an additional directory
level.

---

# Wii / Wii U Entity Boundary

Wii U is a separate canonical platform from Wii.

Do not merge Wii U into:

`platform.nintendo.wii`

The separate entity is justified by meaningful differences in:

- platform identity
- hardware architecture
- software compatibility
- execution environment
- software distribution conventions
- emulator compatibility

Batch 6 therefore creates one independent Wii U platform entity.

---

# Release Year

Earliest canonical commercial release year:

`2012`

Detailed regional launch dates remain outside Batch 6.

---

# Category

Canonical category:

`console`

This value already exists in the controlled Platform v2 category
vocabulary.

---

# Media

Canonical media:

`optical-disc`

This value already exists in the controlled Platform v2 media vocabulary.

Batch 6 does not introduce a new media enum value.

---

# Extensions

Planned conservative extension set:

- `wud`
- `wux`
- `wua`

These extensions represent Wii U disc-image/archive representations used
in the current emulation ecosystem.

The extension list is intentionally conservative.

The following is explicitly deferred:

- `rpx`

RPX represents executable content inside an extracted Wii U title layout
rather than a standalone canonical game-image/archive representation for
the purpose of this initial platform record.

Other emulator-loadable file types must not be added automatically.

---

# Relationships

Planned relationship structure:

`supports_core: []`

Do not populate emulator/core relationships during Batch 6.

Core relationships require separately researched canonical core entities
and relationship work.

---

# Deferred Optional Metadata

The following optional Platform v2 fields remain omitted:

- `family`
- `generation`
- `regions`
- `architecture`

No speculative values will be introduced.

---

# Hardware Revision Boundary

Batch 6 creates only the canonical Wii U platform entity.

Hardware models, storage-capacity configurations, regional bundles, and
cosmetic revisions must not become separate platform entities solely
because they represent different retail hardware configurations.

Hardware revision alone is insufficient to establish a new canonical RVDB
platform entity.

---

# Regional Naming

Batch 6 does not introduce structured regional naming.

No aliases are required merely to duplicate the Nintendo manufacturer name.

---

# Intended Production Shape

```yaml
id: platform.nintendo.wii.u
type: platform

name: Wii U

aliases: []

manufacturer:
  - manufacturer.nintendo

release_year: 2012

category:
  - console

media:
  - optical-disc

extensions:
  - wud
  - wux
  - wua

relationships:

  supports_core: []

metadata:

  retroarch_supported: true

  notes: ""
```

---

# Contract Compliance

Batch 6 is designed to comply with:

- `docs/platform_contract.md`
- `docs/platform_catalog_policy.md`

The planned record uses:

- a canonical Nintendo manufacturer reference
- a canonical manufacturer-specific multi-segment ID
- a deterministic manufacturer-specific filesystem path
- the controlled `console` category
- the controlled `optical-disc` media value
- a conservative extension list
- an empty unresolved core relationship
- no speculative optional metadata

---

# Explicit Batch 6 Deferrals

Batch 6 does not include:

- Nintendo DSi
- Nintendo 64DD
- additional Wii hardware revisions
- Sega Master System / Mark III
- additional Atari platforms
- emulator-core relationship population
- normalized family metadata
- generation metadata
- structured regional metadata
- architecture metadata
- RPX as a canonical platform extension

---

# Production Gate

Do not create:

`data/platforms/nintendo/wii_u.yaml`

until this plan has been:

1. reviewed
2. validated against current policy
3. committed separately
4. pushed to `develop`

---

# Planned Production Sequence

After plan approval:

1. commit this plan only
2. push the plan commit to `develop`
3. create Wii U production YAML
4. verify Platform v2 structure
5. verify the Nintendo manufacturer relationship
6. update affected dataset baselines
7. run the complete regression suite
8. run production validation
9. rebuild `rvdb.bundle.json`
10. verify 34 nodes / 34 edges
11. append implementation results to this document
12. review the complete production diff
13. commit production separately
14. push the production commit to `develop`
15. update `docs/current_milestone.md` separately

---

# Next Checkpoint

Review and approve the Nintendo Wii U Platform Batch 6 plan.

If approved:

P2A7E — Commit Nintendo Wii U Batch 6 Plan

No Wii U production YAML should exist before that commit.
