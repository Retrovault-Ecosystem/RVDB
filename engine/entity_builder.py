from engine.factory import EntityFactory
from engine.id_generator import IDGenerator


class EntityBuilder:

    def __init__(self):

        self.factory = EntityFactory()

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
    # Platform Builder
    # =====================================================

    def build_platform(self):

        print()
        print("RVDB Platform Builder")
        print("---------------------")

        name = input(
            "Platform name: "
        ).strip()

        manufacturer = input(
            "Manufacturer (optional): "
        ).strip()

        release_year = input(
            "Release year (optional): "
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

        # Remove template placeholder alias
        entity["aliases"] = []

        # Manufacturer
        if manufacturer:
            entity["manufacturer"] = [
                manufacturer
            ]
        else:
            entity["manufacturer"] = []

        # Release year
        if release_year.isdigit():
            entity["release_year"] = int(
                release_year
            )
        else:
            entity["release_year"] = None

        # Generation
        if generation.isdigit():
            entity["generation"] = int(
                generation
            )
        else:
            entity["generation"] = None

        # Remove placeholder relationship
        entity["relationships"][
            "supports_core"
        ] = []

        return entity
