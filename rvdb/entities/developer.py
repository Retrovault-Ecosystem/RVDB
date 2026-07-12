from dataclasses import dataclass, field


@dataclass
class Developer:

    id: str
    name: str

    type: str = "developer"

    aliases: list[str] = field(
        default_factory=list
    )
