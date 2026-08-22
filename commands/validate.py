"""
=========================================================
RVDB Validation Command
=========================================================

Project:
    RetroVault Database (RVDB)

File:
    commands/validate.py

Purpose:
    Validates:

    - entity loading
    - schema compliance
    - relationship integrity

    Uses canonical project paths and therefore does not
    depend on the shell's current working directory.

Foundation Release:
    0.2

Checkpoint:
    C4 — Final Integration and Release Readiness

=========================================================
"""

import traceback

from engine.graph import build_graph
from engine.loader import EntityLoader
from engine.paths import DATA_ROOT

from validator.relationships import (
    RelationshipValidator,
)
from validator.schema import (
    SchemaValidator,
)


def cmd_validate():

    try:

        loader = EntityLoader(
            DATA_ROOT
        )

        entities = loader.load()

        if not entities:

            print(
                "Validation FAILED: No entities found"
            )

            return

        graph = build_graph(
            entities
        )

        schema_validator = (
            SchemaValidator()
        )

        relationship_validator = (
            RelationshipValidator()
        )

        schema_errors = []

        relationship_errors = []

        valid_count = 0

        for entity in entities:

            schema_result = (
                schema_validator.validate(
                    entity
                )
            )

            if schema_result.valid:

                valid_count += 1

            else:

                for error in (
                    schema_result.errors
                ):

                    schema_errors.append(
                        {
                            "entity":
                                entity.id,
                            "error":
                                error,
                        }
                    )

            relationships = entity.get(
                "relationships",
                {},
            )

            for (
                relationship,
                targets,
            ) in relationships.items():

                if not isinstance(
                    targets,
                    list,
                ):

                    continue

                for target_id in targets:

                    target = (
                        graph.nodes.get(
                            target_id
                        )
                    )

                    if target is None:

                        relationship_errors.append(
                            {
                                "entity":
                                    entity.id,
                                "error":
                                    (
                                        "Missing target "
                                        "entity: "
                                        f"{target_id}"
                                    ),
                            }
                        )

                        continue

                    result = (
                        relationship_validator
                        .validate(
                            entity,
                            relationship,
                            target,
                        )
                    )

                    if not result.valid:

                        for error in (
                            result.errors
                        ):

                            relationship_errors.append(
                                {
                                    "entity":
                                        entity.id,
                                    "error":
                                        error,
                                }
                            )

        print()

        print(
            "RVDB VALIDATION"
        )

        print(
            "----------------"
        )

        print(
            f"Entities checked: "
            f"{len(entities)}"
        )

        print(
            f"Valid: {valid_count}"
        )

        print(
            f"Schema Errors: "
            f"{len(schema_errors)}"
        )

        print(
            f"Relationship Errors: "
            f"{len(relationship_errors)}"
        )

        if schema_errors:

            print()

            print(
                "SCHEMA ERRORS"
            )

            print(
                "--------------"
            )

            for error in schema_errors:

                print(
                    f"{error['entity']}: "
                    f"{error['error']}"
                )

        if relationship_errors:

            print()

            print(
                "RELATIONSHIP ERRORS"
            )

            print(
                "-------------------"
            )

            for error in (
                relationship_errors
            ):

                print(
                    f"{error['entity']}: "
                    f"{error['error']}"
                )

        if (
            not schema_errors
            and not relationship_errors
        ):

            print()

            print(
                "Validation OK"
            )

    except Exception as error:

        print()

        print(
            "Validation FAILED:"
        )

        print(
            repr(
                error
            )
        )

        traceback.print_exc()
