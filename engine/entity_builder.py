import yaml

from engine.factory import EntityFactory
from engine.id_generator import IDGenerator
from engine.relationship_lookup import RelationshipLookup


class EntityBuilder:

    def __init__(self):

        self.factory = EntityFactory()

        self.lookup = RelationshipLookup()

    # =====================================================
    # Generic Builder Dispatcher
    # =====================================================

    def build(self, entity_type):

        if entity_type == "platform":
            return self.build_platform()

        print(
            f"No interactive builder available for '{entity_type}'."
        )

        return None

    # =====================================================
    # Resolve Relationship
    # =====================================================

    def resolve_relationship(
        self,
        prompt,
        relationship_type
    ):

        print()

        print(
            f"{prompt} (optional)"
        )

        value = input(
            f"{prompt}: "
        ).strip()

        if not value:

            return []

        entity_id = self.lookup.resolve(
            value
        )

        if entity_id:

            print(
                f"Resolved -> {entity_id}"
            )

            return [
                entity_id
            ]

        print()

        print(
            f"No {relationship_type} found named:"
        )

        print(
            value
        )

        print()

        keep = input(
            "Keep as plain text? (Y/n): "
        ).strip().lower()

        if keep in (
            "",
            "y",
            "yes"
        ):

            return [
                value
            ]

        return []

    # =====================================================
    # Entity Preview
    # =====================================================

    def preview(self, entity):

        print()

        print("----------------------------------------")
        print("Entity Preview")
        print("----------------------------------------")
        print()

        print(
            yaml.safe_dump(
                entity,
                sort_keys=False,
                allow_unicode=True,
                default_flow_style=False,
            ).rstrip()
        )

        print("----------------------------------------")
        print()

        response = input(
            "Save entity? (Y/n): "
        ).strip().lower()

        if response in (
            "",
            "y",
            "yes"
        ):

            return True

        print()

        print(
            "Entity creation cancelled."
        )

        return False

    # =====================================================
    # Platform Builder
    # =====================================================

    def build_platform(self):

        print()

        print("RVDB Platform Builder")
        print("---------------------")

        name = input(
            "Platform name: "
        ).strip()

        manufacturer = self.resolve_relationship(
            "Manufacturer",
            "manufacturer"
        )

        release_year = input(
            "\nRelease year (optional): "
        ).strip()

        generation = input(
            "Generation (optional): "
        ).strip()

        entity_id = IDGenerator.generate(
            "platform",
            name
        )

        print()

        print("Generated ID:")

        print(entity_id)

        entity = self.factory.create_entity(
            "platform",
            entity_id,
            name
        )

        entity["aliases"] = []

        entity["manufacturer"] = manufacturer

        if release_year.isdigit():

            entity["release_year"] = int(
                release_year
            )

        else:

            entity["release_year"] = None

        if generation.isdigit():

            entity["generation"] = int(
                generation
            )

        else:

            entity["generation"] = None

        entity["relationships"][
            "supports_core"
        ] = []

        if not self.preview(
            entity
        ):

            return None

        return entity
