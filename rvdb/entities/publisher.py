from dataclasses import dataclass, field


@dataclass
class Publisher:

    id: str
    name: str

    type: str = "publisher"

    aliases: list[str] = field(
        default_factory=list
    )
