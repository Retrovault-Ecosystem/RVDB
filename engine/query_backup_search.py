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

        # 1. Exact ID match
        if text in self.graph.nodes:
            return self.graph.nodes[text]

        # 2. Exact name match
        for entity in self.graph.nodes.values():

            if entity.get("name", "").lower() == text:
                return entity

        # 3. Exact alias match
        for entity in self.graph.nodes.values():

            aliases = entity.get("aliases", [])

            for alias in aliases:

                if alias.lower() == text:
                    return entity

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

            id_lower = entity_id.lower()
            name_lower = entity.get("name", "").lower()
            type_lower = entity.get("type", "").lower()

            aliases = entity.get("aliases", [])
            aliases_lower = [a.lower() for a in aliases]

            entity_type = entity.get("type", "")


            # -----------------------------------------
            # Entity type weighting
            # -----------------------------------------

            if entity_type == "platform":
                score += 5
                reasons.append("platform bonus +5")

            # -----------------------------------------
            # Exact matches
            # -----------------------------------------

            if term == id_lower:
                score += 20
                reasons.append("exact id match +20")

            if term == name_lower:
                score += 20
                reasons.append("exact name match +20")

            # -----------------------------------------
            # Partial matches
            # -----------------------------------------

            if term in id_lower:
                score += 8
                reasons.append("id partial match +8")

            if term in name_lower:
                score += 12
                reasons.append("name partial match +12")

            # -----------------------------------------
            # Alias matching
            # -----------------------------------------

            for alias in aliases_lower:

                if term == alias:
                    score += 25
                    reasons.append(f"exact alias '{alias}' +25")

                elif term in alias:
                    score += 10
                    reasons.append(f"partial alias '{alias}' +10")

            # -----------------------------------------
            # Platform boost
            # -----------------------------------------

            if entity_type == "platform" and term in id_lower:
                score += 15
                reasons.append("platform id match +15")

            # -----------------------------------------
            # Token matching
            # -----------------------------------------

            for token in query_tokens:

                if token in id_lower:
                    score += 2
                    reasons.append(f"id token '{token}' +2")

                if token in name_lower:
                    score += 4
                    reasons.append(f"name token '{token}' +4")

                if token in type_lower:
                    score += 1
                    reasons.append(f"type token '{token}' +1")

            # -----------------------------------------
            # Character overlap
            # -----------------------------------------

            overlap = 0

            for char in term:

                if char in id_lower or char in name_lower:
                    overlap += 0.2

            if overlap:
                score += overlap
                reasons.append(f"character overlap +{overlap:.1f}")

            # -----------------------------------------
            # Save result
            # -----------------------------------------

            if score >= 8:
                results.append({
                    "score": score,
                    "entity": entity,
                    "reasons": reasons
                })

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
