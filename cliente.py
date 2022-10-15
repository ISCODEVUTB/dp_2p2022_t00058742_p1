from AbstractcharacterFactory import AbstractCharacterFactory


class Client():
    __factory: AbstractCharacterFactory
    def __init__(self, factory: AbstractCharacterFactory):
        self.__factory = factory

    def buildProduct(self, factory: AbstractCharacterFactory,**kwargs):
        self.__factory = factory
        return self.__factory.addcharacter(**kwargs)


