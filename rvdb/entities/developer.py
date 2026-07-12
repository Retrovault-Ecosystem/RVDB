from dataclasses import dataclass


@dataclass
class Developer:
    id: str
    name: str
    country: str | None = None
