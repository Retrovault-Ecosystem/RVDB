# RVDB Nintendo Console Platform Batch 5 Plan

Status:

PLANNED — NO PRODUCTION YAML CREATED

Phase:

Phase 2A — Platform Database Expansion

Checkpoint:

P2A6 — Platform Population Batch 5

---

# Purpose

Nintendo Console Platform Batch 5 extends the existing Nintendo production
catalog with two optical-disc console platforms:

- Nintendo GameCube
- Wii

The batch remains deliberately small and reviewable.

Production YAML must not be created until this plan is reviewed and
committed separately.

---

# Batch Scope

Manufacturer:

`manufacturer.nintendo`

Platforms:

- `platform.nintendo.gamecube`
- `platform.nintendo.wii`

Expected production paths:

- `data/platforms/nintendo/gamecube.yaml`
- `data/platforms/nintendo/wii.yaml`

Batch size:

2 platform entities

Current production entity count:

31

Current production platform count:

16

Expected post-batch entity count:

33

Expected post-batch platform count:

18

---

# Manufacturer Coverage

The canonical Nintendo manufacturer entity already exists:

`manufacturer.nintendo`

Canonical path:

`data/manufacturers/nintendo.yaml`

No new manufacturer entity is required.

Both Batch 5 platform entities will reference:

`manufacturer.nintendo`

---

# Nintendo GameCube

## Canonical Identity

Canonical ID:

`platform.nintendo.gamecube`

Canonical path:

`data/platforms/nintendo/gamecube.yaml`

Canonical name:

`Nintendo GameCube`

Justified searchable alias:

`GameCube`

## Release Year

Earliest canonical commercial release year:

`2001`

## Category

Canonical category:

`console`

## Media

Canonical media:

`optical-disc`

## Extensions

Planned conservative extension set:

- `iso`
- `gcm`
- `gcz`
- `rvz`

The extension list is intentionally conservative.

Do not automatically add every format loadable by Dolphin.

## Relationships

Planned relationship structure:

`supports_core: []`

Do not populate Dolphin or other emulator-core relationships during this
batch.

## Deferred Optional Metadata

The following fields remain omitted:

- `family`
- `generation`
- `regions`
- `architecture`

---

# Wii

## Canonical Identity

Canonical ID:

`platform.nintendo.wii`

Canonical path:

`data/platforms/nintendo/wii.yaml`

Canonical name:

`Wii`

Aliases:

none required

## Release Year

Earliest canonical commercial release year:

`2006`

## Category

Canonical category:

`console`

## Media

Canonical media:

`optical-disc`

## Extensions

Planned conservative extension set:

- `iso`
- `wbfs`
- `rvz`

Do not automatically add:

- `wad`
- executable formats
- playlist formats
- less-general container formats

## Relationships

Planned relationship structure:

`supports_core: []`

## Deferred Optional Metadata

The following fields remain omitted:

- `family`
- `generation`
- `regions`
- `architecture`

---

# Wii Hardware Revision Boundary

Batch 5 treats the following as hardware models/revisions of the canonical
Wii platform rather than separate RVDB platform entities:

- original Wii / RVL-001
- revised Wii / RVL-101
- Wii mini / RVL-201

Do not create separate platform entities for these models during Batch 5.

Future hardware-variant modeling may represent these distinctions.

---

# Wii U Boundary

Wii U is not included in Batch 5.

Wii U is a distinct Nintendo console platform and must not be represented
as a Wii hardware revision.

A future controlled population batch may create a separate canonical Wii U
entity.

---

# GameCube / Wii Entity Boundary

Nintendo GameCube and Wii remain separate canonical RVDB platform entities.

Shared Dolphin emulator support does not merge their platform identities.

Batch 5 establishes:

`platform.nintendo.gamecube`

and:

`platform.nintendo.wii`

as independent entities.

---

# Emulator-Core Deferral

Although Dolphin supports GameCube and Wii, Batch 5 does not populate
`supports_core`.

Core relationships require separately researched canonical core entities.

Both records will therefore use:

`supports_core: []`

---

# Regional Naming

Batch 5 does not introduce structured regional naming.

Aliases remain searchable alternate names only.

---

# Regional Release Information

Only earliest canonical commercial release year is recorded:

- Nintendo GameCube: 2001
- Wii: 2006

Detailed regional launch dates remain outside Batch 5.

---

# Intended GameCube Production Shape

```yaml
id: platform.nintendo.gamecube
type: platform

name: Nintendo GameCube

aliases:
  - GameCube

manufacturer:
  - manufacturer.nintendo

release_year: 2001

category:
  - console

media:
  - optical-disc

extensions:
  - iso
  - gcm
  - gcz
  - rvz

relationships:

  supports_core: []

metadata:

  retroarch_supported: true

  notes: ""
```

---

# Intended Wii Production Shape

```yaml
id: platform.nintendo.wii
type: platform

name: Wii

aliases: []

manufacturer:
  - manufacturer.nintendo

release_year: 2006

category:
  - console

media:
  - optical-disc

extensions:
  - iso
  - wbfs
  - rvz

relationships:

  supports_core: []

metadata:

  retroarch_supported: true

  notes: ""
```

---

# Contract Compliance

Batch 5 is designed to comply with:

- `docs/platform_contract.md`
- `docs/platform_catalog_policy.md`

The planned records use:

- canonical manufacturer references
- canonical manufacturer-specific IDs
- canonical manufacturer-specific paths
- controlled `console` category values
- controlled `optical-disc` media values
- conservative software-image extension lists
- empty unresolved core relationships
- no speculative optional metadata

---

# Expected Dataset Result

Current production entities:

31

Current platform entities:

16

Batch 5 additions:

2

Expected production entities after implementation:

33

Expected platform entities after implementation:

18

Expected canonical graph:

- nodes: 33
- edges: 33

---

# Explicit Batch 5 Deferrals

Batch 5 does not include:

- Wii U
- Wii hardware revisions as separate platform entities
- GameCube hardware revisions
- Nintendo DSi
- Nintendo 64DD
- Sega Master System / Mark III
- additional Atari platforms
- emulator-core relationship population
- normalized family metadata
- generation metadata
- structured regional metadata
- architecture metadata

---

# Production Gate

Do not create:

- `data/platforms/nintendo/gamecube.yaml`
- `data/platforms/nintendo/wii.yaml`

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
3. create GameCube production YAML
4. create Wii production YAML
5. validate Platform v2 structure
6. verify manufacturer relationships
7. update affected dataset baselines
8. run the complete regression suite
9. run production validation
10. rebuild `rvdb.bundle.json`
11. verify 33 nodes / 33 edges
12. append implementation results to this document
13. review the full production diff
14. commit production separately
15. push production commit to `develop`
16. update `docs/current_milestone.md` separately

---

# Next Checkpoint

Review and approve the Nintendo Console Platform Batch 5 plan.

If approved:

P2A6D — Commit Nintendo Console Batch 5 Plan

No production YAML should exist before that commit.
