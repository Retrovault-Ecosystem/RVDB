class RVEngine:

    def __init__(self, graph):
        self.graph = graph


    def get_entity(self, entity_id):
        return self.graph.nodes.get(entity_id)


    def get_supported_cores(self, platform_id):

        platform = self.get_entity(platform_id)

        if not platform:
            return []

        return platform.get("relationships", {}).get("supports_core", [])


    def get_platforms_by_core(self, core_id):

        return self.graph.reverse_edges.get(core_id, {}).get("supports_core", [])


    def get_relationships(self, entity_id):

        return {
            "forward": self.graph.edges.get(entity_id, {}),
            "reverse": self.graph.reverse_edges.get(entity_id, {})
        }


    def get_entities_by_relationship(self, target_id, relationship_type):

        results = []

        for entity_id, entity in self.graph.nodes.items():

            relationships = entity.get("relationships", {})

            targets = relationships.get(
                relationship_type,
                []
            )

            if target_id in targets:
                results.append(entity)

        return results

    # =====================================================
    # FUZZY SEARCH WITH EXPLAINABLE SCORING + ALIASES
    # =====================================================

    # =====================================================
    # AUTOMATIC ENTITY RESOLUTION
    # =====================================================

    def resolve_entity(self, text):

        text = text.lower().strip()

        if not text:
            return None

        # 1. Exact ID match
        if text in self.graph.nodes:
            return self.graph.nodes[text]

        # 2. Unique exact name match
        name_matches = []

        for entity in self.graph.nodes.values():

            if entity.get("name", "").lower() == text:

                name_matches.append(
                    entity
                )

        if len(name_matches) == 1:
            return name_matches[0]

        if len(name_matches) > 1:
            return None

        # 3. Unique exact alias match
        alias_matches = []

        for entity in self.graph.nodes.values():

            aliases = entity.get(
                "aliases",
                [],
            )

            for alias in aliases:

                if alias.lower() == text:

                    alias_matches.append(
                        entity
                    )

                    break

        if len(alias_matches) == 1:
            return alias_matches[0]

        if len(alias_matches) > 1:
            return None

        # 4. Fuzzy fallback
        results = self.search(text)

        if results:
            return results[0]["entity"]

        return None


    def search(self, term):

        term = term.lower().strip()

        query_tokens = term.split()

        results = []


        for entity_id, entity in self.graph.nodes.items():

            score = 0
            reasons = []


            entity_id_lower = entity_id.lower()
            name_lower = entity.get("name", "").lower()
            entity_type = entity.get("type", "").lower()

            aliases = [
                a.lower()
                for a in entity.get("aliases", [])
            ]


            # =================================================
            # EXACT ID
            # =================================================

            if term == entity_id_lower:

                score += 100

                reasons.append(
                    "exact id match +100"
                )


            # =================================================
            # EXACT NAME
            # =================================================

            if term == name_lower:

                score += 100

                reasons.append(
                    "exact name match +100"
                )


            # =================================================
            # EXACT ALIAS
            # =================================================

            for alias in aliases:

                if term == alias:

                    score += 90

                    reasons.append(
                        f"exact alias '{alias}' +90"
                    )


            # =================================================
            # FULL QUERY MATCH
            # =================================================

            name_words = name_lower.split()

            if query_tokens:

                matched = all(
                    token in name_words
                    for token in query_tokens
                )

                if matched:

                    score += 50

                    reasons.append(
                        "all query words matched +50"
                    )


            # =================================================
            # NAME TOKENS
            # =================================================

            for token in query_tokens:

                if token in name_lower:

                    score += 20

                    reasons.append(
                        f"name token '{token}' +20"
                    )


                if token in entity_id_lower:

                    score += 10

                    reasons.append(
                        f"id token '{token}' +10"
                    )


                if token in entity_type:

                    score += 5

                    reasons.append(
                        f"type token '{token}' +5"
                    )


            # =================================================
            # ALIASES
            # =================================================

            for alias in aliases:

                for token in query_tokens:

                    if token in alias:

                        score += 15

                        reasons.append(
                            f"alias token '{token}' +15"
                        )


            # =================================================
            # PLATFORM BOOST
            # =================================================

            if entity_type == "platform":

                score += 5

                reasons.append(
                    "platform bonus +5"
                )


            # =================================================
            # SMALL CHARACTER SIMILARITY BONUS
            # =================================================

            overlap = 0

            for char in term:

                if char in entity_id_lower or char in name_lower:

                    overlap += 0.1


            if overlap:

                score += overlap

                reasons.append(
                    f"character overlap +{overlap:.1f}"
                )


            # =================================================
            # STORE RESULT
            # =================================================

            if score > 0:

                results.append(
                    {
                        "score": score,
                        "entity": entity,
                        "reasons": reasons
                    }
                )


        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )


        return results[:10]
    

    def get_related_entities(self, entity_id):

        entity = self.get_entity(entity_id)

        if not entity:
            return {}

        relationships = entity.get("relationships", {})

        results = {}

        for relationship_type, targets in relationships.items():

            results[relationship_type] = []

            for target_id in targets:

                target = self.get_entity(target_id)

                if target:
                    results[relationship_type].append(target)

        return results
