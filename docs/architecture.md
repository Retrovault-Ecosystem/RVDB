# RVDB Architecture

## Current Milestone #14 integration contract

Milestone #14 closes the approved 14-milestone roadmap; no Milestone #15 has begun. The producer remains
`EntityLoader -> validated RVGraph -> nodes/edges bundle`; RetroVault consumes the portable
bundle and owns local inventory, persistence, presentation policy and emulator lifecycle.
No schema, canonical identity or graph-format change is part of this milestone.

`commands/validate.py` returns a boolean and rejects duplicate IDs before graph construction.
`commands/build.py` retains its Path/None API and existing validation. `cli.py` maps those two
commands to process exit status (zero only on success), including validation alias `v`.
Other CLI return conventions remain unchanged. `build/builder.py` serializes to a unique
same-directory temporary file, flushes/fsyncs, preserves existing output permissions and uses
atomic replacement. Serialization/write/flush/replacement failure preserves the old bundle
and removes temporary output. Successful deterministic JSON bytes remain compatible.

See [current evidence](current_milestone.md) and RetroVault's paired
`docs/milestone14_final_integration.md` for closure/deferred-work details. Historical sections
below remain historical. Scalar relationship expansion, richer BIOS/compatibility modeling,
automatic distribution and speculative canonical data remain outside M14.

## Overview

RVDB (RetroVault Database) is the knowledge foundation behind the RetroVault ecosystem.

The purpose of RVDB is to provide a structured, validated, relationship-aware database containing:

- Retro gaming platforms
- Games
- Developers
- Publishers
- Emulation cores
- Hardware information
- RetroArch configuration metadata
- Visual enhancement data
- Controller information
- BIOS requirements

RVDB is designed as a knowledge graph rather than a simple game list.

---

# Core Architecture

RVDB is separated into multiple layers.

```
                 RetroVault Application
                         |
                         |
                    RVDB Database
                         |
        ---------------------------------
        |               |               |
    Data Layer     Engine Layer    Validation Layer
        |               |               |
       YAML          Graph          Rules
     Entities       Queries        Schemas
```

---

# Data Layer

Location:

```
data/
```

The data layer contains YAML entity definitions.

Examples:

```
data/
├── platforms/
├── games/
├── cores/
├── developers/
├── publishers/
├── genres/
├── controllers/
├── bios/
├── shaders/
├── overlays/
└── themes/
```

YAML files are the source of truth.

---

# Entity System

Every RVDB object is represented as an entity.

Example:

```yaml
id: platform.nintendo.snes
type: platform

name: Super Nintendo

aliases:
  - SNES
  - Super NES
```

Every entity contains:

- Unique ID
- Entity type
- Display name
- Optional aliases
- Optional relationships
- Metadata fields

---

# Relationship Graph

RVDB uses a graph-based architecture.

Entities connect through relationships.

Example:

```
Game
 |
 | developed_by
 |
Developer


Game
 |
 | platform
 |
Platform


Platform
 |
 | supports_core
 |
Core
```

This allows RetroVault to answer questions like:

- What games exist on SNES?
- Which cores support this platform?
- Which developer created this game?
- Which shaders work best for this system?

---

# Engine Layer

Location:

```
engine/
```

The engine provides:

## Entity Loading

Responsible for:

- Discovering YAML files
- Parsing entities
- Creating entity objects


## Graph Construction

Responsible for:

- Building entity nodes
- Creating relationships
- Creating reverse indexes


## Query Engine

Responsible for:

- Searching entities
- Resolving names
- Traversing relationships


## Entity Resolver

Allows natural queries:

Example:

```
rvdb query "Super Nintendo"
```

can resolve:

```
platform.nintendo.snes
```

---

# Validation Layer

Location:

```
validator/
```

Responsible for maintaining database integrity.

Includes:

## Schema Validation

Checks:

- Required fields
- Data types
- Supported entity types
- Unknown fields


## Relationship Validation

Checks:

- Valid relationship names
- Valid target entity types
- Broken references

---

# Command Layer

Location:

```
commands/
```

Provides CLI access.

Current commands include:

```
validate
build
query
list
show
info
related
cores
who-uses
find
```

---

# Build System

The build system converts RVDB into application-ready formats.

Future outputs:

```
build/
├── json/
├── csv/
├── indexes/
├── manifests/
└── application_data/
```

---

# Design Principles

RVDB follows these principles:

1. YAML is the source of truth.
2. Entities are reusable building blocks.
3. Relationships define knowledge.
4. Validation prevents corruption.
5. The database grows independently from applications.
6. RetroVault applications consume RVDB rather than duplicate data.

