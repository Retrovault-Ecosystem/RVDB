# RVDB Phase 2B — P2B3

## Emulator / Core / Frontend Entity Architecture

---

# Status

PLANNING

---

# Objective

Define the concrete RVDB entity and relationship architecture required to
represent:

- canonical retro platforms
- standalone emulators
- Libretro cores
- frontends
- emulator/platform compatibility
- core/platform compatibility
- frontend/emulator relationships
- frontend/core relationships where justified
- playability evidence
- emulator/core version compatibility
- historical-only systems

P2B3 is an architecture checkpoint.

It does not authorize bulk production population.

---

# Architectural Foundation

P2B2 established that the complete Retro Platform Universe cannot be
represented safely by platform entities alone.

The long-term model must distinguish:

- what the platform is
- what emulator can emulate it
- what Libretro core can emulate it
- what frontend can launch or expose it
- whether the resulting system is actually playable
- what evidence supports that claim
- whether the system is operational or historical-only

The distinction is mandatory.

---

# Platform Independence

A platform entity represents the canonical system being emulated.

The platform identity must remain independent of:

- emulator
- Libretro core
- frontend
- ROM format
- software title
- BIOS file
- artwork
- shader
- controller
- launcher
- compatibility frontend
- operating-system installation method

An emulator must never cause a duplicate platform entity to be created.

A core must never cause a duplicate platform entity to be created.

A frontend must never cause a duplicate platform entity to be created.

---

# Emulator Entity

An emulator entity represents a software emulator capable of reproducing
one or more hardware systems.

Examples include:

- MAME
- Dolphin
- PCSX2
- DuckStation
- PPSSPP
- DOSBox
- PCem
- 86Box
- VICE
- WinUAE
- FS-UAE
- ScummVM

The emulator entity is software infrastructure, not hardware.

---

# Emulator Identity

An emulator should have a canonical identifier independent of:

- executable filename
- package name
- frontend display name
- distribution package name
- platform-specific installation name

Canonical identity should survive:

- Linux packaging changes
- Windows packaging changes
- Flatpak naming
- AppImage naming
- distribution-specific package names
- frontend-specific aliases

---

# Emulator Fields

The proposed Emulator Entity Contract should support, subject to schema review:

- canonical ID
- entity type
- canonical name
- aliases
- developer/project
- supported platforms
- supported cores where applicable
- operating systems
- official website
- source repository
- status
- evidence

No field should be added to production until its schema contract is
explicitly reviewed.

---

# Emulator Status

The architecture should distinguish software status from playability.

Possible emulator status values may include:

- active
- maintenance
- archived
- discontinued
- experimental
- unknown

Emulator status must not be used as a substitute for platform playability.

---

# Core Entity

A core represents an emulator implementation exposed through a core-based
framework.

The primary example is a Libretro core used by RetroArch.

The existing RVDB core schema is currently minimal and contains a platform
support relationship.

P2B3 should expand that contract deliberately rather than treating the
current minimal schema as final.

---

# Core Identity

A core must have a canonical identity independent of:

- downloaded filename
- frontend display label
- package filename
- operating-system package name
- historical repository name
- version suffix

Examples of distinctions that may require separate core entities include
different emulator implementations or materially different core projects.

Version changes alone should not automatically create a new core entity.

---

# Core Fields

The proposed Core Entity Contract should support, subject to schema review:

- canonical ID
- entity type
- canonical name
- aliases
- emulator/project
- supported platforms
- status
- official source
- documentation source
- evidence

Version information should be modeled separately from core identity when
the architecture requires version-specific compatibility.

---

# Core and Emulator Relationship

A Libretro core is related to an emulator/project implementation.

However, the relationship must not assume that:

- every emulator has a Libretro core
- every Libretro core has a standalone emulator
- every core is merely a differently packaged standalone emulator

The relationship should explicitly support the distinction between:

- standalone emulator
- emulator-derived Libretro core
- independent Libretro implementation
- multi-system core
- experimental/test core

---

# Frontend Entity

