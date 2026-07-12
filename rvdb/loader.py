from rvdb.registry import registry


class RVDBLoader:


    def load_entity(
        self,
        category,
        entity
    ):

        registry.register(
            category,
            entity
        )


    def load_entities(
        self,
        category,
        entities
    ):

        for entity in entities:

            self.load_entity(
                category,
                entity
            )
