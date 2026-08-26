# RVDB Atari ST Platform Batch 8 Plan

## Status

PLANNED — NOT YET IMPLEMENTED

Phase:

Phase 2A — Platform Database Expansion

Checkpoint:

P2A9 — Platform Population Batch 8

---

# Purpose

Atari ST Platform Batch 8 extends the controlled Atari production catalog
with one canonical computer platform:

- Atari ST

The batch remains deliberately limited to a single platform so that the
later ST-family boundaries can remain explicit rather than being silently
collapsed into one production record.

No production YAML is created by this planning checkpoint.

---

# Batch Scope

Manufacturer:

`manufacturer.atari`

Platform:

`platform.atari.st`

Expected production path:

`data/platforms/atari/st.yaml`

Batch size:

1 platform entity

Current production entity count:

36

Current production platform count:

21

Expected post-batch entity count:

37

Expected post-batch platform count:

22

Expected post-batch graph:

- nodes: 37
- edges: 37

---

# Manufacturer Coverage

The canonical Atari manufacturer entity already exists:

`manufacturer.atari`

Canonical manufacturer path:

`data/manufacturers/atari.yaml`

No new manufacturer entity is required.

The Batch 8 platform record will reference:

`manufacturer.atari`

---

# Canonical Platform — Atari ST

## Canonical ID

`platform.atari.st`

## Canonical Path

`data/platforms/atari/st.yaml`

## Canonical Name

`Atari ST`

## Aliases

No alias is required for the initial production record.

Aliases must not be invented merely to populate the field.

## Manufacturer

`manufacturer.atari`

## Earliest Commercial Release Year

`1985`

## Category

`computer`

This value already exists in the controlled Platform v2 category
vocabulary.

## Media

`floppy`

This value already exists in the controlled Platform v2 media vocabulary.

## Conservative Software-Image Extensions

Initial controlled extension set:

- `st`
- `msa`
- `stx`

The extension list is intentionally conservative.

Additional executable, archive, hard-disk-image, emulator-specific, or
less-general formats require separate evidence and review.

## Emulator-Core Relationships

Initial relationship shape:

```yaml
relationships:
  supports_core: []
```

No emulator-core relationships are populated during Batch 8.

They may be added only after the required canonical core entities exist
and Atari ST/core relationships have been researched independently.

## Deferred Optional Metadata

The following fields remain omitted unless separately normalized and
justified:

- `family`
- `generation`
- `regions`
- `architecture`

No speculative values will be introduced.

---

# Atari ST Family Entity Boundary

Batch 8 models only the canonical Atari ST platform.

The following related machines are deliberately excluded from Batch 8:

- Atari STE
- Atari TT
- Atari Falcon

Do not create during Batch 8:

- `platform.atari.ste`
- `platform.atari.tt`
- `platform.atari.falcon`

Do not create during Batch 8:

- `data/platforms/atari/ste.yaml`
- `data/platforms/atari/tt.yaml`
- `data/platforms/atari/falcon.yaml`

These machines are historically related to the Atari ST line, but Batch 8
does not assume that they should be represented as aliases, revisions, or
the same canonical platform entity.

Each requires a separate canonical entity-boundary review before any
production YAML is introduced.

Until that review occurs:

- do not merge STE-specific capabilities into Atari ST
- do not merge TT-specific capabilities into Atari ST
- do not merge Falcon-specific capabilities into Atari ST
- do not create aliases that imply canonical equivalence
- do not introduce family metadata merely to solve this boundary

Batch 8 therefore establishes only:

`platform.atari.st`

as the production entity.

---

# Media Boundary

The initial Atari ST production record uses:

`floppy`

as its controlled media value.

Batch 8 does not attempt to normalize every storage mechanism used across
the broader ST ecosystem.

In particular, hard-disk, cartridge, removable-storage, and later-machine
storage distinctions remain outside this controlled first production
record unless separately researched and modeled.

---

# Extension Decisions

