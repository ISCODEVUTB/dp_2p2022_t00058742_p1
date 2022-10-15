from characters import Personaje
from Ificha import IFicha
from enums import TypeAlienigena

class Aliens(Personaje):
    __RaceAlien: TypeAlienigena

    def __init__(self, caracterizacion=[], enemigo=None, liga=None, **kwargs):
        super().__init__(caracterizacion, enemigo, liga, **kwargs)
        self.__RaceAlien = kwargs['RaceAlien']

    def getRazaAlien(self):
        return self.__RaceAlien.name
    
    