from AbstractcharacterFactory import AbstractCharacterFactory
from alienz import Aliens


class AliensFactory(AbstractCharacterFactory):

    def addcharacter(self, **kwargs):
        return Aliens(**kwargs)