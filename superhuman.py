from characters import Personaje
from enums import SuperHuman
from characters import Personaje
from enums import SuperHuman

class SuperHumanos(Personaje):
    __ShClases: SuperHuman

    def __init__(self, caracterizacion=[], enemy=None, ligue=None, **kwargs):
        super().__init__(caracterizacion, enemy, ligue, **kwargs)
        self.__ShClases = kwargs['shclass']

    def getShClases(self):
        return self.__ShClases.name