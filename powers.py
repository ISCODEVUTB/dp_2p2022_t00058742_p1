from characterization  import Caracterizacion
from enums import Elemento


class Poderes(Caracterizacion):
    __damage: float
    __cost: float
    __elemento: Elemento
    __description: str
    def __init__(self, name, damage, cost, description, elemento):
        
        super().__init__(name)
        self.__description = description
        self.__damage = damage
        self.__cost = cost
        self.__elemento = elemento

    
    def getDamage(self):
        return self.__damage
    def getCost(self):
        return self.__cost
    def getDescription(self):
        return self.__description
    def getElemento(self):
        return self.__elemento.name