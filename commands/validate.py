"""
RVDB Validation Command

Validates:
- entity loading
- schema compliance
- relationship integrity
"""

from engine.loader import EntityLoader
from engine.graph import build_graph

from validator.schema import SchemaValidator
from validator.relationships import RelationshipValidator

import traceback


def cmd_validate():

    try:

        loader = EntityLoader("data")

        entities = loader.load()


        if not entities:

            print(
                "Validation FAILED: No entities found"
            )

            return


        graph = build_graph(
            entities
        )


        schema_validator = SchemaValidator()
        relationship_validator = RelationshipValidator()


        schema_errors = []
        relationship_errors = []

        valid_count = 0


        for entity in entities:


            schema_result = schema_validator.validate(
                entity
            )


            if schema_result.valid:

                valid_count += 1

            else:

                for error in schema_result.errors:

                    schema_errors.append(
                        {
                            "entity": entity.id,
                            "error": error,
                        }
                    )


            relationships = entity.get(
                "relationships",
                {}
            )


            for relationship, targets in relationships.items():


                if not isinstance(
                    targets,
                    list
                ):
                    continue


                for target_id in targets:


                    target = graph.nodes.get(
                        target_id
                    )


                    if target is None:

                        relationship_errors.append(
                            {
                                "entity": entity.id,
                                "error":
                                f"Missing target entity: {target_id}"
                            }
                        )

                        continue


                    result = relationship_validator.validate(
                        entity,
                        relationship,
                        target
                    )


                    if not result.valid:

                        for error in result.errors:

                            relationship_errors.append(
                                {
                                    "entity": entity.id,
                                    "error": error,
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
            f"Entities checked: {len(entities)}"
        )

        print(
            f"Valid: {valid_count}"
        )

        print(
            f"Schema Errors: {len(schema_errors)}"
        )

        print(
            f"Relationship Errors: {len(relationship_errors)}"
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
                    f"{error['entity']}: {error['error']}"
                )


        if relationship_errors:

            print()
            print(
                "RELATIONSHIP ERRORS"
            )

            print(
                "-------------------"
            )


            for error in relationship_errors:

                print(
                    f"{error['entity']}: {error['error']}"
                )


        if not schema_errors and not relationship_errors:

            print()
            print(
                "Validation OK"
            )


    except Exception as e:

        print()
        print(
            "Validation FAILED:"
        )

        print(
            repr(e)
        )

        traceback.print_exc()