---

# Future Expansion

Planned additions:

- Complete console database
- Arcade hardware database
- Emulator compatibility database
- Libretro core database
- Shader database
- Overlay database
- Controller database
- BIOS database
- Artwork metadata
- Automated metadata importing

## Current producer/consumer contract — Milestone #1 (2026-09-28)

This section is the current export-boundary reference; earlier overview sections
include historical and future architecture descriptions.

YAML remains the canonical knowledge source. RVDB owns entity identity, schemas,
relationships, and portable knowledge export. It does not own a consumer's local
ROM inventory, installed core paths, user preferences, presentation calibration,
or emulator processes. RetroVault consumes the bundle through `RVDBConsumer` and
its application-owned `RVDBService` typed read models, not by importing this engine.

The active production build path is:

`commands/build.py` -> fresh `EntityLoader` snapshot -> `build_graph` ->
`SchemaValidator` + `RelationshipValidator` -> `build_bundle`.

The command rejects empty input, duplicate IDs, schema failures, missing relationship
targets, and invalid relationship types before invoking the writer. Failed validation
does not replace the prior artifact. It retains the existing return convention:
output path on success, `None` plus a diagnostic on failure. The low-level
`build_bundle(graph, output)` remains a serializer; direct callers must validate
first. Build I/O itself is not claimed to be an atomic replacement transaction.

`engine/context.py` caches the query graph/resolver. The build command deliberately
uses a fresh source snapshot rather than that query cache. `EntityRegistry` remains
an existing reference/name lookup facility; this milestone does not replace either
it or the loader/graph with a new universal runtime.

The portable envelope remains exactly `nodes` and `edges`, with canonical string
IDs. There is no new mandatory version field. RetroVault validates nested structural
shape before publishing a loaded snapshot, preserves the previous snapshot on
failure, and does not duplicate RVDB's schema engine. Its compatibility behavior
permits unresolved targets and omitted empty edge entries. The exported edge map
is authoritative for consumed relationships. Raw consumer dictionaries remain
low-level compatibility access; application callers should use typed service views.

### Historical source/artifact discrepancy — resolved in Milestone #2

The Milestone #1 audit validated 53 YAML source entities with no schema or relationship
errors. The tracked producer bundle and local RetroVault copy contained 57 entities. The four bundle-only entities
are `core.mame`, `core.mupen64plus.next`,
`compatibility.core.mame.platform.arcade`, and
`compatibility.core.mupen64plus.next.platform.nintendo.n64`.

The bundles also extend the relationships of `frontend.retroarch`, `platform.arcade`,
and `platform.nintendo.n64`. RetroVault's copy has one additional edge entry for the
N64 compatibility entity compared with this repository's bundle.

Milestone #1 did not regenerate either bundle. At that checkpoint, a source build
would have removed the extra records. That discrepancy is resolved by the source
promotion and verified generation described below. The following audit hashes
remain historical evidence and are not the current artifact hashes.

Audit hashes:

- RVDB `rvdb.bundle.json`: `c64263bd84cf0c1e0c9359d0e280e28be13814142af6e356a2e484352850d9e9`
- RetroVault `data/rvdb/rvdb.bundle.json`: `978aacf594b580f12c2cf8189bb33459280967074095c3d9caca6b6e2538c0fa`

The complete six-boundary consumer contract lives in the RetroVault repository at
`docs/architecture_contracts.md`. Bundle distribution, schema expansion, knowledge
reconciliation, and later ecosystem milestones remain outside Milestone #1.

Milestone #1 verification: all **372 RVDB tests passed** (370 baseline plus two
producer-boundary regressions). The companion RetroVault suite passed **1,864 tests**.
Both bundle hashes above remained unchanged. No knowledge reconciliation or
publication was performed.


## Milestone #2 — RVDB source/bundle reconciliation

The four previously bundle-only records now have canonical YAML ownership:

- `data/cores/libretro/mame.yaml`
- `data/cores/libretro/mupen64plus_next.yaml`
- `data/compatibilities/core.mame.platform.arcade.yaml`
- `data/compatibilities/core.mupen64plus.next.platform.nintendo.n64.yaml`

`data/frontends/retroarch.yaml`, `data/platforms/arcade.yaml`, and
`data/platforms/nintendo/n64.yaml` now carry the same associations already present
in the distributed knowledge. These are restorations of source ownership, not new
compatibility claims. The earlier bundle-only changes originated in commits
`0832a93147e228c5e562354c30db095fa1507d29` (N64) and
`291ade131ffd7d772083acac9ddda44c43d60345` (Arcade).

