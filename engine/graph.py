class RVGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.reverse_edges = {}   # NEW

    def add_entity(self, entity):
        entity_id = entity["id"]

        self.nodes[entity_id] = entity
        self.edges[entity_id] = entity.get("relationships", {})

        # Build reverse index
        relationships = entity.get("relationships", {})

        for rel_type, targets in relationships.items():

            if not isinstance(targets, list):
                continue

            for target in targets:

                if target not in self.reverse_edges:
                    self.reverse_edges[target] = {}

                if rel_type not in self.reverse_edges[target]:
                    self.reverse_edges[target][rel_type] = []

                self.reverse_edges[target][rel_type].append(entity_id)


def build_graph(entities):
    graph = RVGraph()

    for entity in entities:
        if isinstance(entity, dict) and "id" in entity:
            graph.add_entity(entity)

    return graph
