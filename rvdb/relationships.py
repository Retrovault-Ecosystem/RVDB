class RelationshipGraph:


    def __init__(self):

        self.links = []



    def clear(self):

        self.links = []



    def add(
        self,
        source,
        relation,
        target
    ):

        self.links.append(
            {
                "source": source,
                "relation": relation,
                "target": target,
            }
        )



    def find(
        self,
        source=None,
        relation=None
    ):

        results = []


        for link in self.links:

            if source and link["source"] != source:

                continue


            if relation and link["relation"] != relation:

                continue


            results.append(
                link
            )


        return results



graph = RelationshipGraph()
