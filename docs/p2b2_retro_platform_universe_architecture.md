# RVDB Phase 2B — P2B2

## Retro Platform Universe Architecture Specification

# Status

PLANNING

---

# Objective

Define the architecture required for RVDB to catalog the complete retro
platform universe while distinguishing platforms that are currently
playable/emulatable from platforms retained for historical and educational
purposes.

The architecture must support both operational use by RetroVault and
historical preservation within RVDB.

The architecture must not restrict RVDB to platforms that are currently
playable.

---

# Core Catalog Principle

RVDB catalogs retro platforms as identifiable systems.

A platform may qualify for the catalog because:

1. it is currently playable/emulatable through a defensible emulator
   implementation, or
2. it is historically significant and retained for knowledge,
   preservation, documentation, images, videos, or related historical
   material.

Historical significance alone does not make a platform playable.

Emulator/frontend listings alone do not automatically establish a new
canonical platform entity.

---

# Playable Platform Principle

A platform is considered playable/emulatable only when an associated
emulator implementation provides a defensible means of running software,
games, applications, demonstrations, or other native content for that
platform.

The evidence should identify an actual emulator implementation, emulator
core, or equivalent emulation implementation.

Frontend listing alone is insufficient.

A platform does not need to have perfect emulation to qualify as playable.

The architecture must therefore distinguish:

- playable
- playable with limitations
- experimental
- historical-only
- unknown / insufficient evidence

---

# Historical Platform Principle

Historical platforms remain valid RVDB entities even when no usable
emulator is currently known.

Historical-only entities may contain:

- historical descriptions
- photographs
- screenshots
- advertisements
- videos
- surviving software information
- documentation
- manufacturer information
- release information
- historical relationships

Historical-only status must not imply that RetroVault can launch the
platform.

---

# Platform Identity

The canonical platform entity remains the fundamental hardware/system
identity.

Platform identity must be independent of:

- a specific emulator
- a specific frontend
- a specific emulator core
- a ROM format
- a particular software title
- a particular hardware revision unless an explicit entity-boundary
  decision establishes it as a separate platform

---

# Emulator Entity

RVDB should support a canonical emulator entity type.

An emulator represents software whose purpose includes emulating a
platform or family of platforms.

An emulator entity is distinct from:

- platform
- frontend
- libretro core
- game
- software title
- media format

Potential emulator metadata may include:

- canonical ID
- name
- aliases
- project
- supported platforms
- operating-system availability
- architecture availability
- version information
- official website
- source repository
- license
- status

Only fields justified by the eventual schema contract should become
production metadata.

---

# Libretro Core Entity

RVDB should retain a distinct core entity type.

A libretro core is an implementation loaded by a libretro frontend.

The existing RVDB core entity model should be extended only after its
contract is explicitly reviewed.

A core may represent:

- console emulation
- computer emulation
- arcade emulation
- handheld emulation
- game-engine execution
- application execution
- other software exposed through the libretro API

Core identity must not automatically become platform identity.

---

# Frontend Entity

RVDB should support a distinct frontend entity type.

Examples include:

- RetroArch
- EmulationStation
- EmulationStation-DE
- Batocera
- RetroPie
- Recalbox
- EmuDeck
- LaunchBox

A frontend is not itself necessarily an emulator.

A frontend may launch:

- standalone emulators
- libretro cores
- engines
- applications
- platform-specific tools

Frontend support therefore must not be used as the sole definition of
platform playability.

---

# Platform / Emulator Relationship

The architecture should support a relationship equivalent to:

`platform -> supported_by_emulator`

This relationship represents that a specific emulator provides emulation
support for a platform.

It must be distinct from frontend support.

---

# Platform / Core Relationship

The existing:

`supports_core`

relationship remains the canonical platform-to-core relationship unless
a later schema review deliberately replaces it.

A relationship should only be populated when:

1. the core entity exists,
2. the platform entity exists,
3. the relationship has been independently researched, and
4. the relationship can be validated against canonical RVDB entities.

No speculative relationships should be created.

---

# Emulator / Core Relationship

The architecture should distinguish a standalone emulator from a
libretro core derived from, based on, or implementing related emulator
technology.

The exact relationship vocabulary remains subject to schema design.

No relationship should be invented until the entity model is finalized.

---

# Frontend / Emulator Relationship

The architecture should permit a frontend to identify the emulators it
can launch or integrate.

This relationship must remain distinct from platform emulation support.

