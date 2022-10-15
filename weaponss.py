from characterization import Caracterizacion


class Armas(Caracterizacion):
    
    __damage: float
    __municion: int
    __cargador: int
    __capacidadCargador: int
    def __init__(self, name,damage, municion, cargador, capacidadCargador):
        super().__init__(name)
        self.__damage = damage
        self.__capacidadCargador = capacidadCargador
        if  cargador <= self.__capacidadCargador:
            self.__cargador = cargador
        else: 
            raise TypeError("El cargador no puede ser mayor que la capacidad maxima")
        self.__municion = municion
    
    
    def recargar(self)->bool:
        if self.__municion == 0: 
            print("no hay municion.")
            return False
        else:
            reloading = self.__capacidadCargador - self.__cargador
            if reloading == 0:
                print("municion llena")
                return False
            else: 
                aux = self.__municion - reloading
                if aux > 0:
                    self.__cargador += reloading
                    self.__municion -= reloading
                    return True
                else: 
                    self.__cargador += self.__municion
                    self.__municion -= self.__municion
                    return True         
    def getDamage(self):
        self.__cargador -= 1
        return self.__damage
    

arma = Armas("Arma", 20, 30, 30, 30)
print(arma.getName())