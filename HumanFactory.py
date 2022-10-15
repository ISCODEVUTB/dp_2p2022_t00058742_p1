from AbstractcharacterFactory import AbstractCharacterFactory
from human import Humano


class HumanFactory(AbstractCharacterFactory):

    def addcharacter(self, **kwargs):
        return Humano(**kwargs)
        