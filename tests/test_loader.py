from rvdb.loader import RVDBLoader
from rvdb.registry import registry


loader = RVDBLoader()


loader.load_directory(
    "platforms",
    "data/platforms"
)


loader.load_directory(
    "developers",
    "data/developers"
)


loader.load_directory(
    "publishers",
    "data/publishers"
)


loader.load_directory(
    "games",
    "data/games"
)


print(
    "Platforms:",
    registry.count("platforms")
)


print(
    "Developers:",
    registry.count("developers")
)


print(
    "Publishers:",
    registry.count("publishers")
)


print(
    "Games:",
    registry.count("games")
)


game = registry.get(
    "games",
    "galaga_arcade"
)


print()
print(game)
