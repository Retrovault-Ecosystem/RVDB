import os
import yaml


class ValidationError:

    def __init__(
        self,
        file,
        message
    ):
        self.file = file
        self.message = message

    def __str__(self):
        return f"{self.file}: {self.message}"


class RVDBValidator:

    def __init__(
        self,
        schema_path="schemas/entities"
    ):
        self.schema_path = schema_path
        self.errors = []


    def load_schema(
        self,
        entity_type
    ):

        path = os.path.join(
            self.schema_path,
            f"{entity_type}.yaml"
        )

        if not os.path.exists(path):

            raise FileNotFoundError(
                f"Schema missing: {path}"
            )

        with open(path, "r") as file:

            return yaml.safe_load(file)


    def validate_entity(
        self,
        entity_type,
        filepath
    ):

        schema = self.load_schema(
            entity_type
        )

        with open(
            filepath,
            "r"
        ) as file:

            data = yaml.safe_load(file)


        required = schema.get(
            "required",
            []
        )


        for field in required:

            if field not in data:

                self.errors.append(
                    ValidationError(
                        filepath,
                        f"Missing required field: {field}"
                    )
                )


        fields = schema.get(
            "fields",
            {}
        )


        for field, rules in fields.items():

            if field not in data:

                continue


            expected = rules.get(
                "type"
            )

            value = data[field]


            if expected == "string":

                if not isinstance(value, str):

                    self.errors.append(
                        ValidationError(
                            filepath,
                            f"{field} must be a string"
                        )
                    )


            elif expected == "integer":

                if not isinstance(value, int):

                    self.errors.append(
                        ValidationError(
                            filepath,
                            f"{field} must be an integer"
                        )
                    )


            elif expected == "boolean":

                if not isinstance(value, bool):

                    self.errors.append(
                        ValidationError(
                            filepath,
                            f"{field} must be a boolean"
                        )
                    )


            elif expected == "list":

                if not isinstance(value, list):

                    self.errors.append(
                        ValidationError(
                            filepath,
                            f"{field} must be a list"
                        )
                    )


        return len(self.errors) == 0



    def validate_directory(
        self,
        entity_type,
        directory
    ):

        results = []


        for filename in sorted(
            os.listdir(directory)
        ):

            if filename.endswith(".yaml"):

                filepath = os.path.join(
                    directory,
                    filename
                )


                valid = self.validate_entity(
                    entity_type,
                    filepath
                )


                results.append(
                    valid
                )


        return all(results)



    def report(self):

        if not self.errors:

            print(
                "✓ Validation successful"
            )

            return


        print(
            "RVDB Validation Errors"
        )

        print(
            "======================"
        )


        for error in self.errors:

            print(error)



def validate_all():

    validator = RVDBValidator()


    validator.validate_directory(
        "platform",
        "data/platforms"
    )


    validator.validate_directory(
        "game",
        "data/games"
    )


    validator.validate_directory(
        "core",
        "data/cores"
    )


    validator.report()



if __name__ == "__main__":

    validate_all()