A frontend represents software that organizes and launches emulation
content or emulator applications.

Examples include:

- RetroArch
- EmulationStation
- EmulationStation-DE
- Batocera
- RetroPie
- Recalbox
- EmuDeck
- LaunchBox

The frontend entity is not itself a platform.

---

# Frontend Boundary

A frontend may:

- discover systems
- display systems
- associate ROMs with systems
- launch emulators
- launch cores
- provide metadata
- provide artwork
- provide configuration
- manage BIOS files
- expose compatibility information

None of those functions automatically establish platform identity.

---

# Frontend vs Emulator

A frontend and emulator are distinct entity types.

A frontend may launch:

- one emulator
- many emulators
- one core
- many cores
- a mixture of standalone emulators and cores

Therefore frontend support must not be represented merely as a platform
relationship.

---

# Frontend Fields

The proposed Frontend Entity Contract should support, subject to schema
review:

- canonical ID
- entity type
- canonical name
- aliases
- developer/project
- operating systems
- supported launch mechanisms
- official website
- source repository
- status
- evidence

---

# Platform / Emulator Relationship

The architecture should define a relationship equivalent to:

platform -> supported_by_emulator -> emulator

This relationship answers:

"Which emulator can emulate this platform?"

The inverse query must answer:

"Which platforms can this emulator emulate?"

---

# Platform / Core Relationship

The architecture should define:

platform -> supports_core -> core

This relationship answers:

"Which core can emulate this platform?"

The inverse query must answer:

"Which platforms are supported by this core?"

The existing platform schema already contains supports_core.

P2B3 must preserve compatibility with the existing relationship model unless
a controlled schema migration explicitly replaces it.

---

# Emulator / Core Relationship

The architecture should define an explicit relationship only where evidence
supports it.

Possible semantic forms include:

- implements
- derived_from
- exposes_as_core
- bundled_core

No relationship should be inferred solely because a core has a similar
name to an emulator.

---

# Frontend / Emulator Relationship

The architecture should support:

frontend -> launches_emulator -> emulator

This records that a frontend can launch or integrate with a standalone
emulator.

The relationship should not imply that the frontend developed the emulator.

---

# Frontend / Core Relationship

The architecture should support:

frontend -> launches_core -> core

This is particularly important for RetroArch-family workflows and frontends
that invoke Libretro cores directly.

---

# Frontend / Platform Relationship

A direct frontend -> platform relationship should be avoided as the primary
compatibility mechanism.

A frontend may list a platform because it has configuration or scraping
support without proving that an actual emulator/core can execute content
for that platform.

Operational compatibility should instead resolve through:

frontend
-> emulator/core
-> platform

---

# Playability Model

P2B2 established these controlled values:

- playable
- playable_limited
- experimental
- historical_only
- unknown

P2B3 must define where those values belong.

Playability is a property of a compatibility relationship or compatibility
claim, not necessarily a permanent property of the platform itself.

A platform can therefore be:

- playable through one emulator
- experimental through another
- historical-only when no valid emulator exists

The architecture must preserve those distinctions.

---

# Relationship-Level Playability

The preferred architecture is to associate compatibility evidence and
playability with the relevant relationship.

For example:

platform
-> emulator compatibility
-> playability
-> evidence

and:

platform
-> core compatibility
-> playability
-> evidence

This avoids incorrectly declaring an entire platform universally playable
because one emulator has partial support.

---

# Evidence

Operational compatibility claims require evidence.

Evidence may come from:

- official emulator documentation
- official core documentation
- official compatibility lists
- official frontend system documentation
- project source repositories
- authoritative compatibility databases
- reproducible project documentation

Frontend presence alone is insufficient.

A system appearing in a frontend menu does not prove that an emulator/core
can actually run it.

---

# Compatibility Evidence

Compatibility evidence should eventually support:

- source
- URL or source reference
- date checked
- emulator/core version where relevant
- platform
- compatibility claim
- notes
- confidence

The exact evidence schema requires a later controlled design checkpoint.

---

# Version Compatibility

