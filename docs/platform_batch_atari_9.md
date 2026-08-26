# RVDB Atari 8-bit Computer Platform Batch 9 Plan

## Status

PLANNED — NOT YET IMPLEMENTED

Phase:

Phase 2A — Platform Database Expansion

Checkpoint:

P2A10 — Platform Population Batch 9

---

# Purpose

Atari Platform Batch 9 introduces one canonical Atari computer-family
platform entity:

- Atari 8-bit Computers

The batch models the compatible Atari 8-bit computer lineage as one
canonical RVDB platform rather than creating separate production
entities for each hardware model.

No production platform YAML is created by this planning checkpoint.

---

# Batch Scope

Manufacturer:

`manufacturer.atari`

Canonical platform:

`platform.atari.8.bit.computers`

Canonical production path:

`data/platforms/atari/8_bit_computers.yaml`

Canonical name:

`Atari 8-bit Computers`

Batch size:

1 platform entity

Current production entities:

37

Current platform entities:

22

Expected post-batch production entities:

38

Expected post-batch platform entities:

23

Expected post-batch graph:

- nodes: 38
- edges: 38

---

# Manufacturer Coverage

The canonical Atari manufacturer entity already exists:

`manufacturer.atari`

Canonical manufacturer path:

`data/manufacturers/atari.yaml`

No new manufacturer entity is required.

---

# Canonical Platform Identity

## Canonical Name

`Atari 8-bit Computers`

## Canonical ID

`platform.atari.8.bit.computers`

The ID is generated directly by the canonical RVDB `IDGenerator` from
the canonical platform name.

Generator result:

```text
Atari 8-bit Computers
-> platform.atari.8.bit.computers
```

## Canonical Path

`data/platforms/atari/8_bit_computers.yaml`

The filesystem path follows the existing multi-word platform filename
convention using underscores.

## Manufacturer

`manufacturer.atari`

## Earliest Commercial Release Year

`1979`

The earliest production hardware represented by this family is the
original Atari 400/800 generation.

## Category

`computer`

This value already exists in the controlled Platform v2 category
vocabulary.

## Media

The canonical Atari 8-bit computer family uses the following controlled
media values:

- `cartridge`
- `floppy`
- `cassette`

All three values already exist in the controlled Platform v2 media
vocabulary.

## Conservative Software-Image Extensions

Approved initial extension set:

- `atr`
- `xfd`
- `atx`
- `cas`

The extension set is deliberately conservative.

The following formats are not included in the initial production record:

- `a52`
- `bin`
- `xex`
- `zip`
- `cdm`

Reasons:

- `a52` is reserved for the separate Atari 5200 platform.
- `bin` is too generic to serve as a controlled Atari 8-bit family image
  format.
- `xex` represents executable content rather than a disk or cassette image.
- `zip` is an archive/container format rather than a native platform image.
- `cdm` remains deferred pending stronger format-policy evidence.

## Emulator-Core Relationships

Initial relationship shape:

```yaml
relationships:
  supports_core: []
```

No emulator-core relationships are populated during Batch 9.

Core relationships may be added only after the required canonical core
entities exist and those relationships have been researched separately.

## Deferred Optional Metadata

The following optional fields remain omitted unless separately normalized
and justified:

- `family`
- `generation`
- `regions`
- `architecture`

No speculative normalization is introduced merely to make the production
record appear more complete.

---

# Atari 8-bit Family Boundary

Batch 9 represents the compatible Atari 8-bit computer lineage as one
canonical RVDB platform entity.

The family boundary includes:

- Atari 400
- Atari 800
- Atari 1200XL
- Atari 600XL
- Atari 800XL
- Atari 65XE
- Atari 130XE
- Atari 800XE
- Atari XEGS

These systems are modeled as members of one canonical software-platform
family rather than as separate production platform entities.

Batch 9 therefore creates only:

`platform.atari.8.bit.computers`

---

# XEGS Boundary Decision

Atari XEGS is included inside the Atari 8-bit computer-family boundary.

Batch 9 must not create a separate XEGS production platform.

Do not create:

- `platform.atari.xegs`
- `platform.atari.xe.game.system`
- `data/platforms/atari/xegs.yaml`
- `data/platforms/atari/xe_game_system.yaml`

XEGS marketing as a game system does not, by itself, establish a separate
canonical RVDB software-platform boundary.

The XEGS remains represented through:

`platform.atari.8.bit.computers`

---

# Atari 5200 Boundary

Atari 5200 remains a separate canonical platform:

`platform.atari.5200`

