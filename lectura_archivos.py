

import os
import tempfile


archivo= tempfile.TemporaryFile()
archivo.write(b"hola hola hola")

print(archivo.name)
print(archivo.read())
input()
archivo.close()
"""
with tempfile.TemporaryFile() as temporal:
    temporal.write(b"hola hola hola")
    temporal.seek(0)
    print(temporal.read())

with tempfile.TemporaryDirectory() as  temporal:
    print(f"cree un directorio temporal {temporal}")
    with open(os.path.join(temporal, "archivo_temporal.txt"), 'w') as archivo:
        archivo.write("estoy escribiendo en un temporal")
    input()



from send2trash import send2trash

send2trash("cambiado")


print(os.path.exists("texto.txt"))
print(os.path.exists("C:\\Users\\Arioc"))

open("archivo_test.txt", 'w').close()
open("archivo_test2.txt", 'a').close()

with open("archivo_test3.txt", 'a') as archivo:
    pass

#os.mknod('archivo_test4.txt')
#os.mknod("C:\\Users\\Arioc\\archivo_test4.txt")
#os.mkdir("templates")
#os.mkdir("C:\\Users\\Arioc\\templates3")
#os.makedirs("template1/template2/template3/template4", exist_ok=True)
#os.rename("nuevo", "cambiado")
#os.rename("template1/template2/template3/template4/prueba.txt", "template1/template2/template3/template4/nuevo.txt")
#os.remove("templates")
#os.rmdir("template1")

for archivo in os.scandir('template1'):
    print(f"{archivo.name}")
    if archivo.is_file():
        os.remove(archivo.path)

os.removedirs("template1\\template2\\template3\\template4")
print(os.getcwd())

os.chdir('..')
print(os.getcwd())

print(os.path.isabs('Arioc/PycharmProjects'))

print(os.name)

import sys
print(sys.platform)

print()
print()


print(os.getcwd())

nuevo= os.path.join(os.getcwd(),"tests")

os.chdir(nuevo)
print(os.getcwd())


print(os.listdir("C:\\"))
print(len(os.listdir("C:\\")))

print(list(os.scandir("C:\\")))

archivos=list(os.scandir("C:\\"))

print(archivos[0].inode())
print(archivos[0].is_dir())
print(archivos[0].is_file())
print(archivos[0].is_symlink())
print(archivos[0].name)
print(archivos[0].path)
print(archivos[0].stat())

os.scandir.close()


from io import StringIO

mensage= "Esto es solo una string normal"
archivo= StringIO(mensage)
print(archivo.read())
archivo.write("otro  texto de prueba")
archivo.seek(0)
print(archivo.read())


with open("frutas.txt", "a") as fichero:
    while True:
        fruta= input("Que frutas quieres, cariño? o dime 'salir' asi como suena cuando no quieras mas nada: ")
        if fruta != "salir":
            fichero.write(fruta + '\n')
        else:
            break


with open("frutas.txt", "w") as fichero:
    while True:
        fruta= input("Que frutas quieres, cariño? o dime 'salir' asi como suena cuando no quieras mas nada: ")
        if fruta != "salir":
            fichero.write(fruta + '\n')
        else:
            break


with open("texto2.txt","w") as  archivo:
    archivo.write("Hola pibe \n" * 100)


with open("texto.txt") as archivo:
    print(archivo.readlines())
    print(archivo.closed)

print(archivo.closed)
print(archivo.read())



archivo= open('texto.txt')
print(archivo.read(50))
print(archivo.closed)
archivo.close()
print(archivo.closed)
print(archivo.read(50))



print(archivo.readline())
print(archivo.readline())
print(archivo.readline())

archivo= open('texto.txt')

print("read 1")
print(archivo.read())
print("read 2")
print(archivo.read())
archivo.seek(0)
print("read 3")
print(archivo.read())



archivo= open('texto.txt')

print(archivo)
print(type(archivo))


print(archivo.read())
print(archivo.read())"""