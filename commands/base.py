from abc import ABC, abstractmethod


class Command(ABC):
    """
    Base class for all RVDB commands.
    """

    name = ""
    aliases = []
    help = ""
    arguments = []

    @abstractmethod
    def run(self, args):
        pass