Version information matters because emulator support changes over time.

The architecture should therefore permit:

platform + emulator + version + compatibility state

and:

platform + core + version + compatibility state

without creating duplicate platform entities for each emulator version.

---

# Version Identity Rule

A new emulator release must not create:

- a new platform
- a new emulator identity
- a new core identity

unless the software project itself has materially changed identity.

Normal releases belong to versioned compatibility/evidence data.

---

# Multi-System Emulators

Some emulators represent many hardware systems.

Examples include:

- MAME
- MESS-derived systems
- VICE families
- multi-system emulator suites
- multi-system cores

A multi-system emulator must therefore have many platform relationships.

The platform remains canonical and singular.

---

# MAME Boundary

MAME requires special treatment.

MAME is a multi-system emulator rather than a single hardware platform.

MAME compatibility should not result in one "MAME platform" replacing the
individual emulated systems.

Individual arcade and computer systems represented by MAME require their own
canonical platform identities when they meet RVDB platform criteria.

MAME itself remains an emulator entity.

---

# Arcade Boundary

Arcade hardware requires additional care.

An arcade title, cabinet, board, system, and emulator are not automatically
the same entity.

P2B3 should establish the architecture necessary to distinguish:

- arcade platform/system
- arcade game/software
- emulator
- core
- ROM set
- clone
- machine variant

Detailed arcade population remains outside P2B3 production scope.

---

# ScummVM Boundary

ScummVM requires explicit treatment because it is primarily a game-engine
and adventure-game runtime rather than a traditional hardware emulator.

ScummVM should therefore not automatically create a hardware platform for
every supported game engine.

The architecture must permit software-engine or runtime relationships.

Detailed ScummVM modeling requires a later controlled checkpoint.

---

# DOS Boundary

DOSBox represents an emulated PC/DOS environment.

The architecture should distinguish:

- IBM PC-compatible platform
- DOS operating environment
- DOSBox emulator
- DOSBox core
- individual game/software entities

A DOS game must not automatically become a hardware platform.

---

# Computer Emulator Boundary

Computer systems require the same canonical-platform principle as consoles.

Examples include:

- PDP-1
- Apple II
- Commodore PET
- Commodore 64
- Atari 8-bit systems
- ZX Spectrum
- Amstrad CPC
- MSX
- PC-98
- X68000
- Amiga

An emulator relationship establishes how the system can be run.

It does not alter the platform's canonical identity.

---

# Historical Systems

A historical platform may exist without a verified operational emulator.

Such an entity may have:

- historical metadata
- photographs
- videos
- documentation
- manufacturer information
- release information
- software history

but must not appear as launchable in RetroVault unless operational
playability is separately established.

---

# RetroVault Launchability

RetroVault should consume only compatibility relationships that satisfy the
required operational criteria.

A historical-only platform must never become launchable merely because:

- it exists in RVDB
- it appears in a frontend database
- it has artwork
- it has a ROM folder name
- it has an emulator entry without verified compatibility

---

# RetroVault Compatibility Resolution

The eventual resolver should be able to answer:

1. What platforms exist?
2. Is the platform operationally playable?
3. Which emulators support it?
4. Which cores support it?
5. Which versions are appropriate?
6. Which frontend can launch the chosen emulator/core?
7. What BIOS or firmware is required?
8. What media/software formats are accepted?
9. What evidence supports the compatibility claim?

P2B3 defines the architecture needed for those queries.

---

# Frontend Catalogs

Frontend system lists should be treated as discovery sources.

Examples:

- Batocera system catalog
- RetroPie emulator/system configuration
- Recalbox system catalog
- EmulationStation metadata/system configuration
- EmulationStation-DE system definitions
- EmuDeck emulator integrations
- LaunchBox platform/emulator integrations

These sources can identify candidates.

They do not independently establish canonical identity or full playability.

---

# Libretro Catalog

The official Libretro core catalog is a major discovery source.

It can identify:

- core names
- systems/machines targeted by cores
- multi-system cores
- experimental cores
- game-engine cores
- DOS cores
- computer cores
- console cores
- arcade cores

