# RVDB Atari Platform Batch 3 Plan

_Last Updated: 2026-08-26_

---

# Status

PLANNED — NO PRODUCTION YAML CREATED

---

# Scope

Atari Platform Batch 3 contains three platform entities:

1. Atari 2600
2. Atari 5200
3. Atari 7800

The batch establishes Atari's first production platform entities in RVDB.

---

# Batch Selection Rationale

Atari is selected for Platform Population Batch 3 because:

- `manufacturer.atari` already exists
- no Atari platform entities currently exist
- no Atari platform references currently exist
- the batch expands manufacturer coverage
- all three selected systems are cartridge-based home consoles
- the existing Platform v2 category vocabulary supports the batch
- the existing Platform v2 media vocabulary supports the batch
- no schema expansion is required

Nintendo already has substantial production-platform coverage.

Sega also has established production-platform coverage, while its
Master System / Mark III boundary remains intentionally deferred.

---

# Research Policy

The batch uses conservative, defensible metadata.

Release year represents earliest canonical commercial release, not merely:

- announcement year
- prototype year
- planned launch year
- branding year

Extensions represent platform-specific software-image representations.

Generic emulator-container or archive extensions are deliberately excluded
when a platform-specific extension exists.

---

# 1. Atari 2600

Canonical ID:

`platform.atari.2600`

Canonical path:

`data/platforms/atari/2600.yaml`

Canonical name:

`Atari 2600`

Aliases:

- `Atari 2600 VCS`

Manufacturer:

- `manufacturer.atari`

Release year:

`1977`

Category:

- `console`

Media:

- `cartridge`

Proposed extensions:

- `a26`

Deferred fields:

- `family`
- `generation`
- `regions`
- `architecture`

Relationships:

`supports_core` remains empty until an appropriate canonical RVDB core
entity exists.

Historical naming note:

The hardware was originally marketed under the Video Computer System
name before the Atari 2600 branding became canonical.

The modern Atari VCS product must not be conflated with this historical
platform.

Extension policy:

`.a26` is used as the platform-specific software-image extension.

Generic `.bin` and archive formats such as `.zip` are intentionally omitted.

---

# 2. Atari 5200

Canonical ID:

`platform.atari.5200`

Canonical path:

`data/platforms/atari/5200.yaml`

Canonical name:

`Atari 5200`

Aliases:

- `Atari 5200 SuperSystem`

Manufacturer:

- `manufacturer.atari`

Release year:

`1982`

Category:

- `console`

Media:

- `cartridge`

Proposed extensions:

- `a52`

Deferred fields:

- `family`
- `generation`
- `regions`
- `architecture`

Relationships:

`supports_core` remains empty until an appropriate canonical RVDB core
entity exists.

Entity-boundary note:

Atari 5200 remains distinct from the Atari 8-bit computer family even
though the hardware architectures are closely related.

Emulator-core support for both families must not cause their platform
identities to be merged.

Extension policy:

`.a52` is used as the platform-specific cartridge-image extension.

Other formats accepted by Atari800, including Atari computer disk,
cassette, executable, archive, and generic binary formats, are not added
to this platform record solely because the same emulator core can load
them.

---

# 3. Atari 7800

Canonical ID:

`platform.atari.7800`

Canonical path:

`data/platforms/atari/7800.yaml`

Canonical name:

`Atari 7800`

Aliases:

- `Atari 7800 ProSystem`

Manufacturer:

- `manufacturer.atari`

Release year:

`1986`

Category:

- `console`

Media:

- `cartridge`

Proposed extensions:

- `a78`

Deferred fields:

- `family`
- `generation`
- `regions`
- `architecture`

Relationships:

`supports_core` remains empty until an appropriate canonical RVDB core
entity exists.

Release-year decision:

Historical material surrounding the 7800 includes references to a planned
or proposed 1984 introduction.

RVDB uses `1986` because the production platform's commercial launch is
treated as occurring in 1986 rather than treating announcement,
pre-release, or planned-launch activity as commercial release.

Extension policy:

`.a78` is used as the platform-specific software-image extension.

Generic `.bin` is intentionally omitted.

---

# Canonical Naming Policy

Numeric Atari platform names remain numeric canonical namespace segments.

Examples:

`platform.atari.2600`

`platform.atari.5200`

`platform.atari.7800`

Canonical paths:

`data/platforms/atari/2600.yaml`

`data/platforms/atari/5200.yaml`

`data/platforms/atari/7800.yaml`

No additional namespace segment is required because each canonical system
name is represented unambiguously by its Atari model number.

---

# Media Policy

All three platforms use the existing controlled Platform v2 media value:

`cartridge`

No Platform schema expansion is required.

Planned values:

Atari 2600:

`media: [cartridge]`

Atari 5200:

`media: [cartridge]`

Atari 7800:

`media: [cartridge]`

---

# Extension Policy

Platform-specific extensions are preferred over generic emulator formats.

Planned extensions:

Atari 2600:

- `a26`

Atari 5200:

- `a52`

Atari 7800:

- `a78`

The following are intentionally excluded from the initial records:

