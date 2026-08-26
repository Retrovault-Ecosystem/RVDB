# RVDB Platform Catalog Policy

_Last Updated: 2026-08-26_

---

# Purpose

This document defines the canonical identity, filesystem, naming, and
population rules for RVDB platform entities during Phase 2A platform
database expansion.

The policy exists to ensure that large-scale platform population remains:

- deterministic
- reviewable
- machine-validatable
- consistent across manufacturers
- independent of source-specific naming
- compatible with the Platform Entity Contract v2

---

# 1. Canonical Platform Identity

Every distinct RVDB platform must have one stable canonical entity ID.

Platform IDs use dot-separated namespace segments.

Preferred form:

`platform.<manufacturer>.<system>`

Examples:

- `platform.nintendo.nes`
- `platform.nintendo.snes`
- `platform.sega.genesis`

The canonical ID is the database identity.

Display names, regional names, abbreviations, aliases, filenames, and
directory paths must not replace or redefine canonical identity.

Once published as production data, a canonical platform ID should be
treated as stable unless a deliberate migration is approved.

---

# 2. Manufacturer Namespace

Where a platform has a clear canonical manufacturer, its ID should use
the canonical manufacturer namespace.

Example:

`platform.nintendo.nes`

corresponds to:

`manufacturer.nintendo`

Manufacturer namespace segments should therefore align with canonical
manufacturer entity IDs whenever practical.

A manufacturer name must not be invented merely to satisfy the preferred
ID structure.

Platforms without one meaningful manufacturer namespace require an
explicitly justified canonical identity.

---

# 3. Canonical Filesystem Layout

Manufacturer-specific platforms should be stored beneath a manufacturer
directory.

Preferred layout:

`data/platforms/<manufacturer>/<system>.yaml`

Examples:

`data/platforms/nintendo/nes.yaml`

`data/platforms/nintendo/snes.yaml`

`data/platforms/sega/genesis.yaml`

The directory segment should normally match the manufacturer namespace
used by the platform ID.

The filename should normally match the final canonical system segment.

The filesystem path organizes source data but is not itself the entity
identity.

Canonical identity remains the entity `id`.

---

# 4. Non-Manufacturer Platform Classes

Not every platform concept has a single useful manufacturer.

Collective, generic, historically broad, or multi-manufacturer platform
classes must not receive fake manufacturer entities solely to satisfy the
preferred manufacturer directory structure.

The existing Arcade entity is an example:

`platform.arcade`

Such exceptions must remain explicit and justified.

Special catalog structures for broad platform classes may be introduced
later when actual production requirements establish the appropriate
organization.

---

# 5. Canonical Name

The `name` field contains the preferred human-readable canonical platform
name.

A canonical name should be:

- historically recognizable
- sufficiently specific
- stable
- suitable for general display

The canonical name does not need to reproduce the canonical ID wording
exactly.

Example:

ID:

`platform.nintendo.nes`

Name:

`Nintendo Entertainment System`

---

# 6. Aliases

Alternate names belong in `aliases`.

Aliases may include:

- common abbreviations
- alternate marketed names
- widely recognized regional names
- historical naming variants
- common search terms

Aliases must not create duplicate platform entities.

Regional naming information may remain searchable through aliases until
RVDB implements a validated structured regional-name representation.

---

# 7. Platform Entity Boundary

A new platform entity should represent a meaningfully distinct hardware
or software platform, not every revision, cosmetic redesign, bundle, or
regional branding variation.

A separate platform entity is generally justified when one or more of
the following materially differ:

- software compatibility
- execution environment
- hardware architecture
- software distribution format
- emulator/core compatibility
- platform identity recognized by the emulation ecosystem

A separate platform entity is generally not justified solely by:

- case redesign
- color variation
- storage-capacity variation
- packaging
- bundle contents
- minor board revision
- regional branding

Ambiguous cases must be reviewed before production data is added.

No automatic rule should split a platform solely because a source
database lists multiple hardware models.

---

# 8. Regional Variants

Regional branding alone should normally be represented through canonical
name and aliases rather than duplicate platform entities.

Separate regional entities require a technical or compatibility reason,
not merely a different marketed name.

The Platform Entity Contract v2 intentionally defers structured regional
name mappings until the schema language can validate them properly.

---

# 9. Family

