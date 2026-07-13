import json
import os


class JSONExporter:

    def export(
        self,
        database,
        output="dist/rvdb.json"
    ):

        os.makedirs(
            os.path.dirname(output),
            exist_ok=True
        )

        with open(output, "w") as f:
            json.dump(
                database,
                f,
                indent=4
            )

        return output
