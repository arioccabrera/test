

class Persona:
    def __init__(self, codigo, nombre, edad):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__edad = edad
        print("constuctor calidad")
    @property
    def exibir(self):
        return f"codigo:{self.__codigo }, nombre:{self.__nombre}, edad: {self.__edad}"
    @exibir.setter
    def exibir(self, num):
        if num==1:
            return print(f"codigo:{self.__codigo}, nombre:{self.__nombre}, edad: {self.__edad}")
        return print(f"codigo:{self.__codigo}, nombre:{self.__nombre}")

class TestPersona(Persona):

    def __init__(self, codigo, nombre, edad):
        super().__init__(codigo, nombre, edad)

person1= TestPersona(123, "Juan", 23)
print(person1.exibir)
person1.exibir=1
person1.exibir=0


"""
class Equipamiento:

    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca
    @property
    def modelo(self):
        return self.__modelo

    @marca.setter
    def marca(self, marca):
        self.__marca = marca
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo


class PC(Equipamiento):
    def __init__(self, memoria, procesador, marca, modelo):
        self.__memoria = memoria
        self.__procesador = procesador
        super().__init__(marca, modelo)

    @property
    def memoria(self):
        return self.__memoria
    @property
    def procesador(self):
        return self.__procesador

    @memoria.setter
    def memoria(self, memoria):
        self.__memoria = memoria
    @procesador.setter
    def procesador(self, procesador):
        self.__procesador = procesador

    @property
    def modelo(self):
        return self._Equipamiento__modelo
    @modelo.setter
    def modelo(self, modelo):
        self._Equipamiento__modelo = modelo + ' turbo'

computador= PC('16GB', 'i25', 'telefunken', 'A50')
print(computador.memoria)
print(computador.procesador)
print(computador.marca)
print(computador.modelo)
print()
computador.memoria='32GB'
computador.procesador='i30'
computador.marca='Sony'
computador.modelo= 'epic'
print(computador.memoria)
print(computador.procesador)
print(computador.marca)
print(computador.modelo)



print("'Crea una clase Electrodomestico con atributo encendido y el metodo imprimir para mostras todo eso' Descartes")
class Electrodomestico:
    def __init__(self, encendido= False):
        self.__encendido = encendido
    @property
    def imprimir(self):
        if self.__encendido:
            return "El aparato esta encendido"
        return "El aparato esta apagao"
    @imprimir.setter
    def imprimir(self, senal):
        if senal:
            self.__encendido= True
        else:
            self.__encendido = False
electro1= Electrodomestico(True)
print(electro1.imprimir)
electro1.imprimir=1
print(electro1.imprimir)




print("'Crea una clase Moto con atributos marca, modelo, color y marcha y el metod imprimir para mostras todo eso' Descartes")
class Moto:
    def __init__(self, marca, modelo, color, marcha, arrancada):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__marcha = marcha
        self.__arrancada = arrancada
    @property
    def imprimir(self):
        if self.__arrancada:
            return f"Marca= {self.__marca}\nModelo= {self.__modelo}\nColor= {self.__color}\nMarcha= {self.__marcha}\n y está arrancada hehehe :)"
        else:
            return f"Marca= {self.__marca}\nModelo= {self.__modelo}\nColor= {self.__color}\nMarcha= {self.__marcha}\n y la tego parada para pa no gastar hehehe :)"
    @property
    def subir_marcha(self):
        return self.__marcha
    @subir_marcha.setter
    def subir_marcha(self, marcha):
        self.__marcha += 1
    @property
    def bajar_marcha(self):
        return self.__marcha
    @bajar_marcha.setter
    def bajar_marcha(self, marcha):
        if (self.__marcha >0):
            self.__marcha -=1
        else:
            return print("La moto esta en neutro")
    @property
    def arrancar(self):
        return self.__arrancada
    @arrancar.setter
    def arrancar(self, arranca):
        if self.__arrancada:
            self.__arrancada = False
        else:
            self.__arrancada = True
moto1= Moto('honda','700', 'negra', 2, False)
print(moto1.imprimir)
moto1.subir_marcha=1
print(moto1.imprimir)
moto1.bajar_marcha=1
print(moto1.imprimir)
moto1.arrancar= 1
print(moto1.imprimir)
moto1.arrancar= 1
print(moto1.imprimir)



from  math import pi
print("'Crea una clase circulo con atributos radio, area y perimetro y los metodos calcularArea, calcularPerimetro e imprimir para mostras todo eso' Descartes")
class Circulo:
    def __init__(self, radio):
        self.__radio = radio
        self.__area = 0
        self.__perimetro = 0
    def calcularArea(self):
        self.__area = pi * pow(self.__radio, 2)
    def calcularPerimetro(self):
        self.__perimetro = 2 * pi * self.__radio
    def get_imprimir(self):
        return f"Un circulo de radio:{self.__radio} tiene la siguiente area y perimetro:\n Area= {self.__area}\n Perimetro= {self.__perimetro}"
cuadrado1= Circulo(2)
cuadrado1.calcularArea()
cuadrado1.calcularPerimetro()
print(cuadrado1.get_imprimir())




print("'Crea una clase Rectangulo con atributos largo, ancho, area y perimetro y los metodos calcularArea, calcularPerimetro e imprimir para mostras todo eso' Descartes")
class Cuadrado:
    def __init__(self, largo, ancho):
        self.__largo = largo
        self.__ancho = ancho
        self.__area = 0
        self.__perimetro = 0
    def calcularArea(self):
        self.__area = self.__largo * self.__ancho
    def calcularPerimetro(self):
        self.__perimetro = (self.__largo * 2) + (self.__ancho * 2)
    def get_imprimir(self):
        return f"Un rectangulo  de largo:{self.__largo} y ancho:{self.__ancho} tiene la siguiente area y perimetro:\n Area= {self.__area}\n Perimetro= {self.__perimetro}"
cuadrado1= Cuadrado(6, 2)
cuadrado1.calcularArea()
cuadrado1.calcularPerimetro()
print(cuadrado1.get_imprimir())



print("'Crea una clase Cuadrado con atributos lado, area y perimetro y los metodos calcularArea, calcularPerimetro e imprimir para mostras todo eso' Descartes")
class Cuadrado:
    def __init__(self, lado):
        self.__lado = lado
        self.__area = 0
        self.__perimetro = 0
    def calcularArea(self):
        self.__area = self.__lado * self.__lado
    def calcularPerimetro(self):
        self.__perimetro = self.__lado * 4
    def get_imprimir(self):
        return f"Un cuadrado de lado: {self.__lado} tiene la siguiente area y perimetro:\n Area= {self.__area}\n Perimetro= {self.__perimetro}"
cuadrado1= Cuadrado(2)
cuadrado1.calcularArea()
cuadrado1.calcularPerimetro()
print(cuadrado1.get_imprimir())



print("'Crea una clase persona con atributos nombre, direccion y telefono y crea un metodo imprimir para mostras todo eso' Descartes")
class Persona:
    def __init__(self, nombre, direccion, telefono):
        self.__nombre= nombre
        self.__direccion= direccion
        self.__telefono= telefono
    def get_imprimir(self):
        return f"Nombre: {self.__nombre} \nDireccion: {self.__direccion} \nTelefono: {self.__telefono}"
persona1= Persona("Pepillo", "Calle universo", "928454545")
print(persona1.get_imprimir())





class Libro:

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def __str__(self):
        return self.__titulo

    def __repr__(self):
        return f"titulo: {self.__titulo}"

    def __len__(self):
        return self.__paginas

    def __del__(self):
        print("Un objeto de tipo libro fue eliminado")

    def __add__(self, other):
        return f"{self} - {other}"

    def __mul__(self, other):
        if isinstance(other, int):
            msg= ' '
            for i in range(other):
                msg += ' ' + str(self)
            return msg
        return "Error, multiplicatión no es posible"

libro1= Libro ("1984", "orwell", 200)
libro2= Libro ("la biblia", "dios", "infinitas")

print(libro1)
print(libro2)

print(libro1 + libro2)

print(libro1 * 3)



class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre

#raise NotImplementedError() esto aqui quier decir que una subclase que herede de esta clase
#va a tener que implementar este método, porque si no le va a mostras ese mensaje de error
    def hablar(self):
        raise NotImplementedError("La clase hija necesita implementar este método")

    def comer(self):
        print(f"{self.__nombre} se está jartando a comé")

class Perrillo(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hablar(self):
        print(f"{self._Animal__nombre} hace waw waw")

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hablar(self):
        print(f"{self._Animal__nombre} hace miaaau miaaau")


class Raton(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)


perro1 = Perrillo("Sultan")
gato1 = Gato("Bigotes")
raton1 = Raton("Topolliyo")

perro1.comer()
gato1.comer()
raton1.comer()

perro1.hablar()
gato1.hablar()
raton1.hablar()



class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre

    def saludar(self):
        return f"hola, soy {self.__nombre}"


class Acuatico(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def nadar(self):
        return f"El/La {self._Animal__nombre} está nadando"

    def saludar(self):
        return f"hola, soy un/a {self._Animal__nombre} del mar"


class Terrestre(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def andar(self):
        return f"El/La {self._Animal__nombre} está andando"

    def saludar(self):
        return f"hola, soy un/a {self._Animal__nombre} de la tierra"


class Pinguino(Terrestre,Acuatico):
    def __init__(self,nombre):
        super().__init__(nombre)


criatura= Pinguino('pingüinazo')
print(criatura.andar())
print(criatura.nadar())
print(criatura.saludar())
print(criatura.saludar())


print(f"criatura es instancia de Pinguino? {isinstance(criatura, Pinguino)}")
print(f"criatura es instancia de Acuatico? {isinstance(criatura, Acuatico)}")
print(f"criatura es instancia de Terrestre? {isinstance(criatura, Terrestre)}")
print(f"criatura es instancia de object? {isinstance(criatura, object)}")


print(f"Pinguino es subclase de Acuativo? {issubclass(Pinguino, Acuatico)}")
print(f"Terrestre es subclase de Acuativo? {issubclass(Terrestre, Acuatico)}")
print(f"Acuativo es subclase de Animal? {issubclass(Acuatico, Animal)}")
print(f"Pinguino es subclase de Animal? {issubclass(Pinguino, Animal)}")
print(f"Animal es subclase de Pinguino? {issubclass(Animal, Pinguino)}")

print(Pinguino.__mro__)
print(Pinguino.mro())
print(help(Pinguino))



class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class Multiderivada(Base1,Base2, Base3):
    pass


class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class Multiderivada(Base3):
    pass




class Animal:
    def __init__(self, nombre, especie):
        self.__nombre = nombre
        self.__especie = especie
    def sonido(self, sonido):
        print(f"El {self.__especie}, {self.__nombre}, hace {sonido}")

class Gato(Animal):
    def __init__(self, nombre, especie, raza):
        super().__init__(nombre, especie)
        #Animal.__init__(self, nombre, especie) //se puede poner así también
        self.__raza= raza
        super().sonido('kikirikii')


gato1= Gato('chispita', 'felino', 'siemens')
gato1.sonido('rrrrr')



class Cuenta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Cuenta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite= limite
        Cuenta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite_nuevo):
        self.__limite = limite_nuevo

    @property
    def valor_total(self):
        return self.__saldo + self.__limite


    def extracto(self):
        return f"Saldo: {self.__saldo}, titular: {self.__titular}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


cuenta1= Cuenta('arioc', 5000, 6000)
cuenta2= Cuenta('pepillo', 5000, 56000)

print(cuenta1.extracto())
print(cuenta2.extracto())

suma= cuenta1.saldo + cuenta2.saldo
print(suma)

print(cuenta1.__dict__)
cuenta1.limite= 9999999
print(cuenta1.__dict__)

print(cuenta1.valor_total)
print(cuenta2.valor_total)





class Cuenta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Cuenta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite= limite
        Cuenta.contador += 1

    def extracto(self):
        return f"Saldo: {self.__saldo}, titular: {self.__titular}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return  self.__limite

    def set_titular(self, titular):
        self.__titular = titular

    def set_limite(self, limite):
        self.__limite = limite



cuenta1= Cuenta('arioc', 5000, 6000)
cuenta2= Cuenta('pepillo', 5000, 56000)

print(cuenta1.extracto())
print(cuenta2.extracto())

suma= cuenta1.get_saldo() + cuenta2.get_saldo()
print(suma)

print(cuenta1.__dict__)
cuenta1.set_limite(999999999)
print(cuenta1.__dict__)





class Persona:
    def __init__(self, nombre, apellido, nif):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nif = nif

    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

class Cliente(Persona):
    def __init__(self, nombre, apellido, nif, renta):
        super().__init__(nombre, apellido, nif)
        self.__renta= renta

class Funcionario(Persona):

    def __init__(self,nombre, apellido, nif, matricula):
        super().__init__(nombre, apellido, nif)
        self.__matricula= matricula

    def nombre_completo(self):
        print(super().nombre_completo())
        print(self._Persona__nif)
        return f"Funcionario: {self.__matricula}, nombre: {self._Persona__nombre}"


cliente1= Cliente('arioc', 'silvera', '123456789', 2000)
funcionario1= Funcionario('kevin', 'cabrera', '987654321', 2500)

print(cliente1.nombre_completo())
print(funcionario1.nombre_completo())


class Persona:
    def __init__(self, nombre, apellido, nif):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nif = nif

    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

class Cliente(Persona):
    def __init__(self, nombre, apellido, nif, renta):
        super().__init__(nombre, apellido, nif)
        self.__renta= renta

class Funcionario(Persona):

    def __init__(self,nombre, apellido, nif, matricula):
        super().__init__(nombre, apellido, nif)
        self.__matricula= matricula


cliente1= Cliente('arioc', 'silvera', '123456789', 2000)
funcionario1= Funcionario('kevin', 'cabrera', '987654321', 2500)
print(cliente1.nombre_completo())
print(funcionario1.nombre_completo())


print(cliente1.__dict__)
print(funcionario1.__dict__)





class Cliente:

    def __init__(self, nombre, apellido, nif, renta):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nif = nif
        self.renta= renta

    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

class Funcionario:

    def __init__(self, nombre, apellido, nif, matricula):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nif = nif
        self.__matricula= matricula

    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

cliente1= Cliente('arioc', 'silvera', '123456789', 2000)
funcionario1= Funcionario('kevin', 'cabrera', '987654321', 2500)

print(cliente1.nombre_completo())
print(funcionario1.nombre_completo())"""