---

# Frontend / Core Relationship

The architecture should permit a frontend to identify compatible
libretro cores where applicable.

This is particularly important for RetroArch and frontend distributions
that integrate libretro cores.

---

# Playability Model

Playability must not be represented solely by a Boolean.

The architecture should distinguish at minimum:

- `playable`
- `playable_limited`
- `experimental`
- `historical_only`
- `unknown`

The final controlled vocabulary must be established through the formal
schema design checkpoint.

---

# Emulation Quality

Emulation quality must be separate from playability.

A playable system may have:

- mature emulation
- high compatibility
- minor known issues
- significant limitations
- experimental support

The architecture must not require perfect emulation before a platform can
be classified as playable.

---

# Evidence Principle

Every operational playability claim should eventually be traceable to
evidence.

Evidence may include:

- official emulator documentation
- official core documentation
- official emulator compatibility documentation
- official project repositories
- authoritative emulator system lists
- documented software lists
- documented supported systems

Frontend listings may be useful discovery sources but should not
automatically establish canonical platform identity or playability.

---

# Major Ecosystem Coverage

The eventual platform census should investigate at minimum:

- RetroArch / Libretro
- Batocera
- RetroPie
- Recalbox
- EmulationStation
- EmulationStation-DE
- EmuDeck
- LaunchBox
- MAME
- ScummVM
- DOSBox
- PCem
- 86Box
- VICE
- WinUAE
- FS-UAE
- and specialized standalone emulators

This is a research scope, not a declaration that every named ecosystem
creates unique platform entities.

---

# MAME / Multi-System Principle

MAME must not be treated as an arcade-only source.

MAME has expanded beyond its original arcade focus and documents and
emulates a broad range of vintage computers, consoles, calculators, and
other systems.

The census must therefore inspect MAME/MESS-derived system coverage for
non-arcade platforms.

---

# ScummVM Boundary

ScummVM must not automatically be treated as a collection of hardware
platforms.

Its engines execute supported software and game engines.

The eventual schema must distinguish:

- hardware platforms
- software environments
- game engines
- games
- emulators

ScummVM support should therefore inform the universe without
automatically turning every supported engine into a hardware platform.

---

# Arcade Boundary

Arcade hardware must be modeled carefully.

The architecture must distinguish, where appropriate:

- arcade platform/hardware
- arcade game
- arcade manufacturer
- arcade emulator
- arcade software set
- ROM set

A ROM set or individual arcade title must not automatically become a
platform.

---

# Computer Boundary

Computer platforms are first-class RVDB platforms.

This includes, where emulatable or historically significant:

- home computers
- personal computers
- educational computers
- business computers
- workstation-class systems
- mainframe gaming experiments
- specialized computer systems

Computer systems must not be excluded merely because they were not
marketed primarily as game consoles.

---

# Early Historical Systems

The universe must permit historically significant systems from before
the conventional console-generation model.

This includes early experimental electronic gaming systems and early
mainframe/computer gaming experiments beginning in the 1950s and
continuing through the 1960s and 1970s.

Generation metadata must not be required for these systems.

---

# Generation Model

Generation should be treated as metadata rather than as the fundamental
platform identity.

The architecture must permit:

- pre-generation / experimental
- first generation
- second generation
- third generation
- fourth generation
- fifth generation
- sixth generation
- seventh generation

A platform may also exist outside the console-generation framework.

Generation assignment must be based on explicit catalog policy rather than
being inferred solely from release year.

---

# Hardware Revisions

Hardware revisions must not automatically become separate platform
entities.

A revision should remain inside the canonical platform boundary unless an
explicit entity-boundary decision establishes independent platform status.

This preserves the policy already applied to SC-3000H.

---

# Regional Variants

Regional variants must not automatically become separate platform
entities.

Separate regional entities require an explicit canonical boundary
decision.

Regional naming may instead be represented through aliases or future
normalized regional metadata where justified.

---

# Compatible / Clone Hardware

Compatible hardware and clones require explicit entity-boundary review.

A compatible system must not automatically be merged with the original
platform.

A clone must not automatically become a separate platform solely because
it has a different manufacturer.

The final policy must distinguish:

- revision
- regional variant
- compatible hardware
- clone
- licensed hardware
- substantially different platform

---

# Media and Software Formats

Media formats and software-image extensions are not platforms.

RVDB should preserve the distinction between:

