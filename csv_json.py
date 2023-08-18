
import jsonpickle

class Gato:
    def __init__(self, nombre, raza):
        self.__nombre = nombre
        self.__raza = raza
    @property
    def nombre(self):
        return self.__nombre
    @property
    def raza(self):
        return self.__raza


with open('gatos.json', 'r') as archivo:
    contenido = archivo.read()
    ret = jsonpickle.decode(contenido)
    print(ret)
    print(type(ret))
    print(ret.nombre)
    print(ret.raza)

"""
import jsonpickle

class Gato:
    def __init__(self, nombre, raza):
        self.__nombre = nombre
        self.__raza = raza
    @property
    def nombre(self):
        return self.__nombre
    @property
    def raza(self):
        return self.__raza

gato1= Gato('Felix', 'Siemens')

with open('gatos.json', 'w') as archivo:
    ret= jsonpickle.encode(gato1)
    archivo.write(ret)






import jsonpickle


class Gato:
    def __init__(self, nombre, raza):
        self.__nombre = nombre
        self.__raza = raza
    @property
    def nombre(self):
        return self.__nombre
    @property
    def raza(self):
        return self.__raza

gato1= Gato('Felix', 'Siemens')

ret = jsonpickle.encode(gato1)

print(ret)








import json


class Gato:
    def __init__(self, nombre, raza):
        self.__nombre = nombre
        self.__raza = raza
    @property
    def nombre(self):
        return self.__nombre
    @property
    def raza(self):
        return self.__raza

gato1= Gato('Felix', 'Siemens')

print(gato1.__dict__)

ret= json.dumps(gato1.__dict__)

print(ret)

ret = json.dumps(['producto', {'PS4':('2TB', 'Nuevo', '22v', 2340)}])

print(type(ret))
print(ret)



import pickle

class Animal:
     def __init__(self, nombre):
        self.__nombre = nombre

     @property
     def nombre(self):
         return self.__nombre

     def comer(self):
         print(f"{self.__nombre} esta comiendo")

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    def maullar(self):
        print(f"{self._Animal__nombre} Esta maullando")


class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def ladrar(self):
        print(f"{self._Animal__nombre} Esta ladrando")


with open('animalitos.pickle', 'rb') as archivo:
    gato, perro= pickle.load(archivo)
    print(f"El gato se llama {gato.nombre}")
    gato.maullar()
    print(f"Su tipo de dato es: {type(gato)}")

    print(f"El perro se llama {perro.nombre}")
    perro.ladrar()
    print(f"Su tipo de dato es: {type(perro)}")



import pickle

class Animal:
     def __init__(self, nombre):
        self.__nombre = nombre

     def comer(self):
         print(f"{self.__nombre} esta comiendo")

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    def maullar(self):
        print(f"{self._Animal__nombre} Esta maullando")


class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    def ladrar(self):
        print(f"{self._Animal__nombre} Esta ladrando")

gato1= Gato("Bigotes")
perro1= Perro("Tobi")

with open('animalitos.pickle', 'wb') as archivo:
    pickle.dump((gato1, perro1), archivo)



from csv import DictWriter

with open('peliculas2.csv', 'w') as archivo:
    encabezado= ['Titulo', 'Genero', 'Duracion']
    escritor_csv = DictWriter(archivo, fieldnames=encabezado)
    escritor_csv.writeheader()
    pelicula = None
    while pelicula !='salir':
        pelicula= input("Nombre de la pelicula: ")
        if pelicula !='salir':
            genero = input("Género de la pelicula: ")
            duracion = input("Duración de la pelicula: ")
#acuardate aqui que los diccionarios funcionan con key:value
#Y al principio dle código indiqué cual es la key
#que equivale al nombre de cada columna ['Titulo', 'Género', 'Duración']
#es importante que la key este escrita exactamente igual que en el encabezado
#o sea, mayusculas, minuculas, acentos,... tooodo igualito
            escritor_csv.writerow({'Titulo':pelicula, 'Genero':genero, 'Duracion':duracion})



from csv import writer

with open('peliculas.csv', 'w') as archivo:
    escritor_csv = writer(archivo)
    pelicula = None
    escritor_csv.writerow(['Titulo', 'Género', 'Duración'])
    while pelicula != 'salir':
        pelicula= input("Nombre de la pelicula: ")
        if pelicula != 'salir':
            genero= input("Genero de la pelicula: ")
            duracion = input("Duración de la pelicula: ")
            escritor_csv.writerow([pelicula, genero, duracion])



from csv import DictReader

with open("lutadores.csv") as archivo:
    lector_csv= DictReader(archivo, delimiter=';')
    print(type(lector_csv))
    for i in lector_csv:
        print(f"Nombre: {i['Nome']} *** Pais de nacimiento: {i['Pais']} *** Altura: {i['Altura (em cm)']}")


with open("lutadores.csv") as archivo:
    lector_csv= reader(archivo)
    print(type(lector_csv))
    next(lector_csv)
    for i in lector_csv:
        print(f"Nombre: {i[0]} *** Pais de nacimiento: {i[1]} *** Altura: {i[2]}")


with open("lutadores.csv") as archivo:
    lector_csv= reader(archivo)
    for i in lector_csv:
        print(i)


with open("lutadores.csv") as archivo:
    datos= archivo.read()
    datos = datos.split(',')[2:]
    print(datos)


with open("lutadores.csv") as archivo:
    datos= archivo.read()
    print(type(datos))
    print(datos)"""