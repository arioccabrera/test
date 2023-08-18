
import unittest

class ModuloTest(unittest.TestCase):

    def setUp(self):
        #configuracion del setUp()
        pass

    def test_primero(self):
        #setUp va a correr antes que el test
        #tearDown() va a correr despues que el test
        pass

    def test_segundo(self):
        #setUp va a correr antes que el test
        #tearDown() va a correr despues que el test
        pass

    def tearDown(self):
        # configuracion del teardown()
        pass








def comer (comida, saludable):
    if saludable:
        final= 'Quiero estar en forma'
    else:
        final = 'Hoy me apetece comer porqueria'
    return f"Estoy comiendo {comida} porque {final}"

def dormir(horas):
    if horas > 4:
        return 'Hay que dormir menos, gandul!'
    else:
        return 'Hay que dormir mas'
    pass

"""
def dime_hola():
    
    #>>> dime_hola()
    #'hola'
    
    return "hola"






def suma(a,b):
    
    #>>> suma(1,2)
    #3
    #
    #return a+b

def duplicar (valores):
    
    # duplica los valores en una lista
     #>>> duplicar([1,2,3,4])
     #[2, 4, 6, 8]

     #>>> duplicar([])
     #[]

     #>>> duplicar(['a','b','c'])
     #['aa', 'bb', 'cc']

     #>>> duplicar([True, None])
     #Traceback (most recent call last):
     #   ...
     #TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    
    #return [2 * elemento for elemento in valores]












def comer_mcdonals(comida):
    assert comida in ['perrito', 'papita frita', 'salchipapa', 'hamburguesa'], 'La comida que tu quieres no esta en MC donais'
    return f"Me estoy mandando un {comida}"

comida= input("Que querias, mi niño? ")
print(comer_mcdonals(comida))





def suma_numeros_positivos (a,b):
    assert a>0 and b>0, 'Mira perdona, es que los dos número tienen que ser positivos'
    return a + b

calculo = suma_numeros_positivos(-2,4)
print(calculo)




class Gato:

    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    def maullar (self):
        print(f"{self.__nombre} Esta maullando")


gato1= Gato("Bigotes")
gato1.maullar()
print(gato1.nombre)"""