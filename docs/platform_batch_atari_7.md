# RVDB Atari Platform Batch 7 Plan

## Status

PLANNED — NOT YET IMPLEMENTED

This document defines the controlled Phase 2A population plan for Atari
Platform Batch 7.

No production platform YAML is created by this planning checkpoint.

---

# Scope

Atari Platform Batch 7 introduces two additional canonical Atari platform
entities:

- Atari Lynx
- Atari Jaguar

The batch deliberately remains small.

Both platforms have clear canonical identities and can be modeled using the
existing RVDB platform contract without introducing new schema vocabulary.

Atari Jaguar CD is explicitly excluded pending a separate entity-boundary
decision.

---

# Batch Baseline

Repository baseline before Batch 7 production:

- production entities: 34
- platform entities: 19
- graph nodes: 34
- graph edges: 34
- regression tests: 145 passing
- validation errors: 0
- relationship errors: 0

Expected baseline after Batch 7 production:

- production entities: 36
- platform entities: 21
- graph nodes: 36
- graph edges: 36

Batch additions:

- 2 platform entities

---

# Manufacturer

Both Batch 7 entities reference the existing canonical manufacturer:

`manufacturer.atari`

Production manufacturer record:

`data/manufacturers/atari.yaml`

No new manufacturer entity is required.

---

# Canonical Platform 1 — Atari Lynx

## Canonical ID

`platform.atari.lynx`

## Canonical Path

`data/platforms/atari/lynx.yaml`

## Canonical Name

`Atari Lynx`

## Aliases

No alias is required for the initial production record.

Aliases must not be invented solely to populate the field.

## Manufacturer

`manufacturer.atari`

## Earliest Commercial Release Year

`1989`

## Category

`handheld`

This value already exists in the controlled platform category vocabulary.

## Media

`cartridge`

This value already exists in the controlled platform media vocabulary.

## Conservative Software-Image Extensions

Initial controlled extension set:

- `lnx`

The extension set is intentionally conservative.

Additional executable, headerless, emulator-specific, archive, or
container formats must not be added without separate evidence and review.

## Emulator-Core Relationships

Initial relationship shape:

```yaml
relationships:
  supports_core: []
```

No emulator-core relationships are invented during platform population.

They may be added only after canonical core entities exist and the
relationships have been researched independently.

## Optional Metadata

Do not populate unsupported or insufficiently normalized values for:

- `family`
- `generation`
- `regions`
- `architecture`

---

# Canonical Platform 2 — Atari Jaguar

## Canonical ID

`platform.atari.jaguar`

## Canonical Path

`data/platforms/atari/jaguar.yaml`

## Canonical Name

`Atari Jaguar`

## Aliases

No alias is required for the initial production record.

Aliases must not be invented solely to populate the field.

## Manufacturer

`manufacturer.atari`

## Earliest Commercial Release Year

`1993`

## Category

`console`

This value already exists in the controlled platform category vocabulary.

## Media

`cartridge`

Only the cartridge media of the base Atari Jaguar platform is represented
in Batch 7.

Jaguar CD optical-disc media must not be merged into this record.

## Conservative Software-Image Extensions

Initial controlled extension set:

- `jag`
- `j64`

The extension set is intentionally conservative.

Additional executable, raw dump, optical-disc, archive, or
emulator-specific formats require separate evidence and review.

## Emulator-Core Relationships

Initial relationship shape:

```yaml
relationships:
  supports_core: []
```

No emulator-core relationships are invented during platform population.

They may be added only after canonical core entities exist and the
relationships have been researched independently.

## Optional Metadata

Do not populate unsupported or insufficiently normalized values for:

- `family`
- `generation`
- `regions`
- `architecture`

---

# Atari Jaguar / Jaguar CD Entity Boundary

Atari Jaguar CD is deliberately outside Batch 7.

Batch 7 must not create:

`platform.atari.jaguar.cd`

and must not create:

`data/platforms/atari/jaguar_cd.yaml`

The Jaguar CD attachment adds an optical-disc software environment to the
Atari Jaguar ecosystem, but Batch 7 does not assume how that relationship
should be represented canonically.

Before Jaguar CD production modeling, RVDB must explicitly decide whether
Jaguar CD should be represented as:

- a separate canonical platform entity
- an add-on entity related to Atari Jaguar
- a future normalized hardware/accessory relationship
- or another representation supported by the RVDB model

Until that decision is made:

- do not add `optical-disc` to Atari Jaguar solely because of Jaguar CD
- do not add Jaguar CD software-image extensions to Atari Jaguar
- do not create a Jaguar CD production platform
- do not silently treat Jaguar CD as equivalent to the base Jaguar

This boundary remains an explicit deferred decision.

---

# Entity Boundaries

Atari Lynx and Atari Jaguar are independent canonical platform entities.

They must not be merged with:

- Atari 2600
- Atari 5200
- Atari 7800
- Atari 8-bit computers
- Atari XEGS
- Atari ST
- modern Atari VCS
- Atari arcade hardware families

Atari Jaguar must also remain distinct from the unresolved Jaguar CD
representation.

---

# Existing Atari Production Coverage

Before Batch 7, RVDB contains these Atari platform entities:

- `platform.atari.2600`
- `platform.atari.5200`
- `platform.atari.7800`

Batch 7 adds:

- `platform.atari.lynx`
- `platform.atari.jaguar`

After Batch 7, these controlled production records represent five Atari
platform entities.

This does not imply complete Atari platform coverage.

---

# Deferred Atari Platform Families

The following remain outside Batch 7:

- Atari 8-bit computers
- Atari XEGS
- Atari Jaguar CD
- Atari ST
- modern Atari VCS
- Atari arcade hardware families

Each requires its own controlled selection and planning work.

