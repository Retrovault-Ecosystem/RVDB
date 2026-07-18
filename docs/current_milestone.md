# RVDB Current Milestone

_Last Updated: 2026-07-16_

---

# Project

RetroVault Database (RVDB)

Repository Branch:

feature/relationship-resolver

Project Status:

Phase 1.6 — Interactive Entity Builder

---

# Last Completed Milestone

✔ Entity Architecture

✔ Validation Engine (v1)

✔ Relationship Resolver

✔ Reverse Relationship Index

✔ Entity Templates

✔ Entity Factory

✔ Namespace ID Generator

✔ Canonical ID Migration Framework

✔ Create CLI Workflow

✔ Interactive Platform Entity Builder

✔ Entity Preview & Save Confirmation

✔ Typed Relationship Resolution

✔ Entity Registry Foundation

✔ Schema Engine Design (Milestone 1.9 Planning)

---

# Current State

The interactive Platform Builder is operational.

Current workflow:

CLI
→ EntityBuilder
→ IDGenerator
→ EntityFactory
→ YAML output

Interactive command:

python3 cli.py create platform

Automatically generates:

- Canonical RVDB ID
- Template-based entity
- YAML output

---

# Next Milestone

## Milestone 1.9 — Schema Engine

Goal:

Replace hardcoded validation and builders with a schema-driven architecture.

Phase 1

✔ Build SchemaLoader

Phase 2

• Merge common + entity schemas

Phase 3

• Replace SchemaValidator with dynamic validation

Phase 4

• Connect Entity Registry to SchemaLoader

Phase 5

• Build Generic Entity Builder

Future Goal

Every entity type should be defined entirely through YAML schemas.

Adding a new entity type should require:

- One schema
- One template

No new Python builder.

## Entity Builder Improvements

1. Add Entity Preview before saving

2. Ask for confirmation

   Save entity? (Y/n)

3. Add relationship lookup

Example:

Manufacturer:
Sega

↓

manufacturer.sega

4. Expand builders

- Game Builder
- Developer Builder
- Publisher Builder
- Core Builder
- Genre Builder

---

# Current Architecture

Completed

✔ Validation

✔ Search

✔ Query

✔ Relationships

✔ Reverse Relationships

✔ Entity Templates

✔ Entity Factory

✔ Canonical IDs

✔ Migration Framework

✔ Interactive Builder

Next major focus:

Developer productivity tools.

---

# Design Decisions

Canonical IDs use dot notation.

Examples:

platform.sega.genesis

game.super.mario.world

developer.nintendo.ead

genre.role.playing.game

No underscores in canonical IDs unless explicitly preserved through ID overrides.

Interactive builders should always:

Generate IDs automatically.

Show a preview.

Ask for confirmation before writing files.

---

# Architectural Decisions

RVDB follows a data-driven architecture.

Core Principles

1. Schemas define entities.
   Python should not hardcode entity fields.

2. The Entity Registry is the single source of truth
   for loaded entities.

3. Relationship resolution is registry-based.

4. Builders are generic whenever possible.

5. Validation is schema-driven.

6. YAML is the canonical representation of RVDB data.

7. Future applications (CLI, GUI, Web API, Documentation)
   should consume the same schemas rather than maintaining
   separate definitions.

Long-term Vision

RVDB is evolving from a YAML database into the
knowledge layer for the entire RetroVault ecosystem.

# End-of-Session Notes

Working tree should be clean before ending each session.

Commit after every completed milestone.

Avoid committing temporary test entities.

---

# Resume Instructions

To continue development, use the prompt:

Continue RVDB Project.

Read docs/current_milestone.md and continue from the current milestone.

Continue methodically with small, tested improvements.
