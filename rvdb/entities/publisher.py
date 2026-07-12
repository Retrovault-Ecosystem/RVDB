from dataclasses import dataclass


@dataclass
class Publisher:
    id: str
    name: str
    country: str | None = None
