from abc import ABC, abstractmethod
from characters import Personaje

class AbstractCharacterFactory(ABC):

    @abstractmethod
    def addcha(self, **kwargs)-> Personaje:
        pass