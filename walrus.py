from typing import Literal
from typing import Union
from typing import Final
from typing import final
from typing import TypedDict
from typing import Protocol


geek= 'Test'

print(f"{geek=}")








"""
class Curso(Protocol):
    titulo: str

def estudiar(valor: Curso) -> None:
    print(f"Estoy estudiando {valor.titulo}")

class Venta:
    titulo= 'ola'

v1= Venta()
#c1= Curso()

#c1.titulo= ' Programar en python'
estudiar(v1)
#estudiar(c1)



class CursoPython(TypedDict):
    version: str
    actualizacion: int


geek= CursoPython(version='2.8', actualizacion=2022)

print(geek)









@final
class Persona:
    pass

class Estudiante(Persona):
    pass

    @final
    def estudiar(self):
        print('Estudiando...')

class Practicas(Estudiante):
    pass

    def estudiar(self):
        print('De Prácticas...')






NOMBRE: Final = 'Arioc'
print(NOMBRE)


NOMBRE='Kevin'
print(NOMBRE)




def suma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1+num2

    if resultado > 50:
        return f"Resutado {resultado} muy elevado"
    else:
        return resultado




def calcula_v2(operar: Literal['+','-'], num1: int, num2: int) -> None:
    if operar == '+':
        print(f"{num1} + {num2} = {num1+num2}")
    elif operar == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    else:
        raise ValueError(f'Operación inválida {operar!r}')


calcula_v2('+',5,4)
calcula_v2('-',5,4)
calcula_v2('*',5,4)




def estado(usuario: str) -> Literal['conectaco', 'desconectado']:
    pass

def calcula_v1(operar: str, num1: int, num2: int) -> None:
    if operar == '+':
        print(f"{num1} + {num2} = {num1+num2}")
    elif operar == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    else:
        raise ValueError(f'Operación inválida {operar!r}')


calcula_v1('+',5,4)
calcula_v1('-',5,4)
calcula_v1('*',5,4)







def saluda_v6(nombre,/, mensaje='Hola', *, mensaje2):
    return f"{mensaje} {nombre} {mensaje2}"

print(saluda_v6('arioc', mensaje='hola', mensaje2='donde estas?'))
print(saluda_v6('Jonh', mensaje2='WTF?'))
print(saluda_v6('Jonh', 'vamos al monte',mensaje2= 'vamos?' ))





def saluda_v5(*, nombre):
    return f"Hola, {nombre}"

print(saluda_v5(nombre='Pepillo'))
print(saluda_v5('Jonh'))






def saluda_v3(nombre, /, mensaje='Tonces?'):
    return f"{mensaje}, {nombre}"

print(saluda_v3('Pepillo'))
print(saluda_v3('Jonh', mensaje='Hello'))
print(saluda_v3('Arioc', 'buenas tardes'))



def saluda_v2(nombre):
    return f"Hola, {nombre}"

print(saluda_v2(('Pepillo')))
print(saluda_v2(nombre ='Juan'))



def saluda_v1(nombre):
    return f"Hola, {nombre}"

print(saluda_v1(('Pepillo')))
print(saluda_v1(nombre ='Juan'))




valor= '67.3'
print(float(valor))

print(help(float))



cesta=[]
while (fruta := input('Dime frutita: '))!= 'jaca':
    cesta.append(fruta)


cesta=[]
fruta= input('Dime frutita: ')
while fruta != 'jaca':
    cesta.append(fruta)
    fruta = input('Dime frituta: ')



nombre =' Arioc silvera'
print(nombre)

print(nombre :=' Arioc silvera')"""