Core discovery must still be normalized into canonical RVDB platform entities.

---

# Core Duplication Rule

Multiple cores supporting the same platform are expected.

For example:

platform
-> core A

platform
-> core B

platform
-> core C

does not mean three platforms exist.

It means three compatibility implementations exist.

---

# Emulator Duplication Rule

Multiple emulators supporting the same platform are expected.

For example:

platform
-> emulator A

platform
-> emulator B

platform
-> emulator C

does not create duplicate platform records.

---

# Frontend Duplication Rule

Multiple frontends exposing the same platform are expected.

Frontend support does not create duplicate platforms.

---

# Alias Normalization

Aliases must remain attached to the canonical entity they identify.

Examples of alias sources may include:

- manufacturer names
- regional names
- historical names
- common emulator names
- frontend system names
- abbreviations

An alias must not become a second canonical platform merely because one
frontend uses different terminology.

---

# Regional Variants

Regional naming differences should not automatically create separate
platform entities.

Separate regional hardware entities require an explicit canonical boundary
decision.

---

# Hardware Revisions

Hardware revisions should not automatically create separate platform
entities.

The platform boundary established by P2B2 remains authoritative unless a
future architecture checkpoint explicitly changes it.

---

# Clone Hardware

Compatible or clone hardware should not automatically become a canonical
platform.

The relationship between:

- original hardware
- compatible clone
- software compatibility
- emulator support

requires explicit normalization.

---

# Software vs Platform

Games, demos, applications, operating systems, and software engines must
not automatically become platform entities.

A platform is the system on which software operates.

Software identity requires its own future entity architecture.

---

# BIOS / Firmware

BIOS and firmware must be modeled independently from:

- platform
- emulator
- core
- frontend

A BIOS requirement may be attached to a compatibility relationship without
creating a duplicate platform.

Detailed BIOS schema is deferred.

---

# Media and Extensions

Media and software-image extensions remain platform/software metadata.

An extension must not be interpreted as proof that an emulator supports a
platform.

Actual compatibility evidence remains authoritative.

---

# Compatibility Confidence

P2B3 should prepare for compatibility confidence levels.

Possible future controlled values include:

- verified
- documented
- probable
- experimental
- unsupported
- unknown

These values require explicit schema design before production use.

They must not be mixed casually with the five P2B2 playability states.

---

# Unsupported Claims

The architecture must prevent claims such as:

- "frontend lists it, therefore playable"
- "ROM extension exists, therefore playable"
- "emulator name contains platform name, therefore supported"
- "core exists, therefore every game is supported"
- "historical hardware exists, therefore it is launchable"

These are insufficient evidence.

---

# Official Support vs Practical Compatibility

The architecture should distinguish:

- officially documented support
- experimentally supported
- community-reported support
- unknown support

A system may be practically usable without having strong official
documentation.

Such cases must be represented with appropriate evidence/confidence rather
than silently promoted to fully verified support.

---

# Platform Census Dependency

The global platform census must not begin until the P2B3 architecture is
accepted and the required schema/test work is completed.

This is necessary because the census will contain:

- consoles
- handhelds
- computers
- arcade systems
- multi-system emulator targets
- unusual machines
- early historical computers
- specialized game systems
- later generations
- systems with only limited emulator support

Without relationship architecture, those discoveries cannot be normalized
reliably.

---

# Production Safety

P2B3 does not authorize:

- mass platform imports
- mass emulator imports
- mass core imports
- mass frontend imports
- automatic conversion of frontend catalogs into RVDB entities
- automatic conversion of Libretro core lists into platform entities
- bulk compatibility assertions
- schema changes without separate review
- production migration without regression tests

---

# Schema Change Strategy

The implementation should proceed through controlled stages:

1. finalize Emulator Entity Contract
2. finalize Core Entity Contract
3. finalize Frontend Entity Contract
4. finalize relationship contract
5. finalize compatibility/evidence contract
6. update schemas
7. update validators
8. update relationship validation
9. add regression tests
10. validate backward compatibility
11. commit architecture implementation separately
12. only then begin controlled production population

