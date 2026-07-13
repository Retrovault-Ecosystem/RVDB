import json
import os
from datetime import datetime


class ManifestBuilder:

    def build(
        self,
        registry,
        output="dist/manifest.json"
    ):

        os.makedirs(
            os.path.dirname(output),
            exist_ok=True
        )

        manifest = {

            "generated": datetime.utcnow().isoformat(),

            "games": registry.count("games"),
            "platforms": registry.count("platforms"),
            "developers": registry.count("developers"),
            "publishers": registry.count("publishers"),
            "genres": registry.count("genres"),
            "regions": registry.count("regions"),

        }

        with open(
            output,
            "w"
        ) as f:

            json.dump(
                manifest,
                f,
                indent=4
            )

        return output
