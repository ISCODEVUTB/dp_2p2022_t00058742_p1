from AbstractcharacterFactory import AbstractCharacterFactory
from superhuman import SuperHumanos

class SuperHumansFactory(AbstractCharacterFactory):

    def addcharacter(self, **kwargs):
        return SuperHumanos(**kwargs)