- `bin`
- `zip`
- generic archive formats
- Atari 8-bit computer disk-image formats
- Atari 8-bit computer cassette formats
- Atari 8-bit computer executable formats

An emulator accepting a file type does not automatically make that file
type canonical platform metadata.

---

# Fields Intentionally Deferred

The following optional Platform v2 fields remain deferred:

- `family`
- `generation`
- `regions`
- `architecture`

Hardware facts exist for all three systems, but normalization policy must
precede production use of these fields.

No values should be added merely to make the records look complete.

---

# Relationships

No `supports_core` relationships will be invented.

The current canonical RVDB core catalog does not contain Atari cores for
these platforms.

The production records will therefore use:

`supports_core: []`

until a separately researched core-population stage creates the relevant
canonical core entities.

---

# Planned Production Records

Each initial platform record should contain:

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

Before Atari Platform Batch 3 is committed:

1. create exactly three Atari platform YAML files
2. verify canonical IDs
3. verify canonical paths
4. verify `manufacturer.atari` references
5. verify `console` categories
6. verify controlled `cartridge` media values
7. verify platform-specific extensions
8. verify deferred fields remain omitted
9. verify unsupported relationships remain empty
10. run production validation
11. run the complete regression suite
12. regenerate the canonical bundle
13. update dataset-count regression baselines
14. inspect the complete production diff
15. align this batch document with implementation results
16. commit the production batch separately
17. push to `develop`

---

# Expected Entity Count

Current production entity count:

`25`

Atari Batch 3 additions:

`3`

Expected post-batch entity count:

`28`

Current platform count:

`10`

Expected post-batch platform count:

`13`

---

# Expected Canonical Graph

Current graph:

- nodes: 25
- edges: 25

Expected after Atari Batch 3:

- nodes: 28
- edges: 28

No additional relationship edges are expected because each new platform's
`supports_core` list remains empty.

---

# Explicitly Out of Scope

Atari Batch 3 does not include:

- Atari 8-bit computers
- Atari XEGS
- Atari Lynx
- Atari Jaguar
- Atari Jaguar CD
- Atari ST
- Atari VCS (modern system)
- arcade hardware families

These may be considered in later controlled batches.

---

# Next Decision

Review and approve the Atari Platform Batch 3 plan before creating:

- `data/platforms/atari/2600.yaml`
- `data/platforms/atari/5200.yaml`
- `data/platforms/atari/7800.yaml`

No Atari Batch 3 production YAML should exist before the planning
checkpoint is committed.

---

# Implementation Result

Status:

COMPLETE

Atari Platform Batch 3 has been implemented successfully.

Production entities created:

- `platform.atari.2600`
- `platform.atari.5200`
- `platform.atari.7800`

Canonical paths:

- `data/platforms/atari/2600.yaml`
- `data/platforms/atari/5200.yaml`
- `data/platforms/atari/7800.yaml`

This establishes Atari's first production platform family in RVDB.

## Implemented Metadata

### Atari 2600

Canonical ID:

`platform.atari.2600`

Canonical name:

`Atari 2600`

Alias:

`Atari 2600 VCS`

Manufacturer:

`manufacturer.atari`

Release year:

`1977`

Category:

`console`

Media:

`cartridge`

Extension:

- `a26`

### Atari 5200

Canonical ID:

`platform.atari.5200`

Canonical name:

`Atari 5200`

Alias:

`Atari 5200 SuperSystem`

Manufacturer:

`manufacturer.atari`

Release year:

`1982`

Category:

`console`

Media:

`cartridge`

Extension:

- `a52`

### Atari 7800

Canonical ID:

`platform.atari.7800`

Canonical name:

`Atari 7800`

Alias:

`Atari 7800 ProSystem`

Manufacturer:

`manufacturer.atari`

Release year:

`1986`

Category:

`console`

Media:

`cartridge`

Extension:

- `a78`

## Deferred Metadata

The following optional Platform v2 fields remain deliberately omitted:

- `family`
- `generation`
- `regions`
- `architecture`

No speculative values were introduced.

The `supports_core` relationship remains empty for all three new platforms
pending a separately researched Atari core-population stage.

## Dataset Result

After Atari Platform Batch 3:

Production entities:

28

Platform entities:

13

Production validation:

- entities checked: 28
- valid entities: 28
- schema errors: 0
- relationship errors: 0

Automated regression suite:

145 passing

Canonical graph:

- nodes: 28
- edges: 28

Canonical build:

PASS

All Atari Batch 3 entities are present in the canonical bundle.

## Batch Result

Atari Platform Batch 3 satisfies the controlled population requirements
defined by:

- `docs/platform_contract.md`
- `docs/platform_catalog_policy.md`

The batch:

- was planned before production creation
- uses canonical `manufacturer.atari` references
- uses canonical numeric platform IDs
- follows canonical Atari filesystem paths
- uses the controlled `cartridge` media value
- uses platform-specific software-image extensions
- leaves unsupported optional metadata omitted
- introduces no unsupported relationships

Atari Platform Batch 3 is ready for its production commit.
