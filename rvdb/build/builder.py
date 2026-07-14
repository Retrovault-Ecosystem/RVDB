import os
import json


from rvdb.registry import registry
from rvdb.loader import RVDBLoader
from rvdb.validator import RVDBValidator
from rvdb.linker import linker


from rvdb.build.indexer import SearchIndexer
from rvdb.build.manifest import ManifestBuilder
from rvdb.build.checksum import ChecksumBuilder



class RVDBBuilder:


    def __init__(
        self,
        data_directory="data"
    ):

        self.data_directory = data_directory



    def validate(self):

        validator = RVDBValidator()


        validator.validate_directory(
            "platform",
            os.path.join(
                self.data_directory,
                "platforms"
            )
        )


        validator.validate_directory(
            "game",
            os.path.join(
                self.data_directory,
                "games"
            )
        )


        validator.validate_directory(
            "core",
            os.path.join(
                self.data_directory,
                "cores"
            )
        )


        if validator.errors:

            validator.report()

            raise RuntimeError(
                "RVDB validation failed"
            )



    def load(self):

        loader = RVDBLoader()

        loader.load_all(
            self.data_directory
        )



    def link(self):

        linker.link_all_games()



    def index(self):

        print(
            "Building search indexes..."
        )


        indexer = SearchIndexer()


        return indexer.build(
            registry.all(
                "games"
            )
        )



    def manifest(self):

        print(
            "Building manifest..."
        )


        builder = ManifestBuilder()


        return builder.build(
            registry
        )



    def export_json(
        self,
        output="dist/rvdb.json"
    ):

        os.makedirs(
            os.path.dirname(output),
            exist_ok=True
        )


        database = {


            "games": [

                game.__dict__

                for game in registry.all(
                    "games"
                )

            ],



            "platforms": [

                platform.__dict__

                for platform in registry.all(
                    "platforms"
                )

            ],



            "developers": [

                developer.__dict__

                for developer in registry.all(
                    "developers"
                )

            ],



            "publishers": [

                publisher.__dict__

                for publisher in registry.all(
                    "publishers"
                )

            ],

        }



        with open(
            output,
            "w"
        ) as file:

            json.dump(
                database,
                file,
                indent=4
            )



        return output



    def checksums(
        self
    ):

        print(
            "Generating checksums..."
        )


        builder = ChecksumBuilder()


        return builder.build(
            [
                "dist/rvdb.json",
                "dist/search_index.json",
                "dist/manifest.json",
            ]
        )



    def build(self):


        print(
            "Validating RVDB..."
        )

        self.validate()



        print(
            "Loading entities..."
        )

        self.load()



        print(
            "Building relationships..."
        )

        self.link()



        print(
            "Building indexes..."
        )

        index_output = self.index()


        print(
            f"Generated: {index_output}"
        )



        print(
            "Exporting database..."
        )

        database_output = self.export_json()


        print(
            f"Generated: {database_output}"
        )



        manifest_output = self.manifest()


        print(
            f"Generated: {manifest_output}"
        )



        checksum_output = self.checksums()


        print(
            f"Generated: {checksum_output}"
        )


        return database_output
