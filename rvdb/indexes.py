class RVDBIndexes:


    def __init__(self):

        self.clear()



    def clear(self):

        self.title = {}

        self.platform = {}

        self.developer = {}

        self.publisher = {}

        self.genre = {}

        self.region = {}



    def add_to_index(
        self,
        index,
        key,
        value
    ):

        if key not in index:

            index[key] = []


        index[key].append(
            value
        )



    def add_game(
        self,
        game
    ):

        game_id = game.id


        if game.title:

            self.title[
                game.title.lower()
            ] = game_id



        if game.platform:

            self.add_to_index(
                self.platform,
                game.platform,
                game_id
            )



        if game.developer:

            self.add_to_index(
                self.developer,
                game.developer,
                game_id
            )



        if game.publisher:

            self.add_to_index(
                self.publisher,
                game.publisher,
                game_id
            )



        for genre in game.genres:

            self.add_to_index(
                self.genre,
                genre,
                game_id
            )



        for region in game.regions:

            self.add_to_index(
                self.region,
                region,
                game_id
            )



    def build(
        self,
        games
    ):

        self.clear()


        for game in games:

            self.add_game(
                game
            )



indexes = RVDBIndexes()