The optional `family` field groups platforms belonging to a stable,
recognizable hardware or platform family.

Family values must not be used as substitutes for canonical IDs.

Family classification must not cause multiple distinct platforms to be
collapsed into one entity.

Family vocabulary should be introduced conservatively and normalized as
the production catalog expands.

---

# 10. Source Independence

RVDB canonical identity must not be copied mechanically from any single
external catalog.

External sources may disagree about:

- platform boundaries
- names
- release dates
- generations
- manufacturer attribution
- supported media
- file extensions

RVDB must reconcile such information into its own canonical model.

Source-specific identifiers must not become canonical RVDB IDs merely
because they are convenient.

---

# 11. No Speculative Data

Optional Platform v2 fields must not be populated merely because the
template contains them.

Unknown or insufficiently verified information should remain omitted or
null where permitted.

Empty placeholder values must not be mass-added to production entities
for cosmetic consistency.

Existing P2A1 migration policy remains authoritative:

no forced production edits solely to match the template.

---

# 12. Controlled Population Batches

Large-scale platform creation must proceed through controlled batches.

Each batch should have a clearly defined scope such as:

- one manufacturer
- one platform family
- one coherent platform class

Before a batch is committed:

1. canonical IDs must be reviewed
2. entity boundaries must be reviewed
3. manufacturer references must resolve
4. required category values must be valid
5. optional data must be justified
6. relationships must resolve
7. production validation must pass
8. the complete regression suite must pass
9. the canonical bundle must build successfully
10. repository changes must be reviewed before commit

Platform population should favor small reviewable commits over a single
large catalog import.

---

# 13. Existing Foundation Data

The Foundation dataset currently contains:

- `platform.arcade`
- `platform.nintendo.nes`
- `platform.nintendo.snes`
- `platform.sega.genesis`

Nintendo platform files already follow the preferred manufacturer
directory convention.

The Sega Genesis canonical ID follows the preferred namespace convention,
but its current filesystem path is transitional:

`data/platforms/platform_sega_genesis.yaml`

Preferred canonical path:

`data/platforms/sega/genesis.yaml`

Moving that file is a separate controlled migration checkpoint.

The Arcade entity remains a justified non-manufacturer exception and is
not forced into a fabricated manufacturer directory.

---

# 14. Catalog Expansion Gate

No large-scale platform YAML population should begin until:

1. this catalog policy is reviewed
2. existing transitional platform paths are audited
3. the first controlled population batch is explicitly selected
4. required manufacturer entities for that batch exist
5. validation, tests, and canonical build remain green

---

# Current Decision

Canonical manufacturer-specific platform layout:

`data/platforms/<manufacturer>/<system>.yaml`

Canonical manufacturer-specific platform ID:

`platform.<manufacturer>.<system>`

Canonical IDs are authoritative.

Filesystem paths are organizational and should align with IDs where
practical.

Aliases represent alternate names and must not create duplicate entities.

Platform variants become separate entities only when a meaningful
technical, compatibility, or emulation-platform distinction justifies
the boundary.

Large-scale population will proceed through small controlled batches.

---

# 15. Multi-Word System IDs and Filenames

Platform system names containing multiple words may use multiple canonical
namespace segments.

Example:

`Game Boy`

may be represented canonically as:

`platform.nintendo.game.boy`

A longer system name may extend the namespace:

`Game Boy Color`

may be represented as:

`platform.nintendo.game.boy.color`

The manufacturer namespace remains the first platform-specific segment.

Filesystem names must remain readable and deterministic.

For a multi-segment system namespace, the platform filename should join
the system namespace segments using underscores.

Examples:

Canonical ID:

`platform.nintendo.game.boy`

Canonical path:

`data/platforms/nintendo/game_boy.yaml`

Canonical ID:

`platform.nintendo.game.boy.color`

Canonical path:

`data/platforms/nintendo/game_boy_color.yaml`

Canonical ID:

`platform.nintendo.n64`

Canonical path:

`data/platforms/nintendo/n64.yaml`

Existing stable IDs such as:

- `platform.nintendo.nes`
- `platform.nintendo.snes`
- `platform.sega.genesis`

remain unchanged.

Canonical IDs must not be renamed merely to make filenames shorter.

The canonical entity ID remains authoritative; the filename is an
organizational representation of the system namespace.