No canonical production entity is introduced for these families by
Batch 7.

---

# Controlled Vocabulary Decisions

## Categories

Batch 7 uses only existing platform category values:

- Atari Lynx: `handheld`
- Atari Jaguar: `console`

No schema change is required.

## Media

Batch 7 uses only the existing controlled media value:

- `cartridge`

No schema change is required.

Jaguar CD optical-disc media remains outside the batch.

---

# Extension Decisions

## Atari Lynx

Approved initial extension:

- `lnx`

## Atari Jaguar

Approved initial extensions:

- `jag`
- `j64`

These are intentionally narrow production baselines.

Extension population is not intended to enumerate every format that an
emulator may technically accept.

RVDB should record formats that are defensible as common software, ROM, or
disk-image representations for the canonical platform.

---

# Relationship Decisions

Both Batch 7 platforms initially use:

```yaml
relationships:
  supports_core: []
```

This is intentional.

Platform population and emulator-core relationship population are separate
research operations.

No core entity reference should be created merely because a known emulator
supports Atari Lynx or Atari Jaguar.

---

# Metadata Decisions

The following optional fields remain deferred where a normalized value has
not already been established:

- `family`
- `generation`
- `regions`
- `architecture`

Batch 7 must not introduce speculative normalization simply to make the
records appear more complete.

---

# Intended Atari Lynx Production Shape

The intended production record is:

```yaml
id: platform.atari.lynx
type: platform

name: Atari Lynx

aliases: []

manufacturer:
  - manufacturer.atari

release_year: 1989

category:
  - handheld

media:
  - cartridge

extensions:
  - lnx

relationships:

  supports_core: []

metadata:

  retroarch_supported: true

  notes: ""
```

The exact production file must still pass the canonical schema,
relationship validation, tests, and build gates before commit.

---

# Intended Atari Jaguar Production Shape

The intended production record is:

```yaml
id: platform.atari.jaguar
type: platform

name: Atari Jaguar

aliases: []

manufacturer:
  - manufacturer.atari

release_year: 1993

category:
  - console

media:
  - cartridge

extensions:
  - jag
  - j64

relationships:

  supports_core: []

metadata:

  retroarch_supported: true

  notes: ""
```

The exact production file must still pass the canonical schema,
relationship validation, tests, and build gates before commit.

---

# Expected Production Changes

Batch 7 production implementation is expected to create:

- `data/platforms/atari/lynx.yaml`
- `data/platforms/atari/jaguar.yaml`

It is expected to update generated or count-sensitive artifacts only where
required by the existing test and build contracts.

Likely affected generated/baseline files must be determined from actual
test and build results rather than assumed in advance.

No Jaguar CD production YAML is part of Batch 7.

---

# Production Acceptance Criteria

Batch 7 production implementation is acceptable only if all of the
following are true:

1. Atari Lynx exists exactly once as `platform.atari.lynx`.
2. Atari Jaguar exists exactly once as `platform.atari.jaguar`.
3. both records reference `manufacturer.atari`.
4. Lynx uses release year `1989`.
5. Jaguar uses release year `1993`.
6. Lynx uses category `handheld`.
7. Jaguar uses category `console`.
8. both use controlled media value `cartridge`.
9. Lynx uses the conservative extension baseline `lnx`.
10. Jaguar uses the conservative extension baseline `jag`, `j64`.
11. Jaguar CD remains absent.
12. Jaguar does not inherit Jaguar CD optical-disc metadata.
13. `supports_core` remains empty unless separately researched.
14. unsupported optional metadata remains deferred.
15. schema validation passes.
16. relationship validation passes.
17. the complete regression suite passes.
18. the canonical build succeeds.
19. production entity count becomes 36.
20. platform entity count becomes 21.
21. graph node count becomes 36.
22. graph edge count becomes 36.
23. only the intended Batch 7 working set is committed.

---

# Expected Post-Batch State

After successful Batch 7 production implementation:

Production entities:

`36`

Platform entities:

`21`

Graph:

- nodes: `36`
- edges: `36`

Validation:

- schema errors: `0`
- relationship errors: `0`

The exact regression test count must be recorded from the implementation
result.

---

# Explicit Non-Goals

Batch 7 does not:

- create Atari Jaguar CD
- create Atari 8-bit computer entities
- create Atari XEGS
- create Atari ST
- create modern Atari VCS
- create Atari arcade hardware families
- populate emulator-core entities
- populate speculative core relationships
- normalize optional platform metadata
- modify the platform schema merely for this batch
- claim complete Atari platform coverage

---

# Implementation Sequence

After this plan is reviewed and committed separately:

1. verify a clean `develop` baseline
2. verify the Batch 7 plan commit
3. create `data/platforms/atari/lynx.yaml`
4. create `data/platforms/atari/jaguar.yaml`
5. verify Jaguar CD remains absent
6. run targeted platform contract tests
7. run the complete regression suite
8. run production validation
9. run the canonical build
10. inspect generated artifact changes
11. correct only required count-sensitive baselines
12. rerun the complete regression suite
13. rerun production validation
14. rerun the canonical build
15. verify 36 entities
16. verify 21 platforms
17. verify 36 graph nodes
18. verify 36 graph edges
19. verify the exact intended working set
20. document the implementation result
21. commit Batch 7 production separately
22. update the current milestone separately

---

# Next Checkpoint

Review this plan before production implementation.

If the plan passes its documentation gate, commit only:

`docs/platform_batch_atari_7.md`

Suggested plan commit:

`docs: plan Atari Lynx and Jaguar platform batch 7`

After that commit, the next checkpoint is:

P2A8E — Create Atari Lynx and Jaguar Production Data

No Batch 7 production YAML should exist before the plan commit.
