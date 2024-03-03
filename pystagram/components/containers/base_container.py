from abc import ABC


class BaseContainer(ABC):
    """ Abstract class for an Instagram Container."""
    @property
    def fields(self):
        """ Returns the fields of the container as a dictionary."""
        return self.__dict__
