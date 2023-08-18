
def suma (a,b,c):
    print(a+b+c)

diccionario=dict(a=1,b=2,c=3)

suma(**diccionario)


"""
def nombres(**kwargs):
    return f"{kwargs['nombre']} {kwargs['apellido']}"

nombre={'nombre': 'Arioc', 'apellido': 'Silvera'}

print(nombres(**nombre))




def orden(edad, nombre, *args, soltero=False,**kwargs):
    print(f"{nombre} tiene {edad} años")
    print(args)
    if soltero:
        print("soltero")
    else:
        print("casado")
    print(kwargs)

orden(15,'Hugo')
print()
orden(15,'Hugo',1,2,4.4,5.9)
print()
orden(54,'Luis',1,2,4.4,5.9, soltero=True)
print()
orden(54,'Luis',1,2,4.4,5.9, soltero=True, perro='Lula')



def saludo_especial(**kwargs):
    if 'arioc' in kwargs and kwargs['arioc'] == 'hola':
        return 'Saludos especiales para ti, Arioc!'
    elif 'arioc' in kwargs:
        return f"{kwargs['arioc']} Arioc!"
    return "me quedé en 33 ahora al verte la cara..."

print(saludo_especial())
print(saludo_especial(arioc='hola'))
print(saludo_especial(arioc='tonces'))
print(saludo_especial(arioc='saludito'))




def colores(**kwargs):
    for persona, color in kwargs.items():
        print(f"El color favorito de {persona.title()} es el {color}")


colores(pedro='azul', juan='rojo', mario='verde')


def fuera():
    contador=0

    def dentro():
        nonlocal contador

        contador +=1
        return contador
    return dentro()

print(fuera())
print(fuera())
print(fuera())

total=0
def incremento():
    global total
    total +=1
    return total

print(incremento())
print(incremento())
print(incremento())
print(incremento())


def muestra_info(nombre='arioc', trabajador=False):
    if nombre=='arioc' and trabajador:
        return 'Ay maaaqui!'
    elif nombre=='arioc':
        return 'Perdon, te confundi con el maqui'
    return f'Tonces que {nombre}, como va la cosa?'

print(muestra_info())
print(muestra_info(trabajador=True))
print(muestra_info('pepillo'))
print(muestra_info(nombre='kiwi'))



def cuadrado(base=2, exponente):
    return base**exponente

print(cuadrado(8)) #si yo llamo a la funcion así voy a tener un error



def suma(a, b):
    return a - b


print(suma(a=99,b=3))
print(suma(1,3))




def suma(a, b):
    return a + b

def multiplica(a, b):
    return a * b

def otro(num1, b, msg):
    return (num1+ b) *msg

print(suma(99,1))
print(suma(1,3))

print(multiplica(4,5))
print(multiplica(2,7))
print(otro(3,5,'hola mi gente, '))



def cuadrado(int):
    return int*int

print(cuadrado(8))

from random import random

def tira_moneda():
    if random()>0.5:
        return 'Cara'
    else:
        return 'Cruz'


print(tira_moneda())


def funcion_test():
    return 1,2,3,4

print(type(funcion_test()))
print(funcion_test())

num1, num2, num3, num4 = funcion_test()

print(num4,num3,num2,num1)


def funcion_test():
    variable= True
    if variable:
        return 1
    elif variable is None:
        return 2
    else:
        return 3

print(funcion_test())



def dime_hola():
    print("antes del return")
    return ("hola amigo!")
    print("despues del return")

print(dime_hola())

def cuadrado_de_7():
    return 7*7

print(cuadrado_de_7())


def dime_hola():
    print("hola amigo!")

dime_hola()
print()
for i in range(5):
    print(f"{i}")
    dime_hola()

print()
print("saluda")
saluda= dime_hola
print(type(saluda))
saluda()
"""