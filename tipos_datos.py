
lista=[1,2,3,4,5,6,7,8,9]

print(lista[1::4])







"""
import math

def circunferencia(radio: float) -> float:
    #type: (float) -> float
    return 2 * math.pi * radio

print(circunferencia(8))










class Persona:

    def __init__(self, nombre: str, edad: int, peso: float) -> None:
        self.__nombre: str = nombre
        self.__edad: int = edad
        self.__peso: float = peso

    def andar(self) -> str:
        return f"{self.__nombre} Está caminando"

persona1= Persona(nombre='Arioc', edad=33, peso=34)
print(persona1.__dict__)

print(persona1.__init__.__annotations__)

print(persona1.andar.__annotations__)

import math

def circunferencia(radio: float) -> float:
    return 2 * math.pi * radio


#print(circunferencia.__annotations__)

nombre: str = 'Arioc'
peso: float = 64
activo: bool = True


print(nombre)
print(peso)
print(activo)
print(__annotations__)











def encabezado(texto: str, alineamiento: bool = True) ->str:
    if alineamiento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')

print(encabezado('Arioc Silvera'))
print(encabezado('Arioc Silvera', alineamiento='blablabla'))



def saludar (nombre: str) -> str:
    return f'Hola, {nombre}'

print(saludar('Arioc'))




class Cisne:
    def __len__(self):
        return 42

livro = Cisne()

print(len(livro))

nombre= 'Arioc Silvera'
lista= [12, 34, 55, 49]
diccionar= {'carlos':12, 'vanessa':34, 'juan': 49}

print(len(nombre))
print(len(lista))
print(len(diccionar))



if True:
    resultado =  1 + 'Geek'

else:
    resultado = 1 + 41

print(resultado)




edad = 23

print(type(edad))

edad = 'veintitres'

print(type(edad))
"""
