from dataclasses import dataclass


@dataclass
class Platform:

    id: str
    name: str

    manufacturer: str | None = None

    release_year: int | None = None

    category: str | None = None
