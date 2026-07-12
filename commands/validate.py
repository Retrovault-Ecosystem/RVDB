from engine.loader import load_entities, get_load_errors
from engine.graph import build_graph

from validator.schema import validate_entity
from validator.relationships import validate_relationships


def cmd_validate():

    try:

        entities = load_entities()

        load_errors = get_load_errors()

        if load_errors:

            print("\nYAML ERRORS")
            print("-----------")

            for error in load_errors:

                print(error["file"])
                print(error["error"])
                print()

            print("Validation FAILED")
            return


        if not entities:

            print("Validation FAILED: No entities found")
            return


        graph = build_graph(entities)


        valid_count = 0

        schema_errors = []
        relationship_errors = []


        for entity in entities:


            valid, message = validate_entity(entity)


            if valid:

                valid_count += 1

            else:

                schema_errors.append(
                    {
                        "entity": entity.get(
                            "id",
                            "UNKNOWN"
                        ),
                        "error": message
                    }
                )


            rel_errors = validate_relationships(
                entity,
                graph
            )


            for error in rel_errors:

                relationship_errors.append(
                    {
                        "entity": entity.get(
                            "id",
                            "UNKNOWN"
                        ),
                        "error": error
                    }
                )


        print("\nRVDB VALIDATION")
        print("----------------")

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

            print("\nSCHEMA ERRORS")
            print("--------------")

            for error in schema_errors:

                print(
                    f"{error['entity']}: "
                    f"{error['error']}"
                )


        if relationship_errors:

            print("\nRELATIONSHIP ERRORS")
            print("-------------------")

            for error in relationship_errors:

                print(
                    f"{error['entity']}: "
                    f"{error['error']}"
                )


        if not schema_errors and not relationship_errors:

            print("\nValidation OK")


    except Exception as e:

        print(
            "Validation FAILED:",
            e
        )
