import unittest
from enums import *
import enums
from weakness import Debilidades
from ability import Habilidades
from personality import Personalidad
from powers import Poderes
from weaponss import Armas 
from alienz import Aliens
from artificial import Artificiales
from human import Humano
from superhuman import SuperHumanos

class TestPersonaje(unittest.TestCase):
    print("Entrando a desarrollo de tests final branch assigment 1")
    # PERSONAJES PARA TESTEAR
    Xeno = Aliens("Xeno", 450, 300, 400, 230, 210, 410, Estado.VIVO, TypeAlienigena.DEPREDATORS)
    Androide18 = Artificiales("18", 800, 150, 300, 70, 200, TypeArticial.mac_2, Laboratorio.LAB_X11)
    Captain_America = Humano("Steve Rogers", 100, 100, 50, 120, 100, 100, Estado.VIVO, HumanStatus.SUPER_SOLDADO, Sexo.MAN)
    
    Flash = SuperHumanos("Barry Allen", 500, 500, 500,500,500, 100, Estado.VIVO,SuperHuman.VELOCISTA)


    # Caracterizacion para Testear
    Super_Speed = Poderes("SuperVelocidad", 500, 100, "SuperVelocidad", Elemento.NORMAL)
    
    
    AK47 = Armas("AK47", 150,100,30,30)
    MA04= Armas("MA04", 70,100,30,30)
    
    inteligente = Personalidad("inteligente", "Es inteligente")
    loco = Personalidad("loco", "Es loco")

    lanzar_piedrotas = Habilidades("Lanzar Piedrotas", 500, 20)
    
    
    Kriptonita = Debilidades("Kriptonita", Elemento.TIERRA, -0.4)
    veneno = Debilidades("veneno", Elemento.VENENO, -0.4)
    
    

    # TESTEAR METODO ADD 
    def test_personaje_add(self):
        self.Captain_America.Add(self.inteligente)
        self.assertTrue(self.Captain_America.add_test(self.inteligente))
    
    # TESTEAR METODO ENEMIGO
    def test_personaje_Enemigo(self):
        self.Captain_America.Enemigo(self.Xeno)
        self.assertEqual(self.Captain_America.getEnemigo(), self.Xeno)
        
    # TESTEAR SETEO DE LIGA 
    def test_personaje_liga(self):
        self.Captain_America.Liga("Marvel")
        self.assertEqual(self.Captain_America.getLiga(), "Marvel")
        
        
class TestArmas(unittest.TestCase):
    # TEST PARA ARMAS
    def test_Arma_Nombre(self):
        AK47 = Armas("AK47", 50,100,30,30)
        result1 = AK47.getName()
        self.assertEqual(result1, "AK47")
    
    def test_Arma_Disparo(self):
        AK47 = Armas("AK47", 50,100,30,30)
        result2 = AK47.getDamage()
        self.assertEqual(result2, 50)

    # TEST PARA PODERES
    Super_Speed = Poderes("SuperVelocidad", 500, 100, "SuperVelocidad", enums.Elemento.NORMAL)

    def test_poder_nombre(self):
        self.assertAlmostEqual(self.Super_Speed.getName(), "SuperVelocidad")
    def test_poder_damage(self):
        self.assertEqual(self.Super_Speed.getDamage(), 500)
    def test_poder_elemento(self):
        self.assertEqual(self.Super_Speed.getElemento(), "NORMAL")

    # TEST PARA DEBILIDADES
    debilidad_veneno = Debilidades("Venenosis", enums.Elemento.VENENO, -0.5)

    def test_debilidad_efecto(self):
        self.assertEqual(self.debilidad_veneno.getEfecto(), -0.5)
    def test_debilidad_elemento(self):
        self.assertEqual(self.debilidad_veneno.getElemento(), "VENENO")
        
    # TEST PARA HABILIDADES
    lanzar_personaje = Habilidades("Lanzamiento", 500, 50)

    def test_habilidad_cost(self):
        self.assertEqual(self.lanzar_personaje.getCost(), 50)
    def test_habilidad_damage(self):
        self.assertEqual(self.lanzar_personaje.getDamage(), 500)

    # TEST PARA PERSONALIDADES 
    inteligente = Personalidad("inteligente", "Es inteligente")
    
    def test_personalidad_name(self):
        self.assertEqual(self.inteligente.getName(), "inteligente")
    def test_personalidad_descrip(self):
        self.assertEqual(self.inteligente.getDescription(), "Es inteligente")

if __name__ == "__main__":
    unittest.main()