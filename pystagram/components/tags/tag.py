from abc import ABC, abstractmethod


class Tag(ABC):
    """ Abstract class for an Instagram Tag."""
    @abstractmethod
    def dict(self) -> dict:
        pass
