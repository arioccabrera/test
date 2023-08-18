
print("'Dame una clase television con volumen y canal y con los metods que permita subir/bajar el volumen y cambiar de canal y verás que guapo' Descartes")

class television:
    def __init__(self, volumen=0, canal=0):
        self.volumen = volumen
        self.canal = canal
    def consultar_volumen(self):
        return print(f"Volumen= {self.volumen}")
    def consultar_canal(self):
        return print(f"Canal= {self.canal}")
    def aumentar_volumen(self):
        if self.volumen < 100:
            self.volumen += 1
        else:
            print("Mi niño te vas a quedar sordo, ya tienes la chisma esta ar masimo")
    def disminuir_volumen(self):
        if self.volumen > 0:
            self.volumen -= 1
        else:
            print("Que lo tienes muteado bobo")
    def aumentar_canal(self):
        self.canal +=1
    def disminuir_canal(self):
        self.canal -=1


tele = television()

while True:
    print()
    print("elije: ")
    print("1. Subir volumen")
    print("2. Bajar volumen")
    print()
    print("3. Subir un canal")
    print("4. Bajar un canal")
    print()
    print("5. Ver volumen")
    print("6. Ver canal")
    print()
    print("0. Apagar el televisor... y enciende el transistor noo tal")
    opcion= input("Que vas hacer mijo? ")

    if opcion == '0':
        print("Apagando el televisor... adiOFF")
        break
    if opcion == '1':
        print("Opcion 1: Subir volumen")
        tele.aumentar_volumen()
    if opcion == '2':
        print("Opcion 2: Bajar volumen")
        tele.disminuir_volumen()
    if opcion == '3':
        print("Opcion 3: Aumentar un canal")
        tele.aumentar_canal()
    if opcion == '4':
        print("Opcion 4: Bajar un canal")
        tele.disminuir_canal()
    if opcion == '5':
        print("Opcion 5: Ver volumen")
        tele.consultar_volumen()
    if opcion == '6':
        print("Opcion 6: Ver canal")
        tele.consultar_canal()



