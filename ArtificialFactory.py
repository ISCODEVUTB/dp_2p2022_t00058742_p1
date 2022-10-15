from AbstractcharacterFactory import AbstractCharacterFactory
from artificial import Artificiales

class ArtificialsFactory(AbstractCharacterFactory):

    def addcharacter(self, **kwargs):
        return Artificiales(**kwargs)