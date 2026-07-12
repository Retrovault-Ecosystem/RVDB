from dataclasses import dataclass


@dataclass
class Core:
    id: str
    name: str
    library_file: str
    supported_platforms: list[str]