"""
rint("'Dame una clase ascensor que permita guardar piso en que está, total de pisos, capacidad y personas dentro' Descartes")
print("La clase tiene los métodos: iniciar, entar, salir, subir, bajar")
class ascensor:
    def __init__(self,pisoActual=0, totalPisos=0, capacidad=0, personas=0):
        self.pisoActual= pisoActual
        self.totalPisos = totalPisos
        self.capacidad= capacidad
        self.personas = personas
    def iniciar(self):
        self.totalPisos = int(input("Cuantos pisos tiene el edificiooo? "))
        self.capacidad = int(input("Cuanta capacidad tiene el acensooor? "))
    def entrar(self):
        if self.personas < self.capacidad:
            self.personas += 1
        else:
            return print("Mira es que estamos ya a tope perdona, vuelve luego vale?")
    def salir(self):
        if self.personas > 0:
            self.personas -= 1
        else:
            return print("Mira es que ya no hay nadie, quien mas va a salil, casper oiste?")
        pass
    def subir(self):
        if self.pisoActual < self.totalPisos:
            self.pisoActual += 1
        else:
            return print("Mira es que ya no hay mas pa subir, esto es un acensol no un licotero")
    def bajar(self):
        if self.pisoActual > 0:
            self.pisoActual -= 1
        else:
            return print("Mira es que ya no hay mas pa bajal, esto no es una mina")
while True:
    opcion= input("bienvenido, para iniciar el acensor, pulse 1: ")
    if opcion == '1':
        ascensor1= ascensor()
        ascensor1.iniciar()
        break
print("ascensor iniciado, buen viaje :)")
while True:
    print()
    print("elije: ")
    print("2. Entrar")
    print("3. salir")
    print("4. Subir")
    print("5. Bajar")
    print()
    print("0. Parada emergencia")
    opcion= input("Que vas hacer mijo? ")
    print(ascensor1.pisoActual)
    print(ascensor1.totalPisos)
    print(ascensor1.capacidad)
    print(ascensor1.personas)
    if opcion == '0':
        print("paradinha emergencia, hasta luego lucas!")
        break
    if opcion == '2':
        print("Opcion 2: Meterse pa dentro")
        ascensor1.entrar()
    if opcion == '3':
        print("Opcion 3: Salirse pa fuera")
        ascensor1.salir()
    if opcion == '4':
        print("Opcion 4: Subir pa rriba")
        ascensor1.subir()
    if opcion == '5':
        print("Opcion 4: Bajar pa bajo")
        ascensor1.bajar()



print("'Dame una clase agenda que permita guardar 10 persona y sus metodos para guardar/mostrar/borrar datos y te lo hago' Descartes")
opcion=1
class agenda:
    lista_agenda=[]
    def __init__(self, nombre, edad, altura):
        self.__nombre= nombre
        self.__edad= edad
        self.__altura= altura
        if len(agenda.lista_agenda)<10:
            agenda.lista_agenda.append(self)
        else:
            print("Lo siento pero aqui ya no cabe mas nada mijo")
    def eliminar_contacto(self):
        if len(agenda.lista_agenda)>0:
            print(f"en caso conflito, se borrara  solo el primer contacto llamado {self}")
            for obj in range (len(agenda.lista_agenda)):
                if agenda.lista_agenda[obj].__nombre == self:
                    agenda.lista_agenda.pop(obj)
                    break
        else:
            print("Es que no hay nada para borrar")
    def mostrar(self):
        if len(agenda.lista_agenda) > 0:
            for obj in range (len(agenda.lista_agenda)):
                print(agenda.lista_agenda[obj].__nombre, agenda.lista_agenda[obj].__edad, agenda.lista_agenda[obj].__altura)
        else:
            print("eeeh, hola? no tienes a nadie en la agenda, payaso")
    def mostrar_posicion(self):
        if len(agenda.lista_agenda) > 0:
            for obj in range (len(agenda.lista_agenda)):
                if agenda.lista_agenda[obj].__nombre == self:
                    print(f"Tienes a {self} en la posicion {obj}")
        else:
            print("eeeh, hola? no tienes a nadie en la agenda en esa posicion, payaso")
    def mostrar_persona(self):
        if len(agenda.lista_agenda) > self:
            for obj in range (len(agenda.lista_agenda)):
                if obj == self:
                    print(f"La perosna que buscas en la posición {self} es:")
                    print(f"Nombre: {agenda.lista_agenda[obj].__nombre}")
                    print(f"Edad: {agenda.lista_agenda[obj].__edad}")
                    print(f"Altura: {agenda.lista_agenda[obj].__altura}")
        else:
            print("eeeh, hola? no tienes a nadie en la agenda, payaso")
while opcion !=0:
    print()
    print("1. Guardar contacto")
    print("2. Eliminar contacto (Por nombre)")
    print("3. Buscar contacto (Por nombre e informa cual es su posicion en la agenda)")
    print("4. Mostrar agenda (te muestra todos los contactos de la agenda)")
    print("5. Mostrar un contacto (te muestra los datos de la persona en la posicion 'i' de la agenda)")
    print()
    print("0. Para salir del pogama")
    print()
    opcion= int(input("chicos si les puedo ayudar en alguna cositaaa..."))
    print(f"aah vale querias un {opcion} ? te lo miro")
    print()
    print()
    if opcion== 1:
        print("Opción 1. Guardar contacto")
        nombre = input("Nombrecito: ")
        edad = input("Edacita: ")
        altura = input("Alturacita: ")
        agenda(nombre, edad, altura)
    elif opcion== 2:
        print("Opción 2. Eliminar contacto (Por nombre)")
        nombre = input("Nombrecito: ")
        agenda.eliminar_contacto(nombre)
    elif opcion== 3:
        print("Opción 3. Buscar contacto (Por nombre e informa cual es su posicion en la agenda)")
        nombre = input("Nombrecito: ")
        agenda.mostrar_posicion(nombre)
    elif opcion == 4:
        print("Opción 4. Mostrar agenda (te muestra todos los contactos de la agenda)")
        agenda.mostrar(None)
    elif opcion == 5:
        print("Opción 5. Mostrar un contacto (te muestra los datos de la persona en la posicion 'i' de la agenda)")
        posicion= int(input("Dime la posicion del contacto que quieres que te muestre(de 0 a... lo que haiga): "))
        agenda.mostrar_persona(posicion)
    elif opcion == 0:
        print("bueeno muchas gracias")
    else:
        print("No me queda nada de lo que quieres...perona")





print("'Dame una clase persona con atributos privados: nombre, edad, altura y los metodos para mostras datos y te muestro las personas' Descartes")

class Persona:
    def __init__(self, nombre='', edad='', altura=''):
        self.__nombre = nombre
        self.__edad = edad
        self.__altura = altura

    def mostrar_datos(self):
        return f'Nombre: {self.__nombre} \nEdad: {self.__edad} \nAltura(cm): {self.__altura}'

    def guardar_datos(self):
        self.__nombre= input("Nombre del sujeto: ")
        self.__edad = input("Edad del sujeto: ")
        self.__altura = input("Altura del sujeto en cm: ")

person= Persona()

person.guardar_datos()
print()
person.mostrar_datos()
print(person.mostrar_datos())









class Cuenta:
    contador=400

    def __init__(self, titular, saldo, limite):
        self.__numero= Cuenta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Cuenta.contador += 1

    def extracto(self):
        print(f'El saldo es de {self.__saldo} €, de la persona: {self.__titular}, con un limite de {self.__limite}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir (self, valor, destino):
        #1 - saco el dineor de la cuenta origen
        self.__saldo -= valor

        #2 - meto el valor en la cuenta de destino
        destino.__saldo += valor

cuenta1=Cuenta('Arioc', 5000, 500)
cuenta2=Cuenta('Pepillo', 5000, 500)

print(cuenta1.__dict__)
print(cuenta2.__dict__)

cuenta2.transferir(1000, cuenta1)
print(cuenta1.__dict__)
print(cuenta2.__dict__)




print(cuenta1)
cuenta1.extracto()
print(cuenta1.__dict__)
cuenta1.extracto()

print(cuenta1._Cuenta__numero)
print(cuenta1._Cuenta__titular)
print(cuenta1._Cuenta__saldo)
print(cuenta1._Cuenta__limite)


cuenta1._Cuenta__titular= 'pepillo'
print(cuenta1.__dict__)
print(cuenta2.__dict__)

cuenta1.depositar(100)
print(cuenta1.__dict__)
cuenta1.sacar(1000)
print(cuenta1.__dict__)

print(cuenta1.__numero)
print(cuenta1.__titular)
print(cuenta1.__saldo)
print(cuenta1.__limite)




cuenta1.__numero = 5
cuenta1.__titular = 'pepe'
cuenta1.__saldo = 9999999
cuenta1.__limite = 9999





class Lampara:

    def __init__(self, color, voltage, luminosidad):   #esto es el metodo contructor, aqui se declaran los atributos, es privado, solo estan dentro de la clase
        self.__voltage = voltage
        self.__color = color
        self.__luminosidad= luminosidad
        self.__encendida = False

    def verifica_lampara(self):
        return self.__encendida

    def on_off_lampara(self):
        if self.__encendida:
            self.__encendida = False
        else:
            self.__encendida = True


class Cliente:
    def __init__(self, nombre, nif):
        self.__nombre = nombre
        self.__nif = nif

    def saludo(self):
        print(f' el cliente {self.__nombre} te manda saludos')

class CuentaBancaria:

    contador=4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = CuentaBancaria.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente= cliente
        CuentaBancaria.contador = self.__numero

    def muestra_cliente(self):
        print(f' El cliente es {self.__cliente._Cliente__nombre}')


class Usuario:

    def __init__(self, nombre, apellido, correo, clave):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo
        self.__clave = clave


#Instancias / Objetos
lampara1= Lampara('calida', 120, 1000)

clie1= Cliente('Arioc', '12345678T')
cuenta1= CuentaBancaria(10000, 2000, clie1)

cuenta1._CuentaBancaria__cliente.saludo()


cuenta1.muestra_cliente()

user1=Usuario('Arioc', 'Cabrera', 'arioc@gm.com', '123456')

print(user1)


print(f' La lampara esta encendida? {lampara1.verifica_lampara()}')
lampara1.on_off_lampara()
print(f' La lampara esta encendida? {lampara1.verifica_lampara()}')
lampara1.on_off_lampara()
print(f' La lampara esta encendida? {lampara1.verifica_lampara()}')

from passlib.hash import pbkdf2_sha256 as cryp  #importe esa biblioteca para encriptar informacion y lo llamo 'cryp' par ano tener que usar todo ese nombre grande
class Usuario:

    contador = 0

    @classmethod
    def contar_usuarios(cls):
        print(f'Hay {cls.contador} usuario/s guardadito/s')

    @staticmethod
    def test():
        return 'AAAA'

    def __init__(self, nombre, apellido,  correo, clave):
        self.id= Usuario.contador + 1
        self.nombre = nombre
        self.apellido= apellido
        self.correo= correo
        self.__clave= cryp.hash(clave, rounds=200000, salt_size=16)
        Usuario.contador= self.id
        print(f'Usuario creado: {self.__crea_usuario()}')

        #round indica el numero de veces que 'baraja' la clave, cuanot mayor mejor
        #salt_size

    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'

    def verifica_clave(self, clave):
        if cryp.verify(clave, self.__clave):
            return True
        return False

    def __crea_usuario(self):
        return self.correo.split('@')[0]

user2= Usuario('arioc', 'silvera', 'arioc@arioc.com', '123456')
user1= Usuario('pepe', 'dias', 'blabla@blabla.com', '789123')

Usuario.contar_usuarios()   #correcto, usamos el metodo y el nombre de la clase

user1.contar_usuarios()     #incorrecto, usmaos la instancia/objeto y le nombre de la clase
                            #es posible pero incorrecto


print(Usuario.contador)
print(Usuario.test())

print(user1.contador)
print(user1.test())


from passlib.hash import pbkdf2_sha256 as cryp  #importe esa biblioteca para encriptar informacion y lo llamo 'cryp' par ano tener que usar todo ese nombre grande

class Usuario:

    def __init__(self, nombre, apellido,  correo, clave):
        self.nombre = nombre
        self.apellido= apellido
        self.correo= correo
        self.__clave= cryp.hash(clave, rounds=200000, salt_size=16)

        #round indica el numero de veces que 'baraja' la clave, cuanot mayor mejor
        #salt_size

    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'

    def verifica_clave(self, clave):
        if cryp.verify(clave, self.__clave):
            return True
        return False


nombre= input('nombre: ')
apellido= input('apellido: ')
correo= input('correo: ')
clave=input('clave: ')
confirma_clave= input('repite la clave: ')

if clave == confirma_clave:
    user= Usuario(nombre, apellido,  correo, clave)
    print("Usuario creado!! :)")
else:
    print("Las claves son diferentes")
    exit(1)

clave=input('Mete tu clave pa iniciar sesion: ')

if user.verifica_clave(clave):
    print("la clave es veridica")
else:
    print("clave incorrecta")

print(f"clave encriptada:{user._Usuario__clave}")  #Recuerda que hacer esto no es correcto, es solo pal ejemplo




user2= Usuario('arioc', 'silvera', 'arioc@arioc.com', '123456')
user1= Usuario('pepe', 'dias', 'blabla@blabla.com', '789123')

print(user2.nombre_completo())
print(Usuario.nombre_completo(user1))

print(f'Clave user2: {user2._Usuario__clave}')
print(f'Clave user1: {user1._Usuario__clave}')

class lampara:

    def __init__(self,voltage, color):   #esto es el metodo contructor, aqui se declaran los atributos, es privado, solo estan dentro de la clase
        self.voltage = voltage
        self.color = color
        self.encendida = False


class CuentaBancaria:

    contador=4999

    def __init__(self, numero, limite, saldo):
        self.numero = CuentaBancaria.contador + 1
        self.limite = limite
        self.saldo = saldo
        CuentaBancaria.contador = self.numero

class Producto:

    contador=0

    def __init__(self, nombre, descripcion, valor):
        self.id = Producto.contador + 1
        self.nombre = nombre
        self.descripcion = descripcion
        self.valor = valor
        Producto.contador = self.id


class Usuario:

    def __init__(self, correo, clave):
        self.correo= correo
        self.__clave= clave

    def muestra_clave(self):
        print(self.__clave)


user1= Usuario('arioc@arioc.com', '123456')
user1= Usuario('blabla@blabla.com', '789123')

print(user1.correo)
#print(user.clave)
print(user1._Usuario__clave)

user1.muestra_clave()

print(dir(user1))
print()
print()

class Producto:

    #atributo de clase
    impuesto= 1 #23% de impuestos
    contador=0

    def __init__(self, nombre, descripcion, valor):
        self.id= Producto.contador +1
        self.nombre = nombre
        self.descripcion = descripcion
        self.valor = (valor * Producto.impuesto)
        Producto.contador= self.id

    def descuento(self, porcentaje):
         #Retorna el valor de un producto con su descuentito
        return (self.valor *(100 - porcentaje))/100


p1= Producto('PS4', 'Consola', 500)
p2= Producto('XBOX', 'Consola', 600)

print(p1.valor)
print(p2.valor)

print(p1.id)
print(p2.id)

#No necesitamos crear una instanca de clase para poder ver un atributo de clase
#Para acceder a un atributo de clase hacmeos esto:
print(Producto.impuesto)

p2.empresa = 'Microsoft'
print(f'Nombre: {p2.nombre}, descripcion: {p2.descripcion}, Valor: {p2.valor}, Empresa: {p2.empresa}')



print(p1.__dict__)
print(p2.__dict__)

del p2.empresa

print(p1.__dict__)
print(p2.__dict__)



print(p1.descuento(20))
print(Producto.descuento(p1, 20))



lamp=lampara()

print(type(lamp))

print(help(int))


class producto:
    pass

ps4= producto()

print(ps4)
print(type(ps4))

"""