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

        if not query:
            return None

        # -------------------------
        # Exact ID
        # -------------------------

        for entity_id, entity in self.graph.nodes.items():

            if self.normalize(entity_id) == query:
                return entity


        # -------------------------
        # Exact Name
        # -------------------------

        name_matches = []

        for entity in self.graph.nodes.values():

            name = self.normalize(
                entity.get("name", "")
            )

            if name == query:
                name_matches.append(
                    entity
                )

        if len(name_matches) == 1:
            return name_matches[0]

        if len(name_matches) > 1:
            return None


        # -------------------------
        # Exact Alias
        # -------------------------

        alias_matches = []

        for entity in self.graph.nodes.values():

            for alias in entity.get(
                "aliases",
                []
            ):

                if self.normalize(alias) == query:

                    alias_matches.append(
                        entity
                    )

                    break

        if len(alias_matches) == 1:
            return alias_matches[0]

        if len(alias_matches) > 1:
            return None


        # -------------------------
        # Partial match
        # -------------------------

        matches = []

        for index, entity in enumerate(
            self.graph.nodes.values()
        ):

            name = self.normalize(
                entity.get("name", "")
            )

            if query in name:

                matches.append(
                    (
                        self._partial_match_priority(
                            entity
                        ),
                        index,
                        entity,
                    )
                )


        if not matches:
            return None


        matches.sort(
            key=lambda match: (
                match[0],
                match[1],
            )
        )


        return matches[0][2]


    def _partial_match_priority(
        self,
        entity,
    ):

        entity_type = entity.get(
            "type",
            "",
        )

        priorities = {
            "platform": 0,
            "core": 1,
            "game": 2,
            "developer": 3,
            "publisher": 3,
            "manufacturer": 3,
            "genre": 4,
            "compatibility": 100,
        }

        return priorities.get(
            entity_type,
            50,
        )