- physical media
- software-image format
- archive/container format
- emulator-specific format
- frontend packaging

A generic archive extension must not automatically become a canonical
platform extension.

---

# BIOS / Firmware

BIOS and firmware requirements must eventually be represented separately
from platform identity.

A platform may require:

- BIOS
- firmware
- ROM system files
- machine-specific configuration
- other required system assets

These requirements must not be encoded as platform identity.

---

# Software / Game / Demo Boundary

Games, applications, demos, utilities, and other software are not
automatically platforms.

A software title should become a separate entity when supported by the
appropriate RVDB entity model.

A software engine should not automatically become a hardware platform.

---

# RetroVault Operational Use

RetroVault should eventually be able to query RVDB for operationally
playable systems.

Examples:

- platforms playable through RetroArch
- platforms supported by a particular core
- platforms supported by a particular standalone emulator
- platforms available through a particular frontend
- platforms with mature emulation
- platforms requiring BIOS
- platforms supporting a particular media format

Historical-only entities must remain available to the knowledge and
historical portions of RetroVault without appearing as launchable systems.

---

# Historical Presentation

Historical-only platforms may expose:

- photographs
- screenshots
- videos
- advertisements
- manuals
- historical descriptions
- surviving software information
- timelines
- manufacturer information

Historical presentation must remain independent of operational
playability.

---

# Census Principle

The eventual global census must not begin by assuming a fixed number of
platforms.

The final count will emerge from:

1. platform discovery,
2. canonical entity-boundary decisions,
3. duplicate elimination,
4. emulator verification,
5. historical verification,
6. normalization,
7. validation.

Multiple emulator names or frontend names for the same hardware platform
must not create duplicate platform entities.

---

# Discovery Sources

The census should use multiple independent discovery layers.

Primary discovery sources should include official project documentation
and official project repositories where available.

Secondary discovery sources may be used to identify candidates requiring
verification.

A candidate discovered in one ecosystem should not become canonical until
its identity and status are independently justified.

---

# Duplicate Prevention

The architecture must prevent duplicate platform records caused by:

- alternate names
- regional names
- emulator naming
- frontend naming
- core naming
- hardware revisions
- filename conventions
- ROM-set naming
- manufacturer naming differences

Canonical IDs remain stable even when aliases or ecosystem names differ.

---

# Unknown / Insufficient Evidence

The architecture must provide a controlled way to represent uncertainty.

Insufficient evidence must not be silently converted into:

- playable
- historical
- emulator-supported
- core-supported

Unknown status is preferable to an invented assertion.

---

# Controlled Expansion

The project must continue using controlled population checkpoints.

Large-scale census work must be divided into reviewable batches.

Each batch should follow:

1. research
2. planning
3. review
4. production creation
5. regression update
6. validation
7. milestone update
8. commit
9. push

No uncontrolled mass import should be performed.

---

# Schema Change Requirement

No production entity should begin using new architecture fields until:

1. the P2B2 architecture specification is accepted,
2. the affected entity schemas are explicitly designed,
3. validators are updated,
4. tests are added,
5. migration/backward-compatibility requirements are reviewed,
6. the implementation is committed separately from large-scale data
   population.

---

# Initial Entity Model Direction

The anticipated long-term entity universe may include:

- platform
- emulator
- core
- frontend
- manufacturer
- developer
- publisher
- game
- genre
- media
- BIOS / firmware
- software format
- controller
- artwork
- shader
- overlay
- collection
- historical record
- source / evidence

This list is architectural direction only.

No new entity type is authorized for production until its contract has
been explicitly designed and reviewed.

---

# P2B2 Decision

Recommended decision:

**ACCEPT FOR ARCHITECTURAL DESIGN**

The current RVDB platform model is suitable as the foundation, but it is
not sufficient by itself for the complete Retro Platform Universe.

The architecture must be expanded before the global platform census is
performed.

---

# P2B2 Boundary

P2B2 defines the conceptual architecture.

P2B2 does not authorize:

- new production platform entities
- bulk platform imports
- emulator population
- core population
- frontend population
- schema implementation
- mass metadata changes

Those require subsequent controlled checkpoints.

---

# Next Checkpoint

P2B3 — Emulator / Core / Frontend Entity Architecture

The next checkpoint should define the concrete entity contracts and
relationships required to implement the architecture established by P2B2.

No production data expansion should begin until the required architecture
is accepted and implemented through controlled schema/test checkpoints.
