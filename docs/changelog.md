# RVDB Changelog

## Foundation 0.2.1 — Release Hardening

### Legacy Cleanup

- Removed obsolete backup artifacts.
- Removed superseded validator modules and obsolete validator tests.
- Untracked the accidentally committed root virtual environment.
- Migrated the active build pipeline away from retired legacy runtime code.
- Retired unused legacy exporters, build modules, query components, loader tests,
  and the historical inner `rvdb/` runtime.
- Retired obsolete ID migration scaffolding.
- Retired historical Phase-D scaffolding.
- Removed empty root skeleton files.
- Normalized the `services` package.

### Runtime and Release Metadata

- Corrected the canonical runtime version to `0.2.1`.
- Defined the runtime dependency contract as `PyYAML>=6.0`.
- Added the canonical project README.
- Verified `pytest` remains a development-only dependency.

### Reproducibility

- Fast-forwarded `develop` to the completed Foundation implementation.
- Verified a true clean clone from the default GitHub branch.
- Verified isolated `.venv` creation from a clean clone.
- Verified runtime installation from `requirements.txt`.
- Verified the canonical build does not dirty the repository.

### Verified Foundation Baseline

RVDB version         : 0.2.1
Entities checked     : 19
Valid entities       : 19
Schema Errors        : 0
Relationship Errors  : 0
Graph Nodes          : 19
Graph Edge Entries   : 19
Regression Tests     : 110 passing
Clean Clone          : PASS
Canonical Branch     : develop

### Status

Foundation 0.2.1 is in final release hardening.

Architectural feature work and large-scale database expansion remain deferred
until the Foundation 0.2.1 release-hardening sequence is complete.

---


## 2026-07-15

### Entity Architecture Stabilization

#### Added

- Entity object abstraction
- Improved YAML entity loading
- Relationship graph engine
- Reverse relationship indexing
- Relationship resolver
- Schema validation improvements
- Relationship validation improvements
- CLI validation improvements


#### Validation Results

    Entities checked: 16
    Schema Errors: 0
    Relationship Errors: 0


#### Build Results

    Graph Nodes : 15
    Graph Edges : 15


#### Status

RVDB foundation is stable.

The database engine now supports:

- Entity loading
- Entity resolution
- Relationship traversal
- Validation
- Search
- Query operations
- Build generation

---

## Phase 1.5 Started

### Added

* RVDB entity template system
* Standardized entity creation workflow
* Expansion framework preparation

### Purpose

Prepare RVDB for large-scale database expansion while maintaining validation and consistency.

### Notes

Entity templates introduce the future RVDB expansion model.

Some template fields will become available as the schema system evolves.

---

## Entity Factory Added

### Added

* RVDB Entity Factory engine module
* Template-based entity generation
* YAML entity creation foundation


### Validation

```text
python3 -m compileall engine
PASS
```

### Purpose

Prepare RVDB for automated database expansion and future CLI entity creation.
