from dataclasses import dataclass, field


@dataclass
class Game:
    id: str
    title: str

    platform: str
    core: str

    year: int | None = None

    developer: str | None = None
    publisher: str | None = None

    genres: list[str] = field(default_factory=list)

    regions: list[str] = field(default_factory=list)

    rom_path: str | None = None