Batch 9 must not merge Atari 5200 software or metadata into the Atari 8-bit
computer-family record.

In particular:

- do not add `a52` to the Atari 8-bit Computers extension set
- do not treat Atari 5200 as an alias
- do not merge Atari 5200 cartridge identity into the computer family

---

# Intended Production Shape

The intended production record is:

```yaml
id: platform.atari.8.bit.computers
type: platform

name: Atari 8-bit Computers

aliases: []

manufacturer:
  - manufacturer.atari

release_year: 1979

category:
  - computer

media:
  - cartridge
  - floppy
  - cassette

extensions:
  - atr
  - xfd
  - atx
  - cas

relationships:

  supports_core: []

metadata:

  retroarch_supported: true

  notes: ""
```

The exact production file must still pass schema validation, relationship
validation, regression tests, and the canonical build before commit.

---

# Production Acceptance Criteria

Batch 9 production implementation is acceptable only if all of the
following are true:

1. Atari 8-bit Computers exists exactly once as
   `platform.atari.8.bit.computers`.
2. the production path is
   `data/platforms/atari/8_bit_computers.yaml`.
3. the canonical name is `Atari 8-bit Computers`.
4. the record references `manufacturer.atari`.
5. the earliest commercial release year is `1979`.
6. the category is `computer`.
7. the media values are `cartridge`, `floppy`, and `cassette`.
8. the initial extension set is `atr`, `xfd`, `atx`, and `cas`.
9. `a52` remains exclusive to the Atari 5200 record.
10. `bin`, `xex`, `zip`, and `cdm` remain excluded or deferred.
11. `supports_core` remains empty unless separately researched.
12. unsupported optional metadata remains deferred.
13. Atari XEGS is not created as a separate production platform.
14. Atari 5200 remains a separate canonical platform.
15. the family boundary is not expanded beyond the approved Atari 8-bit
    computer lineage.
16. schema validation passes.
17. relationship validation passes.
18. the complete regression suite passes.
19. the canonical build succeeds.
20. production entity count becomes 38.
21. platform entity count becomes 23.
22. graph node count becomes 38.
23. graph edge count becomes 38.
24. only the intended Batch 9 working set is committed.

---

# Expected Dataset Result

Current production entities:

37

Current platform entities:

22

Batch 9 additions:

1

Expected production entities after implementation:

38

Expected platform entities after implementation:

23

Expected canonical graph:

- nodes: 38
- edges: 38

The exact regression test count must be recorded from the implementation
result.

---

# Explicit Batch 9 Deferrals

Batch 9 does not include:

- a separate Atari XEGS platform entity
- Atari Jaguar CD
- Atari STE
- Atari TT
- Atari Falcon
- modern Atari VCS
- Atari arcade hardware families
- Nintendo DSi
- Sega Master System / Mark III
- emulator-core relationship population
- normalized family metadata
- generation metadata
- structured regional metadata
- architecture metadata

The following Atari 8-bit software formats remain excluded or deferred:

- `a52`
- `bin`
- `xex`
- `zip`
- `cdm`

---

# Production Gate

Do not create:

- `data/platforms/atari/8_bit_computers.yaml`

until this plan has been:

1. reviewed
2. checked against the current platform contract
3. committed separately
4. pushed to `develop`

Do not create separate XEGS production YAML during Batch 9.

---

# Planned Production Sequence

After plan approval:

1. commit this plan only
2. push the plan commit to `develop`
3. verify a clean production baseline
4. create `data/platforms/atari/8_bit_computers.yaml`
5. verify separate XEGS production files remain absent
6. verify Atari 5200 remains distinct
7. validate Platform v2 structure
8. verify the Atari manufacturer relationship
9. run targeted platform-contract tests
10. run production validation
11. rebuild `rvdb.bundle.json`
12. verify 38 production entities
13. verify 23 platform entities
14. verify 38 graph nodes
15. verify 38 graph edges
16. run the complete regression suite
17. discover any stale count-sensitive test baselines
18. update only baselines directly affected by the new entity
19. rerun targeted affected tests
20. rerun the complete regression suite
21. rerun production validation
22. rerun the canonical build
23. append the implementation result to this document
24. review the complete Batch 9 production diff
25. commit production separately
26. push production to `develop`
27. update `docs/current_milestone.md` separately

---

# Next Checkpoint

Review and approve the Atari 8-bit Computer Platform Batch 9 plan.

If approved:

P2A10F — Commit Atari 8-bit Computer Platform Batch 9 Plan

No Batch 9 production YAML should exist before that commit.
