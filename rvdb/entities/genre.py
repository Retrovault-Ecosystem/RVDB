from dataclasses import dataclass, field


@dataclass
class Genre:

    id: str
    name: str

    aliases: list[str] = field(
        default_factory=list
    )
