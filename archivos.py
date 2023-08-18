import os
import tempfile
print("'Dame un archivo con codigo_vendedor, nombre_vendedor, valor_venta y mes y te muestro un menu para modificar ese archivo' Descartes")
opcion=''
set_codigo={0,0}
orden_codigo=[]
set_mes={0,0}
orden_mes=[]
print("[A] Ante de empezar, dime el nombre del archivo que vas a crear o abrir, arfavor")
print("Ha elegio usté '[A] Crear/abrir archivo' ")
nombre = input("Cual es el archivo que vas a crear/abrir?: ")
with open(nombre, 'a') as archivo:
    print("listo")
print()
while True:
    print()
    print("[B] Registar datos de vendedor")
    print("[C] Eliminar datos de vendedor")
    print("[D] Modificar valor de venta")
    print("[E] Mostrar informacion del archivo")
    print("[F] Eliminar archivo de datos")
    print()
    print("[X] Salir del programa")
    print()
    opcion=input("Mete una letra pa yo hacer algo ahí: ")
    with open(nombre) as archivo:
        if len(archivo.readlines()) > 0:
            archivo.seek(0)
            orden_codigo.clear()
            set_codigo.clear()
            orden_mes.clear()
            set_mes.clear()
            for i in archivo:
                set_codigo.add(int(i.split()[0]))
                set_mes.add(int(i.split()[3]))
            orden_codigo=list(set_codigo)
            orden_mes= list(set_mes)
            orden_codigo.sort()
            orden_mes.sort()
            print(orden_codigo)
            print(orden_mes)
            with tempfile.TemporaryFile() as temporal:
                for i in orden_codigo:
                    for k in orden_mes:
                        archivo.seek(0)
                        for j in archivo:
                            if int(i) == int(j.split()[0]) and int(k) == int(j.split()[3]):
                                dato = bytes(j, 'utf-8')
                                temporal.write(dato)
                temporal.seek(0)
                with open(nombre, 'w') as f:
                    pass
                with open(nombre, 'a') as archivo2:
                    for i in temporal:
                        j = i.decode()
                        archivo2.write(j)
    if opcion == 'B' or opcion == 'b':
        print()
        print("Ha elegio usté '[B] Registar datos de vendedor' ")
        codigo_vendedor = input("Codigo del vendedor: ")
        nombre_vendedor = input("Nombre del vendedor: ")
        valor_venta = input("Valor de la venta: ")
        mes = input("Mes de la venta: ")
        with open(nombre) as archivo:
            if len(archivo.readlines()) > 0:
                archivo.seek(0)
                existe= False
                print(f"antes del for: {existe}")
                for i in archivo:
                    if int(i.split()[0])== int(codigo_vendedor) and int(i.split()[3])== int(mes):
                        existe= True
        if not existe:
            with open(nombre, "a") as archivo:
                archivo.write(codigo_vendedor + ' ' + nombre_vendedor + ' ' + valor_venta + ' ' + mes + '\n')
            print("+++ Datos del vendedor registrados +++")
        else:
            print("mira perdona, los datos de ese codigo de vendedor y ese mes ya estan guardados eh, no te confundas...")
        print()
    elif opcion == 'C' or opcion == 'c':
        print()
        print("Ha elegio usté '[C] Eliminar datos de vendedor' ")
        codigo_vendedor = input("Codigo del vendedor que quiere eliminar: ")
        with open(nombre) as archivo:
            with tempfile.TemporaryFile() as temporal:
                tam= len(archivo.readlines())
                archivo.seek(0)
                for i in range(tam):
                    linea= archivo.readline().split()
                    if linea[0] != codigo_vendedor:
                        dato= bytes(linea[0] +' '+ linea[1] +' '+ linea[2] +' '+ linea[3] +'\n', 'utf-8')
                        temporal.write(dato)
                temporal.seek(0)
                with open(nombre, 'w') as f:
                    pass
                with open(nombre, 'a') as archivo2:
                    for i in temporal:
                        j = i.decode()
                        archivo2.write(j)
        print("xX Datos del vendedor eliminados Xx")
        print()
    elif opcion == 'D' or opcion == 'd':
        print()
        print("Ha elegio usté '[D] Modificar valor de venta' ")
        codigo_vendedor = input("Codigo del vendedor para modificar la venta: ")
        valor_venta = input("Nuevo valor de la venta: ")
        with open(nombre) as archivo:
            with tempfile.TemporaryFile() as temporal:
                tam= len(archivo.readlines())
                archivo.seek(0)
                for i in range(tam):
                    linea= archivo.readline().split()
                    if linea[0] == codigo_vendedor:
                        dato= bytes(linea[0] +' '+ linea[1] +' '+ valor_venta +' '+ linea[3] +'\n', 'utf-8')
                        temporal.write(dato)
                    else:
                        dato = bytes(linea[0] + ' ' + linea[1] + ' ' + linea[2] + ' ' + linea[3] + '\n', 'utf-8')
                        temporal.write(dato)
                temporal.seek(0)
                with open(nombre, 'w') as f:
                    pass
                with open(nombre, 'a') as archivo2:
                    for i in temporal:
                        j = i.decode()
                        archivo2.write(j)
        print("+++ valor de venta modificado +++")
        print()
    elif opcion == 'E' or opcion == 'e':
        print()
        print("Ha elegio usté '[E] Mostrar informacion del archivo' ")
        with open(nombre) as archivo:
            print(archivo.read())
        print()
    elif opcion == 'F' or opcion == 'f':
        print("Ha elegio usté '[F] Eliminar archivo de datos' ")
        print(f"Va usté a borrá el archivo: {nombre}")
        confirma=input("Para confirmar que quiere eliminar el archivo escriba 'quiero': ")
        if confirma== 'quiero':
            print("xX Archivo eliminado con exito Xx")
            os.remove(nombre)
        else:
            print("oO El archivo no ha sido eliminado Oo")
    elif opcion == 'X' or opcion == 'x':
        print("...Programa finalizado...")
        break
    else:
        print("...Opcion no reconocida, me parece que te estás equivocando...")