---

# Existing RVDB Compatibility

Existing platform entities must continue to validate.

Existing fields such as:

- manufacturer
- release_year
- category
- media
- extensions
- supports_core

must not be broken by P2B3.

Any migration must be explicit and tested.

---

# Existing Core Schema

The current core schema is intentionally minimal.

It currently provides a platform support relationship.

P2B3 treats this as an architectural starting point, not a finished
production contract.

No assumptions should be made about fields that do not yet exist.

---

# Relationship Direction

The architecture should support deterministic forward and reverse queries.

Examples:

platform -> emulator

emulator -> platforms

platform -> core

core -> platforms

frontend -> emulator

emulator -> frontends

frontend -> core

core -> frontends

All relationship directions must resolve through canonical IDs.

---

# Relationship Validation

Every relationship must validate:

- target entity exists
- target entity has expected type
- relationship is permitted by schema
- duplicate references are rejected or normalized
- invalid references produce deterministic errors

---

# Relationship Symmetry

Where a relationship is represented in both directions, RVDB must define
which side is authoritative.

The system must not permit two conflicting declarations to silently
produce different graphs.

---

# Relationship Evidence

Compatibility relationships should eventually support evidence without
embedding uncontrolled prose into platform records.

Evidence should be normalized separately where practical.

---

# Versioned Evidence

When support depends on an emulator/core version, the evidence must retain
the relevant version.

This prevents a current compatibility claim from being incorrectly applied
to every historical release.

---

# Emulator Forks

Forks require explicit identity decisions.

A fork should become a separate emulator/core entity when it is independently
maintained and users can meaningfully select it as a distinct implementation.

A mere packaging fork should not automatically become a new canonical
emulator.

---

# Core Forks

Core forks require the same rule.

A renamed or rebuilt core is not automatically a distinct canonical core.

Identity requires a meaningful project distinction.

---

# Frontend Forks

Frontend forks follow the same canonical identity principle.

Packaging variants do not automatically become separate frontend entities.

---

# Official Source Preference

When multiple sources conflict, prefer:

1. official project documentation
2. official project repository
3. official compatibility database
4. authoritative emulator documentation
5. reputable secondary technical references
6. community sources for discovery and corroboration

Community claims must not silently override authoritative evidence.

---

# Discovery vs Authority

Discovery sources and authoritative sources have different roles.

A frontend catalog may discover a candidate.

An official emulator/core compatibility document should establish the
operational claim where available.

RVDB should preserve that distinction.

---

# RetroArch / Libretro

RetroArch is a frontend/reference frontend for the Libretro API.

Libretro cores are the actual emulator/game-engine implementations used to
run content.

RVDB therefore must not model RetroArch itself as the emulator for every
platform supported by its cores.

Instead:

RetroArch
-> launches_core
-> Libretro core
-> supports_core
-> platform

This is a critical architectural distinction.

---

# Batocera

Batocera should be modeled primarily as a frontend/distribution environment
for supported emulation systems.

Its system catalog is useful for discovery and compatibility research.

A Batocera system entry must not automatically become a platform entity
without canonical normalization.

---

# RetroPie

RetroPie is a distribution/configuration ecosystem built around
EmulationStation and emulators.

Its system definitions are discovery and integration evidence.

They are not canonical platform definitions by themselves.

---

# Recalbox

Recalbox is an emulation-focused operating environment/frontend ecosystem.

Its supported-system catalog can identify platform candidates and emulator
relationships.

Canonical RVDB identity remains independent.

---

# EmulationStation

EmulationStation and EmulationStation-DE are frontend entities.

They should not be confused with the emulators they launch.

---

# EmuDeck

EmuDeck is an integration/configuration ecosystem for emulators and related
tools.

It is not a canonical platform and should not create platform entities.

---

# LaunchBox

LaunchBox is a frontend/library-management ecosystem.

Its platform and emulator configuration can provide discovery information.

