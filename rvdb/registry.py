class Registry:


    def __init__(self):

        self._data = {

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

        if category not in self._data:

            self._data[category] = {}


        self._data[category][entity.id] = entity



    def get(
        self,
        category,
        entity_id
    ):

        return (
            self._data
            .get(category, {})
            .get(entity_id)
        )



    def all(
        self,
        category
    ):

        return list(
            self._data
            .get(category, {})
            .values()
        )



    def count(
        self,
        category
    ):

        return len(
            self._data
            .get(category, {})
        )



    def exists(
        self,
        category,
        entity_id
    ):

        return entity_id in self._data.get(
            category,
            {}
        )



registry = Registry()
