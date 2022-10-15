from characters import Personaje
from enums import HumanStatus, Sexo
class Humano(Personaje):
    __HumanStatus: HumanStatus
    __Sex: Sexo

    def __init__(self, caracterizacion=[], enemy=None, ligue=None, **kwargs):
        "Instanciar un humano para agregarlo al juego, puedes agregarle caracteristicas"
        super().__init__(caracterizacion, enemy, ligue, **kwargs)
        self.__HumanStatus = kwargs['humanStatus']
        self.__Sex = kwargs['sex']

    def getHumanStatus(self):
        return self.__HumanStatus.name
    def getSexo(self):
        return self.__Sex.name