Approved initial extensions:

- `st`
- `msa`
- `stx`

These extensions form the conservative initial Atari ST disk-image set.

Batch 8 does not automatically include every format accepted by a current
Atari ST emulator.

Executable formats, archive formats, generic raw formats, hard-disk images,
and emulator-specific containers require separate evidence and review.

---

# Intended Production Shape

The intended Atari ST production record is:

```yaml
id: platform.atari.st
type: platform

name: Atari ST

aliases: []

manufacturer:
  - manufacturer.atari

release_year: 1985

category:
  - computer

media:
  - floppy

extensions:
  - st
  - msa
  - stx

relationships:

  supports_core: []

metadata:

  retroarch_supported: true

  notes: ""
```

The exact production record must still pass schema validation, relationship
validation, regression tests, and the canonical build before commit.

---

# Production Acceptance Criteria

Batch 8 production implementation is acceptable only if all of the
following are true:

1. Atari ST exists exactly once as `platform.atari.st`.
2. the production path is `data/platforms/atari/st.yaml`.
3. the record references `manufacturer.atari`.
4. the canonical name is `Atari ST`.
5. the earliest commercial release year is `1985`.
6. the category is `computer`.
7. the media value is `floppy`.
8. the conservative extension set is `st`, `msa`, `stx`.
9. `supports_core` remains empty unless separately researched.
10. unsupported optional metadata remains deferred.
11. Atari STE remains absent.
12. Atari TT remains absent.
13. Atari Falcon remains absent.
14. ST-family distinctions are not silently merged into the ST record.
15. schema validation passes.
16. relationship validation passes.
17. the complete regression suite passes.
18. the canonical build succeeds.
19. production entity count becomes 37.
20. platform entity count becomes 22.
21. graph node count becomes 37.
22. graph edge count becomes 37.
23. only the intended Batch 8 working set is committed.

---

# Expected Dataset Result

Current production entities:

36

Current platform entities:

21

Batch 8 additions:

1

Expected production entities after implementation:

37

Expected platform entities after implementation:

22

Expected canonical graph:

- nodes: 37
- edges: 37

The exact regression test count must be recorded from the implementation
result.

---

# Explicit Batch 8 Deferrals

Batch 8 does not include:

- Atari STE
- Atari TT
- Atari Falcon
- Atari 8-bit computers
- Atari XEGS
- Atari Jaguar CD
- modern Atari VCS
- Atari arcade hardware families
- Nintendo DSi
- Sega Master System / Mark III
- emulator-core relationship population
- normalized family metadata
- generation metadata
- structured regional metadata
- architecture metadata

---

# Production Gate

Do not create:

- `data/platforms/atari/st.yaml`

until this plan has been:

1. reviewed
2. checked against the current platform contract
3. committed separately
4. pushed to `develop`

Do not create STE, TT, or Falcon production YAML during Batch 8.

---

# Planned Production Sequence

After plan approval:

1. commit this plan only
2. push the plan commit to `develop`
3. verify a clean production baseline
4. create `data/platforms/atari/st.yaml`
5. verify STE, TT, and Falcon remain absent
6. validate Platform v2 structure
7. verify the Atari manufacturer relationship
8. run targeted platform tests
9. run the complete regression suite
10. run production validation
11. rebuild `rvdb.bundle.json`
12. inspect actual generated and count-sensitive changes
13. update only required dataset baselines
14. rerun the complete regression suite
15. rerun production validation
16. rerun the canonical build
17. verify 37 production entities
18. verify 22 platform entities
19. verify 37 graph nodes
20. verify 37 graph edges
21. append the implementation result to this document
22. review the full production diff
23. commit production separately
24. push production to `develop`
25. update `docs/current_milestone.md` separately

---

# Next Checkpoint

Review and approve the Atari ST Platform Batch 8 plan.

If approved:

P2A9D — Commit Atari ST Platform Batch 8 Plan

No Batch 8 production YAML should exist before that commit.
