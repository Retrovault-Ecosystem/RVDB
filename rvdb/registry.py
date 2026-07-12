class Registry:


    def __init__(self):

        self.data = {

            "games": {},
            "platforms": {},
            "cores": {},
            "developers": {},
            "publishers": {},
            "genres": {},
            "regions": {},

        }



    def register(
        self,
        category,
        entity
    ):

        if category not in self.data:

            self.data[category] = {}


        self.data[category][entity.id] = entity



    def get(
        self,
        category,
        entity_id
    ):

        return (
            self.data
            .get(category, {})
            .get(entity_id)
        )



    def all(
        self,
        category
    ):

        return list(
            self.data
            .get(category, {})
            .values()
        )



    def count(
        self,
        category
    ):

        return len(
            self.data
            .get(category, {})
        )



    def exists(
        self,
        category,
        entity_id
    ):

        return entity_id in self.data.get(
            category,
            {}
        )



registry = Registry()
