from engine.loader import Entity


class RVGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.reverse_edges = {}

    def add_entity(self, entity: Entity):
        entity_id = entity.id

        self.nodes[entity_id] = entity

        relationships = entity.get(
            "relationships",
            {}
        )

        self.edges[entity_id] = relationships

        for rel_type, targets in relationships.items():

            if not isinstance(targets, list):
                continue

            for target in targets:

                if target not in self.reverse_edges:
                    self.reverse_edges[target] = {}

                if rel_type not in self.reverse_edges[target]:
                    self.reverse_edges[target][rel_type] = []

                self.reverse_edges[target][rel_type].append(
                    entity_id
                )


def build_graph(entities):

    graph = RVGraph()

    for entity in entities:

        if isinstance(entity, Entity):

            graph.add_entity(entity)

    return graph