The existing validated build produces **57 nodes and 57 edge-map entries** from
**57 valid source entities**. Both bundles are byte-identical, with SHA-256:

`cbe52800852543f88bdaf033bb0d50e348ffe64368391498ff93d72a785610dc`

All 57 node payloads match both pre-reconciliation bundles exactly, including
names, IDs, evidence text, dates, and playability values. The existing 53 source
entities are unchanged except for the three approved relationship restorations.
Generation adds the missing empty edge entries and sorts serialization using the
existing builder. Empty entries are not new relationship assertions.

### Evidence and scope

The three evidence records in each promoted compatibility claim retain their
original `2026-09-23` dates. Historical local binary/system-info observations were
not re-executed and are not presented as fresh qualification. Official Libretro
[MAME core metadata](https://raw.githubusercontent.com/libretro/libretro-core-info/master/mame_libretro.info)
and [Mupen64Plus-Next metadata](https://raw.githubusercontent.com/libretro/libretro-core-info/master/mupen64plus_next_libretro.info)
were consulted during the reconciliation analysis to corroborate identity and
platform association. No extra evidence record or stronger claim was inserted.

`core.mame` means the Libretro core, not a replacement for arcade hardware identities
or a newly populated standalone emulator. `playable` remains the existing scoped
compatibility classification, not a guarantee about every title or ROM set.

RetroVault's `RVDBService.retroarch_view()` now reads `launches_core` through
`RVDBConsumer.relationship_targets()`, consistently with other graph views.
Embedded node relationships cannot override the exported graph. Missing exported
relationships remain empty, and unresolved entities retain established fallback
handling. Generated artifacts guarantee that embedded and exported relationships
agree; the consumer does not become another schema engine.

### Bundle delivery and drift prevention

RVDB's `rvdb.bundle.json` is tracked generated output. RetroVault's
`data/rvdb/rvdb.bundle.json` is an intentionally Git-ignored local runtime copy.
Earlier references to two checked-in bundles should be read with this correction.
The existing ignore policy is preserved; no installed package, remote artifact,
or external runtime directory is updated by this milestone.

`tests/test_bundle_reconciliation_v2.py` checks a fresh validated build against the
tracked artifact byte-for-byte, verifies deterministic generation with reversed
entity input order, and protects source-backed core/claim relationships. It needs
only this repository. It does not silently skip a missing consumer checkout.

Consumer equality is a separate explicit synchronization acceptance check. To
reproduce it, set both absolute repository paths and run the following. The wrapper
checks `cmd_build()`'s result because the historical CLI dispatcher does not turn
its `None` return into a nonzero exit status.

```sh
rvdb_root=/path/to/rvdb
retrovault_root=/path/to/retrovault
(
    cd "$rvdb_root" || exit 1
    .venv/bin/python -B -c 'from commands.build import cmd_build; raise SystemExit(0 if cmd_build() is not None else 1)' || exit 1
    .venv/bin/python -B -m pytest -q -p no:cacheprovider tests/test_bundle_reconciliation_v2.py || exit 1
    mkdir -p "$retrovault_root/data/rvdb" || exit 1
    cp rvdb.bundle.json "$retrovault_root/data/rvdb/rvdb.bundle.json" || exit 1
    cmp rvdb.bundle.json "$retrovault_root/data/rvdb/rvdb.bundle.json" || exit 1
    sha256sum rvdb.bundle.json "$retrovault_root/data/rvdb/rvdb.bundle.json"
)
```

Close RetroVault before replacing its local bundle and restart it afterward;
consumer/service indexes are snapshots, and automatic hot reload is not introduced.
Tests and synchronization do not require importing the producer into RetroVault.

This milestone preserves schemas, the `nodes`/`edges` envelope, user persistence,
ROM-path identity, core-selection policy, and all presentation/runtime assets.
N64 and Arcade remain UNCONFIGURED for production presentation. No emulator was
launched, and no new platform readiness or live playability qualification is claimed.
Automatic distribution, new knowledge population, state migration, and Milestones
#3–#14 remain outside this milestone.


Milestone #2 closure verification: **375 RVDB tests and 1,869 RetroVault tests passed**.
Source validation reports 57 valid entities with zero errors. Source/artifact parity,
repeat-build determinism, explicit consumer equality, source-delta preservation,
Python parsing, and diff integrity pass. See the
[formal closure record](current_milestone.md#ecosystem-milestone-2--rvdb-sourcebundle-reconciliation--complete).
No later milestone has started and no release/commit/push was performed.
