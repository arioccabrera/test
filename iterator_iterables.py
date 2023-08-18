


"""
def fozar_tipo(*tipos):
    def decorador(funcion):
        def convertir(*args,**kwargs):
            nuevo_arg=[]
            for(valor, tipo) in zip(args, tipos):
                nuevo_arg.append(tipo(valor))
            return funcion(*nuevo_arg, *kwargs)
        return convertir
    return decorador

@fozar_tipo(str, int)
def repite_msg(msg, veces):
    for vez in range(int(veces)):
        print(msg)

repite_msg('Arioc', '3')

@fozar_tipo(float,float)
def dividir(a,b):
    print(a/b)

dividir('1',8)



from functools import wraps

def ver_log(funcion):
    @wraps(funcion)
    #def logar (*args,**kwargs):
        #soy una funcion (logar) dentro de otra
        
        print(f'Aqui estas llamando a: {funcion.__name__}')  #funcion.__name__ muestra el nombre de la funcion, lo tengo en apuntes mas pa atras
        print(f'la documentacion es: {funcion.__doc__}')     #funcion.__doc__  muestra la documentacion de dentro de la funcion, lo tengo en apuntes mas pa atras
        return funcion(*args,**kwargs)
    return logar
"""
"""
@ver_log
def suma(a,b):
    #Funcion para Sumar dos numeros
    return a+b

print(suma(10,30))


#aqui hay un problema
print(suma.__name__)
print(suma.__doc__)
print(help(suma))


def verifica_primer_argumento(valor):
    def interna(funcion):
        def otra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorrecto el primero agumento tiene que ser = {valor}'
            return funcion(*args, **kwargs)
        return otra
    return interna

@verifica_primer_argumento(10)
def suma_diez(N1,N2):
    return N1+N2

print(suma_diez(10,40))


@verifica_primer_argumento('judias')
def comida_rica(*args):
    print(args)

print(comida_rica('burger', 'pizza','garbanza compuestas'))



def mayuscula(funcion):
    def aumentar (*args, **kwargs):
        return funcion(*args, **kwargs).upper()
    return aumentar

@mayuscula
def saludito(nombre):
    return f'Hola, yo soy {nombre}'

print(saludito('arioc'))


@mayuscula
def pedido(primero, segundo):
    return f'Hola, quiero  un {primero} y dispue {segundo}'

print(pedido(primero='potagito', segundo='arroz'))
print(pedido(segundo='arroz', primero='potagito'))


def mayuscula(funcion):
    def aumentar (nombre):
        return funcion(nombre).upper()
    return aumentar

@mayuscula
def saludito(nombre):
    return f'Hola, yo soy {nombre}'

print(saludito('arioc'))


@mayuscula
def pedido(primero, segundo):
    return f'Hola, quiero  un {primero} y dispue {segundo}'

print(pedido('potagito', 'arroz'))






def educado(funcion):
    def siendo():
        print("Encantado de conocerte!")
        funcion()
        print("Que tengas un wen dia!")
    return siendo

@educado
def saludito():
    print("Me llamo Arioc")

saludito()



def educado(funcion):
    def siendo():
        print("Encantado de conocerte!")
        funcion()
        print("Que tengas un wen dia!")
    return siendo

def saludito():
    print("Bienvenido a este test!")

saludito()

prueba= educado(saludito)

prueba()

from random import choice

def faz_me_rir_novo(pesoa):
    def risas():
        riso= choice(('aaaaaaaaaaaaaaaaaaaaaaaaaajajjajaajjajaja', 'kjakjakjakjakjajkakjakja', 'jejejejejejejejejejejeje'))
        return f'{riso} {pesoa}'
    return risas

riendo=faz_me_rir_novo('chanin')

print(riendo())
print(riendo())
print(riendo())

from random import choice

def faz_me_rir():
    def rir():
        return choice(('aaaaaaaaaaaaaaaaaaaaaaaaaajajjajaajjajaja', 'kjakjakjakjakjajkakjakja', 'jejejejejejejejejejejeje'))
    return rir

risas= faz_me_rir()
print(risas())



from random import choice

def cumprimento(persona):
    def humor():
        return choice(('Tonces? que pasa ', 'aay pichon? que pasa ', 'qué pasó? '))
    return humor() + persona

print(cumprimento('Suso'))
print(cumprimento('Grabiel'))


def sumar(a,b):
    return a+b

def resta(a,b):
    return a-b

def multi(a,b):
    return a*b

def divi(a,b):
    return a/b

def calculadora(n1,n2, funcion):
    return funcion(n1,n2)

print(calculadora(4,3,sumar))
print(calculadora(4,3,resta))
print(calculadora(4,3,multi))
print(calculadora(4,3,divi))


import time

gen_inicio= time.time()
print(sum(num for num in range(10000)))
print(type(num for num in range(10000)))
gen_tempo = time.time() - gen_inicio


list_inicio= time.time()
print(sum([num for num in range(10000)]))
print(type([num for num in range(10000)]))
list_tempo = time.time() - list_inicio

print(f"Tiempo del generator: {gen_tempo}")
print(f"tiempo de la lista: {list_tempo}")



ge2= (num for num in range(1,10))

print(ge2)
print(next(ge2))


def nums():
    for num in range(1,10):
        yield num

ge1= nums()

print(ge1)
print(next(ge1))
print(next(ge1))




def fib_gen(max):
    a , b , contador = 0 , 1 , 0
    while contador<max:
        a, b =b, a+b
        yield a
        contador += 1

for n in fib_gen(1000):
    print(n)


def fib_lista(max):
    nums=[]
    a,b =0,1
    while len(nums) < max:
        nums.append(b)
        a, b =b, a+b
    return nums

for n in fib_lista(1000):
    print(n)


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

gen= list(conta_ate(4))

print(gen)

for i in gen:
    print(i)



print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



class Contador:
    def __init__(self, menor, mayor): # funcion llamada contructor. el self siempre va cuando tienes una funcion dentro
        # de una clase pero no cuenta como si fuese un parametro de entrada, representa al propio objeto
        self.menor = menor
        self.mayor = mayor

    def __iter__ (self):
        return self

    def __next__(self):
        if self.menor < self.mayor:
            numero = self.menor
            self.menor = self.menor +1
            return numero
        raise StopIteration

con = Contador (1,6)

it= iter(con)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


def mi_for (iterable):
    it= iter(iterable)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


mi_for([1,2,3,4,5])


for num in [1,2,3,4,5]:
    print(num)

for letra in "palabra de prueba":
    print(letra)


nombre= 'Geek'
numero=[1,2,3,4,5]

#print(next(nombre))
#print(numero)


iterable1 = iter(nombre)
iterable2 = iter(numero)

print(next(iterable2))
print(next(iterable2))
print(next(iterable2))
print(next(iterable2))
print(next(iterable2))
"""
