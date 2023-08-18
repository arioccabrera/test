
import random as rdn
from random import shuffle

cartas=[1,2,3,4,5,6,7,10,11,12]

print(cartas)
shuffle(cartas)
print(cartas)




"""
nombre= 'arioc'
apel= 'silvera'
breakpoint()
completo= nombre+' '+ apel
curso= ' programacion python'
todo= completo + ' esta estudiando' + curso
print(todo)


def dividir(a,b):
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError) as err:
        return (f"Ese valor esta incorrecto: {err}")


n1=(input("Numero 1: "))
n2=(input("Numero 2: "))

print(dividir(n1,n2))


def dividir(a,b):
    try:
        return a/b
    except ValueError:
        return ("Ese valor esta incorrecto")
    except ZeroDivisionError:
        return ("No se puede dividir por cero muchacho!")

n1=int(input("Numero 1: "))
n2=int(input("Numero 2: "))

print(dividir(n1,n2))



try:
    num=int(input("dime un numero: "))
except ValueError:
    print("Ese valor no sirve")
else:
    print(f"numero: {num}")
finally:
    print("estoy dentro del finally")


def valor(diccionario, valor):
    try:
        return diccionario[valor]
    except KeyError:
        return None


dic={'nombre':'Arioc'}

print(valor(dic,'hola'))



try:
    print('Arioc'[8])
except TypeError as erra:
    print(f"Ese tipo de dato no me cuadra eeh? TypeError: {erra}")
except NameError as errb:
    print(f"Ese tipo de dato no me cuadra eeh? NameError: {errb}")
except:
    print(f"Error diferente")


try:
    test()
except:
    print("Aqui pasan rollos raros")


try:
    test2()
except NameError:
    print("el nombre desa funcion no me suena eeh?")


try:
    len(5)
except TypeError:
    print("Ese tipo de dato no me cuadra eeh?")


try:
    len(5)
except TypeError as err:
    print(f"Ese tipo de dato no me cuadra eeh?, se genero el siguiente error: {err}")


def colores(texto, cor):
    cores={'verde','azul', 'amarillo'}
    if type(texto) is not str:
        raise TypeError('El testo tiene que ser string, socio')
    if type(cor) is not str:
        raise TypeError('El color tiene que ser string, socio')
    if cor not  in cores:
        raise ValueError (f"Su colorcito tiene que esta entre: {cores}")
    print(f"aqui su texto:{texto} y aqui su color{cor}")


colores('mar', 'rojo')"""