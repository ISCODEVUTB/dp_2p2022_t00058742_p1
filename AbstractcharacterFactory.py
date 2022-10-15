from abc import ABC, abstractmethod
from characters import Personaje

class AbstractCharacterFactory(ABC):

    @abstractmethod
    def addcharacter(self, **kwargs)-> Personaje:
        pass