It does not define canonical RVDB platform identity.

---

# Small Emulator Ecosystems

The architecture must support specialized emulators that cover only one or
a few systems.

Examples include:

- single-console emulators
- single-computer emulators
- handheld-specific emulators
- arcade-system-specific emulators
- obscure historical-machine emulators

Small scope does not reduce their value as evidence.

---

# Early Historical Machines

The architecture must support early systems such as:

- PDP-1
- early research computers
- early programmable game systems
- early arcade hardware

where reliable emulator support exists.

If no emulator support exists, the platform may remain historical-only.

---

# Seventh Generation

The architecture must not artificially stop at fifth or sixth generation.

It must permit later systems including seventh-generation targets where
emulation exists and meets the RVDB playability/evidence rules.

Examples may include:

- PlayStation 3
- Xbox 360
- Nintendo Wii

Actual production inclusion remains dependent on verified emulator support.

---

# Eighth Generation Boundary

P2B3 does not establish a permanent exclusion of later systems.

However, the current user-defined retro scope is through seventh generation.

Any extension beyond that boundary requires an explicit future scope
decision.

---

# Experimental Systems

Experimental emulator support must remain distinguishable from fully
playable support.

An experimental emulator does not automatically make a platform
`playable`.

The compatibility relationship should carry the appropriate playability
state.

---

# Limited Support

A platform may be technically emulated while only a subset of software is
functional.

Such support should use:

`playable_limited`

when the evidence justifies it.

---

# Historical-Only State

`historical_only` means the entity is retained for knowledge and historical
presentation but does not have a qualifying operational compatibility path.

RetroVault must not present such an entity as launchable.

---

# Unknown State

`unknown` means insufficient evidence exists to classify operational
playability.

Unknown must not be treated as playable.

---

# Resolver Requirements

The future compatibility resolver should reject:

- missing emulator
- missing core
- invalid relationship
- unknown target entity
- historical-only relationship
- unsupported compatibility
- insufficient evidence

unless an explicit administrative/research mode requests the historical
record.

---

# RetroVault Modes

The eventual application architecture should support at least two logical
views:

## Operational View

Show systems that have qualifying emulator/core compatibility.

## Knowledge View

Show all canonical systems, including historical-only systems.

The same RVDB entity can therefore exist in both views while having different
operational visibility.

---

# Historical Presentation

Historical-only records may eventually expose:

- photographs
- videos
- advertisements
- manuals
- magazines
- technical documentation
- historical descriptions
- museum-style timelines

These assets do not make the platform operationally playable.

---

# No Forced Completeness

The architecture must not encourage filling every field simply because
the schema permits it.

Unknown information remains unknown.

Unsupported information remains omitted.

This preserves data quality.

---

# No False Precision

RVDB should prefer:

- explicit uncertainty
- evidence references
- controlled states
- omitted unsupported fields

over fabricated precision.

---

# P2B3 Production Boundary

P2B3 is an architecture checkpoint.

It authorizes design and review of the Emulator/Core/Frontend model.

It does not authorize production population.

No emulator, core, or frontend production census should begin until the
contracts and validation rules are accepted.

---

# P2B3 Decision

Recommended decision:

**ACCEPT FOR CONTRACT DESIGN**

The architecture established by P2B2 requires concrete Emulator, Core,
Frontend, compatibility, and evidence contracts before the global census can
begin.

---

# Next Checkpoint

P2B4 — Emulator / Core / Frontend Schema and Relationship Implementation

P2B4 should implement the contracts accepted through P2B3, update schemas
and validators, add regression coverage, and validate backward
compatibility.

Only after those implementation checkpoints are complete should RVDB begin
the controlled global emulator/platform census.

---

# Final Boundary

P2B3 establishes the architecture required to represent the emulator,
Libretro core, frontend, compatibility, evidence, and playability layers of
the Retro Platform Universe.

It does not authorize uncontrolled production expansion.

No production data expansion should begin until the P2B3 contracts are
accepted and implemented through controlled schema/test checkpoints.