"""
import os
import tempfile
print("'Dame un archivo con codigo_vendedor, nombre_vendedor, valor_venta y mes y te muestro un menu para modificar ese archivo' Descartes")
opcion=''
set_codigo={0,0}
orden_codigo=[]
set_mes={0,0}
orden_mes=[]
print("[A] Ante de empezar, dime el nombre del archivo que vas a crear o abrir, arfavor")
print("Ha elegio usté '[A] Crear/abrir archivo' ")
nombre = input("Cual es el archivo que vas a crear/abrir?: ")
with open(nombre, 'a') as archivo:
    print("listo")
print()
while True:
    print()
    print("[B] Registar datos de vendedor")
    print("[C] Eliminar datos de vendedor")
    print("[D] Modificar valor de venta")
    print("[E] Mostrar informacion del archivo")
    print("[F] Eliminar archivo de datos")
    print()
    print("[X] Salir del programa")
    print()
    opcion=input("Mete una letra pa yo hacer algo ahí: ")
    with open(nombre) as archivo:
        if len(archivo.readlines()) > 0:
            archivo.seek(0)
            orden_codigo.clear()
            set_codigo.clear()
            orden_mes.clear()
            set_mes.clear()
            for i in archivo:
                set_codigo.add(int(i.split()[0]))
                set_mes.add(int(i.split()[3]))
            orden_codigo=list(set_codigo)
            orden_mes= list(set_mes)
            orden_codigo.sort()
            orden_mes.sort()
            print(orden_codigo)
            print(orden_mes)
            with tempfile.TemporaryFile() as temporal:
                for i in orden_codigo:
                    for k in orden_mes:
                        archivo.seek(0)
                        for j in archivo:
                            if int(i) == int(j.split()[0]) and int(k) == int(j.split()[3]):
                                dato = bytes(j, 'utf-8')
                                temporal.write(dato)
                temporal.seek(0)
                with open(nombre, 'w') as f:
                    pass
                with open(nombre, 'a') as archivo2:
                    for i in temporal:
                        j = i.decode()
                        archivo2.write(j)
    if opcion == 'B' or opcion == 'b':
        print()
        print("Ha elegio usté '[B] Registar datos de vendedor' ")
        codigo_vendedor = input("Codigo del vendedor: ")
        nombre_vendedor = input("Nombre del vendedor: ")
        valor_venta = input("Valor de la venta: ")
        mes = input("Mes de la venta: ")
        with open(nombre) as archivo:
            if len(archivo.readlines()) > 0:
                archivo.seek(0)
                existe= False
                print(f"antes del for: {existe}")
                for i in archivo:
                    if int(i.split()[0])== int(codigo_vendedor) and int(i.split()[3])== int(mes):
                        existe= True
        if not existe:
            with open(nombre, "a") as archivo:
                archivo.write(codigo_vendedor + ' ' + nombre_vendedor + ' ' + valor_venta + ' ' + mes + '\n')
            print("+++ Datos del vendedor registrados +++")
        else:
            print("mira perdona, los datos de ese codigo de vendedor y ese mes ya estan guardados eh, no te confundas...")
        print()
    elif opcion == 'C' or opcion == 'c':
        print()
        print("Ha elegio usté '[C] Eliminar datos de vendedor' ")
        codigo_vendedor = input("Codigo del vendedor que quiere eliminar: ")
        with open(nombre) as archivo:
            with tempfile.TemporaryFile() as temporal:
                tam= len(archivo.readlines())
                archivo.seek(0)
                for i in range(tam):
                    linea= archivo.readline().split()
                    if linea[0] != codigo_vendedor:
                        dato= bytes(linea[0] +' '+ linea[1] +' '+ linea[2] +' '+ linea[3] +'\n', 'utf-8')
                        temporal.write(dato)
                temporal.seek(0)
                with open(nombre, 'w') as f:
                    pass
                with open(nombre, 'a') as archivo2:
                    for i in temporal:
                        j = i.decode()
                        archivo2.write(j)
        print("xX Datos del vendedor eliminados Xx")
        print()
    elif opcion == 'D' or opcion == 'd':
        print()
        print("Ha elegio usté '[D] Modificar valor de venta' ")
        codigo_vendedor = input("Codigo del vendedor para modificar la venta: ")
        valor_venta = input("Nuevo valor de la venta: ")
        with open(nombre) as archivo:
            with tempfile.TemporaryFile() as temporal:
                tam= len(archivo.readlines())
                archivo.seek(0)
                for i in range(tam):
                    linea= archivo.readline().split()
                    if linea[0] == codigo_vendedor:
                        dato= bytes(linea[0] +' '+ linea[1] +' '+ valor_venta +' '+ linea[3] +'\n', 'utf-8')
                        temporal.write(dato)
                    else:
                        dato = bytes(linea[0] + ' ' + linea[1] + ' ' + linea[2] + ' ' + linea[3] + '\n', 'utf-8')
                        temporal.write(dato)
                temporal.seek(0)
                with open(nombre, 'w') as f:
                    pass
                with open(nombre, 'a') as archivo2:
                    for i in temporal:
                        j = i.decode()
                        archivo2.write(j)
        print("+++ valor de venta modificado +++")
        print()
    elif opcion == 'E' or opcion == 'e':
        print()
        print("Ha elegio usté '[E] Mostrar informacion del archivo' ")
        with open(nombre) as archivo:
            print(archivo.read())
        print()
    elif opcion == 'F' or opcion == 'f':
        print("Ha elegio usté '[F] Eliminar archivo de datos' ")
        print(f"Va usté a borrá el archivo: {nombre}")
        confirma=input("Para confirmar que quiere eliminar el archivo escriba 'quiero': ")
        if confirma== 'quiero':
            print("xX Archivo eliminado con exito Xx")
            os.remove(nombre)
        else:
            print("oO El archivo no ha sido eliminado Oo")
    elif opcion == 'X' or opcion == 'x':
        print("...Programa finalizado...")
        break
    else:
        print("...Opcion no reconocida, me parece que te estás equivocando...")




print("'Dame un archivo de entrada y uno de salida y te guardo el de entrada pero virado al contrario en el de salida' Descartes")
doc=[]
with open("agenda.bin") as archivo:
    doc=archivo.readlines()
    print(doc)
for i in doc:
    print(i, end=' ')
doc.reverse()
print(doc)
with open("arq6.bin", 'a') as archivo2:
    for i in doc:
        archivo2.write(i[::-1])



print("'Dame una matricula, nombre, año nacimiento de un alumno y la cantidad de alumnos y te lo guardo todo en un archivo ' Descartes")
matricula=''
nombre=''
ano=''
total=0
total=int(input("Cuantos alumnos vas a crear? "))
with open("agenda.bin", 'a') as archivo:
    for i in range(total):
        matricula = ''
        nombre = ''
        ano = ''
        matricula=input("Matricula: ")
        nombre=input("Nombre: ")
        ano=input("Año de nacimiento: ")
        print()
        archivo.write( matricula+ ' ' + nombre + ' ' + ano +"\n" )



from datetime import date
import tempfile
print("'Dame un archivo binario para guardar contactos,telefono y cumpleaños(DDMM) y te creo un programa de control para inserir/quitar contactos, buscar por nombre, ver todos, mostrar contactos que comienzan por una letra y mostrar quien cumple años en el mes en curso' Descartes")
nombre=''
telefono=''
cumple=''
j=''
contacto=[]
existe=False
inicial=''
with open("agenda.bin") as archivo:
    while True:
        archivo.seek(0)
        total = len(archivo.readlines())
        print()
        print("Hooola soy una agenda ortomatica, dime cosas: ")
        print("(a) Nuevo contacto ")
        print("(b) Eliminar contacto ")
        print("(c) Buscar contacto por nombre")
        print("(d) Mostrar todos los contactos")
        print("(e) Mostrar contactos con nombre que empiece por la letra 'X' ")
        print("(f) Mostras quienes cumplen años este mes")
        print("(*) Salir pal carajo ")
        print()
        opcion = input("Introduzca una opcion (a-f o *): ")
        print()
        if opcion=='*':
            break
        elif opcion == 'a' or opcion=='A':
            print()
            print("(a) Nuevo contacto ")
            nombre=input("Nombre del contacto: ")
            telefono=input("Telefono: ")
            cumple=input("Dia del cumple (formato: DDMM): ")
            with open("agenda.bin",'a') as archivo2:
                archivo2.write(nombre +' '+telefono+' '+cumple + '\n')
        elif (opcion == 'b' or opcion=='B') and total!=0:
            archivo.seek(0)
            print("(b) Eliminar contacto ")
            nombre = input("Nombre del contacto que quieres eliminar: ")
            with tempfile.TemporaryFile() as temporal:
                for i in range(total):
                    contacto = archivo.readline().split()
                    if nombre == contacto[0]:
                        True
                    else:
                        dato = bytes(contacto[0] + ' ' + contacto[1] + ' ' + contacto[2] + ' \n', 'utf-8')
                        temporal.write(dato)
                temporal.seek(0)
                archivo.seek(0)
                with open("agenda.bin", 'w') as f:
                    '''esto lo hago para borrar todo el contenido del archivo'''
                    pass
                for i in temporal:
                    j = i.decode()
                    with open("agenda.bin", "a") as archivo2:
                        archivo2.write(j)
        elif opcion == 'c' or opcion=='C':
            print()
            print("(c) Buscar contacto por nombre")
            nombre = input("Nombre del contacto que buscas: ")
            print()
            archivo.seek(0)
            existe=False
            for i in range(total):
                contacto=archivo.readline().split()
                if contacto[0]== nombre:
                    print(f"Nombre: {contacto[0]}, Telefono: {contacto[1]}, Cumple: {contacto[2]}")
                    existe=True
            if not existe:
                print("Ay dios mira perdona, es que no hay nadie que se llame asi, tu me diste bien el nombre?")
        elif opcion == 'd' or opcion=='D':
            print()
            print("(d) Mostrar todos los contactos")
            print()
            archivo.seek(0)
            for i in range(total):
                contacto=archivo.readline()
                print(contacto)
        elif opcion == 'e' or opcion=='E':
            print()
            print("(e) Mostrar contactos con nombre que empiece por la letra 'X' ")
            inicial = input("buscar nombres por la siguiente inicial: ")
            print()
            archivo.seek(0)
            existe=False
            for i in range(total):
                contacto=archivo.readline().split()
                if contacto[0][0]== inicial:
                    print(f"Nombre: {contacto[0]}, Telefono: {contacto[1]}, Cumple: {contacto[2]}")
                    existe=True
            if not existe:
                print("Ay dios mira perdona, es que no hay nadie que empiece por esa inicial, tu me diste bien el nombre?")
        elif opcion == 'f' or opcion=='F':
            print()
            print("(f) Mostrar quienes cumplen años este mes")
            print()
            archivo.seek(0)
            existe=False
            for i in range(total):
                contacto=archivo.readline().split()
                if int(contacto[2][2:4])== date.today().month:
                    print(f"Nombre: {contacto[0]}, Telefono: {contacto[1]}, Cumple: {contacto[2]}")
                    existe=True
            if not existe:
                print("Ay dios mira, es que no hay nadie que cumpla este mes, te lo ahorras")



import tempfile
print("'Dame un archivo binario de mercancias con codigo de producto, descripcion y cantidad y te creo un programa de control para poner/quitar productos y mostrar productos disponibles y nos disponibles' Descartes")
opcion=0
codigo=0
cantidad=0
producto=[]
vacio=''
pro=''
j=''
with open("arq6.bin") as archivo:
    while True:
        archivo.seek(0)
        total = len(archivo.readlines())
        print("Hooola mira, que querias?")
        print("(1) aumentar producto ")
        print("(2) retirar producto ")
        print("(3) Stock total ")
        print("(4) Stock de no disponibles ")
        print("(0) Salir pal carajo ")
        print()
        opcion= int(input("Introduzca una opcion (0-4): "))
        print()
        if opcion == 0:
            break
        elif opcion == 1:
            print("*** (1) aumentar producto ***")
            archivo.seek(0)
            codigo=int(input("cual es el codigo del producto? "))
            cantidad=int(input("Cuanto producto quieres ingresar? "))
            with tempfile.TemporaryFile() as temporal:
                for i in range(total):
                    producto=archivo.readline().split()
                    if codigo== int(producto[0]):
                        producto[2]= int(producto[2]) + cantidad
                        pro=bytes(producto[0] + ' ' + producto[1] + ' ' + str(producto[2]) + ' \n', 'utf-8')
                        temporal.write(pro)
                    else:
                        pro = bytes(producto[0] + ' ' + producto[1] + ' ' + str(producto[2]) + ' \n', 'utf-8')
                        temporal.write(pro)
                temporal.seek(0)
                archivo.seek(0)
                with open("arq6.bin", 'w') as f:
                    '''esto lo hago para borrar todo el contenido del archivo'''
                    pass
                for i in temporal:
                    j = i.decode()
                    with open("arq6.bin", "a") as archivo2:
                        archivo2.write(j)
        elif opcion == 2:
            print("*** (2) retirar producto ***")
            archivo.seek(0)
            codigo=int(input("cual es el codigo del producto? "))
            cantidad=int(input("Cuanto producto quieres retirar? "))
            with tempfile.TemporaryFile() as temporal:
                for i in range(total):
                    producto=archivo.readline().split()
                    if codigo== int(producto[0]):
                        if int(producto[2]) - cantidad <0:
                            print(f"Lo lamento, sacaste mas de lo que hay, pa ese producto solo te vas a poder llevar: {producto[2]} ud")
                            producto[2]= 0
                        else:
                            producto[2] = int(producto[2]) - cantidad
                        pro=bytes(producto[0] + ' ' + producto[1] + ' ' + str(producto[2]) + ' \n', 'utf-8')
                        temporal.write(pro)
                    else:
                        pro = bytes(producto[0] + ' ' + producto[1] + ' ' + str(producto[2]) + ' \n', 'utf-8')
                        temporal.write(pro)
                temporal.seek(0)
                archivo.seek(0)
                with open("arq6.bin", 'w') as f:
                    '''esto lo hago para borrar todo el contenido del archivo'''
                    pass
                for i in temporal:
                    j = i.decode()
                    with open("arq6.bin", "a") as archivo2:
                        archivo2.write(j)
        elif opcion == 3:
            print("*** (3) Stock total ***")
            archivo.seek(0)
            for i in range(total):
                print(archivo.readline())
        elif opcion == 4:
            print("*** (4) Stock de no disponibles ***")
            print("tienes que ir a comprar:")
            archivo.seek(0)
            for i in range(total):
                vacio=archivo.readline()
                if int(vacio.split()[2]) ==0:
                    print(vacio)



print("'Dame el nombre de un archivo de entrada (nombre alumno max 40char, 3 enteros para las notas) y el de salida, y en el de salida te guardo los nombres con las notas en orden creciente' Descartes")
entrada= input("Mira perdona, el archivo de entrada...? ")
salida= input("ah gracias y el de salida...? ")
with open(entrada) as archivo:
    lista1=archivo.readlines()
    archivo.seek(0)
    for i in range(len(lista1)):
        lista2= archivo.readline().split()
        print(f"i:{i}")
        print(f"lista2{lista2}")
        if int(lista2[1])>= int(lista2[2]):
            print("Entro 1-2")
            N=lista2[2]
            print(f"N: {N}")
            lista2[2]= lista2[1]
            print(f"lista2[2]: {lista2[2]}")
            lista2[1]=N
            print(f"lista2[1]: {lista2[1]}")
        if int(lista2[2])>= int(lista2[3]):
            print("Entro 2-3")
            M = lista2[3]
            print(f"M:{M}")
            lista2[3] = lista2[2]
            print(f"lista2[3]: {lista2[3]}")
            lista2[2] = M
            print(f"lista2[3]: {lista2[2]}")
        if int(lista2[1])>= int(lista2[2]):
            print("Entro 1-2")
            N=lista2[2]
            print(f"N: {N}")
            lista2[2]= lista2[1]
            print(f"lista2[2]: {lista2[2]}")
            lista2[1]=N
            print(f"lista2[1]: {lista2[1]}")
        print(f"orden: {lista2}")
        with open(salida, 'a') as archivo2:
            archivo2.write(lista2[0] + ' ' + lista2[1] + ' ' + lista2[2] + ' ' + lista2[3] + '\n')
        print()



print("'Dame el numero de alumnos de una asignatura, nombre(40 char max) y nota final y te los guardo en un archivo binario. luego te digo mayor nota y de quien es' Descartes")
nombre=''
nota=0.0
with open('arq5.txt') as archivo:
    lista1=archivo.readlines()
    print(lista1)
    print(len(lista1))
    for i in range(len(lista1)):
        with open('arq6.bin', 'a') as archivo2:
            archivo2.write(lista1[i])
with open('arq6.bin') as archivo3:
    lista2=archivo3.readlines()
    print(lista2)
    for i in range(len(lista2)):
        if float(lista2[i].split()[1])>nota:
            nota=float(lista2[i].split()[1])
            nombre=lista2[i].split()[0]
print(f"{nombre} sacó un {nota}, es el/la/le mas empoyon/a/e, pegenle")



print("'Dame dos lista(V1=nombres y V2= notas final) y te creo un archivo que te crea una linea para cada nombre con su respectiva nota' Descartes")
contador=0
nombre=''
nota=0
nombres=[]
notas=[]
while True:
    print("Para salir en cualquier momento introduzca '*' ")
    nombre=input("nombre del alumno: ")
    if nota=='*' or nombre=='*':
        break
    else:
        nombres.append(nombre)
    nota=input("nota del alumno: ")
    if nota=='*' or nombre=='*':
        break
    else:
        notas.append(nota)
    contador += 1
print(nombres)
print(notas)
print(contador)
with open('arq5.txt', 'w') as archivo:
    for i in range(contador):
        for j in range(40):
            if len(nombres[i])<40:
                nombres[i] += ' '
        archivo.write(nombres[i] +notas[i]+'\n')



print("'Dame un archivo con nombres y notas de alumnos (1 por linea, NOMBRE: blabla NOTA: 7) y te digo el nombre y la nota mas alta' Descartes")
nombre=''
nota=0.0
with open('arq5.txt') as archivo:
    lista1= archivo.readlines()
    print(lista1)
    total= len(lista1)
    archivo.seek(0)
    lista1 = archivo.readline().split()
    print(lista1)
    for i in range(total):
        if nota < float(lista1[3]):
            nombre= lista1[1]
            nota= float(lista1[3])
        lista1 = archivo.readline().split()
print(f"el alumno: {nombre} con un {nota}, es el alumno mas empoyon de la clase ")



print("'Dame archivo con el nombre y precio de productos (1 producto y precio por linea) y te digo el total de la compra' Descartes")
precio=0
with open('arq5.txt') as archivo:
    lista1= archivo.readlines()
    print(lista1)
    print(len(lista1))
    for i in range(len(lista1)):
        print(lista1[i])
        lista2= lista1[i].split()
        precio += float(lista2[1])
print(f"El total de la compra es: {precio}€")



print("'Dame archivo con el tamaño de una matrix, y luego debajo en cada linea la posicion para poner a cero ese elemento(fila, columna) y te creo otro archivo con la matriz resultante' Descartes")
contador=0
cadena=''
bandera= False
with open('arq5.txt') as archivo:
    lista= archivo.readline().split()
    print(lista)
    lista2= archivo.readlines()
    print(lista2)
    for i in range(int(lista[0])):
        print(f"fila {i}")
        for j in range(int(lista[1])):
            for k in range(int(lista[2])):
                if i== int(lista2[k][0]) and j==int(lista2[k][2]):
                    bandera=True
            if bandera==True:
                print('0', end=' ')
                cadena += ' 0 '
                bandera = False
            else:
                print('1', end=' ')
                cadena += ' 1 '
        print()
        print()
        cadena += '\n'
        print(f"{cadena}")
    print()
    with open('arq4.txt', 'w') as archivo2:
        archivo2.write(cadena)



print("'Dame un vectos con 10 numeros te los convierto a binario y te los guardo en un archivo de texto' Descartes")
numeros=[]
binarios=[]
for i in range(10):
    numeros.append(int(input(f"Numerito ahi[{i + 1}/10]:  ")))
print(numeros)
for i in numeros:
    cadena=str(bin(i))
    print(f"{i} en binerio {cadena[2:len(cadena)]}")
    with open("arq5.txt", 'a') as archivo:
        archivo.write(str(i) +' en binario es: '+ cadena[2:len(cadena)]+ '\n')



from datetime import datetime
print("'Dame un archivo con nombre y año de nacimiento (formato: AAAA) y te creo otro archivo con el nombre y la edad de la persona ' Descartes")
nombre = input("Mira, cual es le nombre del archivo de origen? ")
nombre2 = input("ah vale, y mira, cual es le nombre del archivo nuevo pa guardarte la edad de cada uno? ")
with open(nombre) as archivo:
    while True:
        cadena=''
        lista1=archivo.readline().split()
        if len(lista1) <= 1:
            break
        edad= datetime.now().year - int(lista1[1])
        if edad> 18:
            cadena= lista1[0] +' '+ str(edad)+' años,' + ' Es mayor de edad'
        elif edad<18:
            cadena = lista1[0] + ' ' + str(edad) + ' años,' + ' Es menor de edad'
        else:
            cadena = lista1[0] + ' ' + str(edad) + ' años,' + ' Eentrando en la mayorida de edad'
        print(lista1, end='')
        with open(nombre2, 'a') as archivo2:
            archivo2.write(cadena+ '\n')
        print(cadena)



from datetime import datetime
print("'Dame un archivo con nombre y nacimiento (formato: nombre DD MM AAAA) y te creo otro archivo con el nombre y la edad de la persona ' Descartes")
nombre = input("Mira, cual es le nombre del archivo? ")
nombre2 = input("ah vale, y mira, cual es le nombre del archivo nuevo pa guardarte la edad de cada uno? ")
with open(nombre) as archivo:
    while True:
        cadena=''
        lista1=archivo.readline().split()
        if len(lista1) <= 1:
            break
        edad= datetime.now().year - int(lista1[3])
        cadena= lista1[0] +' '+ str(edad)+' años'
        print(lista1, end='')
        with open(nombre2, 'a') as archivo2:
            archivo2.write(cadena+ '\n')
        print(cadena)



print("'Dame el nombre de la persona y el telefono y te los voy guardando como si fuera una agenda viste? hasta que escribas un '0' para el telefono, ahi paro' Descartes")
cadena=''
while True:
    nombre = input("Mira, cual es le nombre del contacto? ")
    telefono = input("Aaah vale y el telefono? ")
    cadena= nombre + ' ' + telefono
    if int(telefono) !=0:
        with open('arq4.txt', 'a') as archivo:
            archivo.write(cadena + '\n')
    else:
        break
print("metiste un '0' se acabó er programa")



print("'Dame el nombre de 1 archivo y te digo el numero de caracteres, numero de lineas, numero de palabras y las veces que esta repetida cada letra' Descartes")
lineas=0
palabras=0
caracteres=0
lista2=[]
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
I=0
J=0
k=0
l=0
m=0
n=0
o=0
p=0
q=0
r=0
s=0
t=0
u=0
v=0
w=0
x=0
y=0
z=0
nombre1=input("Mira, cual es le nombre del archivo que quieres contar las cosas? ")
with open(nombre1) as archivo:
    fichero= archivo.readlines()
    print(fichero)
lineas=len(fichero)
for i in fichero:
    lista1= i.split()
    lista2 += lista1
    print(lista1)
    palabras +=len(lista1)
for i in lista2:
    for j in i:
        if j in ('a','A'):
            caracteres += 1
            a+=1
        if j in ('b','B'):
            caracteres += 1
            b+=1
        if j in ('c','C'):
            caracteres += 1
            c+=1
        if j in ('d','D'):
            caracteres += 1
            d+=1
        if j in ('e','E'):
            caracteres += 1
            e+=1
        if j in ('f','F'):
            caracteres += 1
            f+=1
        if j in ('g','G'):
            caracteres += 1
            g+=1
        if j in ('h','H'):
            caracteres += 1
            h+=1
        if j in ('i','I'):
            caracteres += 1
            I+=1
        if j in ('j','J'):
            caracteres += 1
            J+=1
        if j in ('k','K'):
            caracteres += 1
            k+=1
        if j in ('l','L'):
            caracteres += 1
            l+=1
        if j in ('m','M'):
            caracteres += 1
            m+=1
        if j in ('o','O'):
            caracteres += 1
            o+=1
        if j in ('p','P'):
            caracteres += 1
            p+=1
        if j in ('q','Q'):
            caracteres += 1
            q+=1
        if j in ('r','R'):
            caracteres += 1
            r+=1
        if j in ('s','S'):
            caracteres += 1
            s+=1
        if j in ('t','T'):
            caracteres += 1
            t+=1
        if j in ('u','U'):
            caracteres += 1
            u+=1
        if j in ('v','V'):
            caracteres += 1
            v+=1
        if j in ('w','W'):
            caracteres += 1
            w+=1
        if j in ('x','X'):
            caracteres += 1
            x+=1
        if j in ('y','Y'):
            caracteres += 1
            y+=1
        if j in ('z','Z'):
            caracteres += 1
            z+=1
print(f"lineas: {lineas}")
print(f"palabras: {palabras}")
print(f"caracteres: {caracteres}")
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")
print(f"e: {e}")
print(f"f: {f}")
print(f"h: {h}")
print(f"i: {I}")
print(f"j: {J}")
print(f"k: {k}")
print(f"l: {l}")
print(f"m: {m}")
print(f"n: {n}")
print(f"o: {o}")
print(f"p: {p}")
print(f"q: {q}")
print(f"r: {r}")
print(f"s: {s}")
print(f"t: {t}")
print(f"u: {u}")
print(f"v: {v}")
print(f"w: {w}")
print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")



print("'Dame el nombre de 1 archivo con nombres de cidades y poblacion en cada linea y otro nombre de archivo y te guarda en el la ciudad mas poblada' Descartes")
print("El nombre de la ciudad siempre tiene un tamaño fijo de 40 caracteres MAXIMO si el nombre de la ciudad es menor, el resto se rellena con espacios en blanco hasta llegar a los 40")
cadena=''
pob=''
poblacion=0
nombre1=input("Mira, cual es le nombre del archivo con los paises? ")
nombre2=input("Mira, cual es le nombre del archivo pa guardarte el pais mas poblado? ")
with open(nombre1) as archivo:
    fichero= archivo.readlines()
for i in fichero:
    pob = ''
    print(i, end= '')
    for j in range(40, len(i)):
        pob += i[j]
    if int(pob) > poblacion:
        poblacion= int(pob)
        cadena= i
print(f"el mayor es: {cadena}")
with open(nombre2, 'w') as archivo2:
    archivo2.write(cadena)



print("'Dame el nombre de 2 archivos de texto existente y te creo uno nuevo con el nombre que quieras y con el contenido del primero + el segundo' Descartes")
cadena=''
nombre1=input("Mira, cual es le nombre del archivo 1? ")
nombre2=input("Mira, cual es le nombre del archivo 2? ")
nombre3=input("Mira, cual es le nombre del archivo que tiene archivo1 + archivo2? ")
with open(nombre1) as archivo1:
    fichero1= archivo1.readlines()
    for i in fichero1:
        cadena += i
with open(nombre2) as archivo2:
    fichero2= archivo2.readlines()
    for i in fichero2:
        cadena += i
with open(nombre3, 'w') as archivo3:
    archivo3.write(cadena)



print("'Dame el nombre de un archivo de texto existente y te creo otro igual, con el nombre que quieras pero con todo en mayusculas' Descartes")
cadena=''
nombre1=input("Mira, cual es le nombre del archivo? ")
with open(nombre1) as archivo:
    fichero= archivo.readlines()
    print(fichero)
for i in range(len(fichero)):
    print(fichero[i].upper())
    cadena += fichero[i].upper()
print(cadena)
nombre1=input("Mira, cual es le nombre del archivo pa guardarte todo eso en mayuscula? ")
with open(nombre1, 'w') as archivo2:
    archivo2.write(cadena)



print("'Dame un archivo de texto y te creo otro igual pero con las vocales sustituidas por un asterisco (*)' Descartes")
cadena=''
with open('arq.txt') as archivo:
    fichero= archivo.readlines()
    print(fichero)
for i in range(len(fichero)):
    for j in fichero[i]:
        print(j)
        if j in ('a','e','i','o','u','A','E','I','O','U'):
            cadena += 'x'
        else:
            cadena += j
print(cadena)
with open('arq2.txt', 'w') as archivo2:
    archivo2.write(cadena)



print("'Dame un archivo de texto y te digo cuantas veces se repite cada letra del abecedario en el archivo' Descartes")
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
J=0
k=0
l=0
m=0
n=0
o=0
p=0
q=0
r=0
s=0
t=0
u=0
v=0
w=0
x=0
y=0
z=0
with open('arq.txt') as archivo:
    fichero= archivo.readlines()
    print(fichero)
print(f"{len(fichero)} linea/s")
for i in range(len(fichero)):
    for j in fichero[i]:
        if j in ('a','A'):
            a +=1
        if j in ('b','B'):
            b +=1
        if j in ('c','C'):
            c +=1
        if j in ('d','D'):
            d +=1
        if j in ('e','E'):
            e +=1
        if j in ('f','F'):
            f +=1
        if j in ('g','G'):
            g +=1
        if j in ('h','H'):
            h +=1
        if j in ('i','I'):
            i +=1
        if j in ('j','J'):
            J +=1
        if j in ('k','K'):
            k +=1
        if j in ('l','L'):
            l +=1
        if j in ('m','M'):
            m +=1
        if j in ('n','N'):
            n +=1
        if j in ('o','O'):
            o +=1
        if j in ('p','P'):
            p +=1
        if j in ('q','Q'):
            q +=1
        if j in ('r','R'):
            r +=1
        if j in ('s','S'):
            s +=1
        if j in ('t','T'):
            t +=1
        if j in ('u','U'):
            u +=1
        if j in ('v','V'):
            v +=1
        if j in ('w','W'):
            w +=1
        if j in ('x','X'):
            x +=1
        if j in ('y','Y'):
            y +=1
        if j in ('z','Z'):
            z +=1
print(f"a={a}")
print(f"b={b}")
print(f"c={c}")
print(f"d={d}")
print(f"e={e}")
print(f"f={f}")
print(f"g={g}")
print(f"h={h}")
print(f"i={i}")
print(f"j={J}")
print(f"k={k}")
print(f"l={l}")
print(f"m={m}")
print(f"n={n}")
print(f"o={o}")
print(f"p={p}")
print(f"q={q}")
print(f"r={r}")
print(f"s={s}")
print(f"t={t}")
print(f"u={u}")
print(f"v={v}")
print(f"w={w}")
print(f"x={x}")
print(f"y={y}")
print(f"z={z}")



print("'Dame un archivo de texto y una letra cualquiera y te digo cuantas veces se repite en el archivo' Descartes")
contador=0
letra= input("Mira perdona, que letra quieres buscar? ")
with open('arq.txt') as archivo:
    fichero= archivo.readlines()
    print(fichero)
print(f"{len(fichero)} linea/s")
for i in range(len(fichero)):
    for j in fichero[i]:
        if j == letra:
            contador +=1
if contador>0:
    print(f"Mira perdona, la letra que tu querias, la '{letra}', esta repetida {contador} vez/veces")
else:
    print(f"Mira perdona, no tengo '{letra}', te las mando a pedir?")



print("'Dame un archivo de texto y te digo cuantas letras vocales y consonantes tienes guardadas dentro' Descartes")
vocal=0
consonante=0
with open('arq.txt') as archivo:
    fichero= archivo.readlines()
    print(fichero)
print(f"{len(fichero)} linea/s")
for i in range(len(fichero)):
    for j in fichero[i]:
        if j in ('a','e','i','o','u','A','E','I','O','U'):
            vocal +=1
        elif j != ' ' and j !='1' and j !='2'and j !='3'and j !='4'and j !='5'and j !='6'and j !='7'and j !='8'and j !='9'and j !='0' and j !='\n':
            consonante +=1
print(f"Dentro de tu fichero tienes {vocal} vocale/s y {consonante}consonante/s")



print("'dame un archivo de texto y te digo cuantas líneas tienes guardadas dentro' Descartes")
texto= input("Hola, dime donde esta con su rutita y nombre del fichero(ejemplo: C:/Users/Arioc/texto.txt): ")
with open(texto) as archivo:
    print("Tu fichero tiene", end=' ')
    print(f"{len(archivo.readlines())} lineas")



print("'Dame todos los caracteres que quieras y creo creo un archivo pa guardartelo hasta que metas un cero (0)' Descartes")
with open('arq.txt', 'w') as archivo:
    while True:
        letras= input("Tu mete caracteres aqui y para salir escribe el numero cero (0)")
        if letras !='0':
            archivo.write(letras+'\n')
        else:
            break
print()
with open('arq.txt') as archivo:
    print(archivo.read())
"""