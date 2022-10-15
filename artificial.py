from characterization import Caracterizacion
from characters import Personaje
from enums import Laboratorio, TypeArticial

class Artificiales(Personaje):
    __RangeArtificial: TypeArticial
    __Laboratory: Laboratorio
    def __init__(self, caracterizacion=[], enemy=None, ligue=None,**kwargs):
        super().__init__( caracterizacion, enemy, ligue, **kwargs)
        "Inicializador de Persojane, nombre: str, vida: float, estamina: float, fuerza: float, velocidad: float, armadura: float, caracterizacion: list of objects, enemigo: Personaje[defaul->none] liga: str"
        self.__RangeArtificial = kwargs['RangeArtificial']
        self.__Laboratory = kwargs['Laboratory']

    def getRangoArtificial(self):
        return self.__RangeArtificial
    def getLaboratorio(self):
        return self.__Laboratory
    