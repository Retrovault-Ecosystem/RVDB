import re


class EntityResolver:

    def __init__(self, graph):
        self.graph = graph


    def normalize(self, text):

        if not text:
            return ""

        text = text.lower()

        # remove punctuation
        text = re.sub(
            r"[^a-z0-9\s]",
            "",
            text
        )

        # collapse spaces
        text = " ".join(
            text.split()
        )

        return text



    def resolve(self, text):

        query = self.normalize(text)


        # -------------------------
        # Exact ID
        # -------------------------

        for entity_id, entity in self.graph.nodes.items():

            if self.normalize(entity_id) == query:
                return entity



        # -------------------------
        # Name
        # -------------------------

        for entity in self.graph.nodes.values():

            name = self.normalize(
                entity.get("name", "")
            )

            if name == query:
                return entity



        # -------------------------
        # Aliases
        # -------------------------

        for entity in self.graph.nodes.values():

            for alias in entity.get(
                "aliases",
                []
            ):

                if self.normalize(alias) == query:
                    return entity



        # -------------------------
        # Partial match
        # -------------------------

        for entity in self.graph.nodes.values():

            name = self.normalize(
                entity.get("name", "")
            )

            if query in name:
                return entity


        return None
