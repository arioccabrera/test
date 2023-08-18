import random
import string
print("'Dame 1 matriz 20x20 y te digo cual es el mayor producto de 4 numeros adjacentes' Descartes")
A=[]
calculo=0
mayor=0
mayores=[0,0,0,0]
print()
for i in range(20):
    A.append([random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)])
print()
print("Matriz 1")
for i in A:
    print(i)
print()



"""
import random
print("'Dame 1 matriz 20x20 y te digo cual es el mayor producto de 4 numeros adjacentes' Descartes")
A=[]
calculo=0
mayor=0
mayores=[0,0,0,0]
print()
for i in range(20):
    A.append([random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)])
print()
print("Matriz 1")
for i in A:
    print(i)
print()
for i in range(3,17,1):
    for j in range(3,17,1):
        if (A[i][j] * A[i][j - 1] * A[i][j - 2] * A[i][j - 3])> mayor:
            mayor=A[i][j] * A[i][j - 1] * A[i][j - 2] * A[i][j - 3]
            mayores=[f'i:{i},j:{j}={A[i][j]}', f'i:{i},j:{j-1}={A[i][j - 1]}', f'i:{i},j:{j-2}={A[i][j - 2]}', f'i:{i},j:{j-3}={A[i][j - 3]}']
        elif (A[i][j] * A[i-1][j - 1] * A[i-2][j - 2] * A[i-3][j - 3])> mayor:
            mayor=A[i][j] * A[i-1][j - 1] * A[i-2][j - 2] * A[i-3][j - 3]
            mayores = [f'i:{i},j:{j}={A[i][j]}', f'i:{i-1},j:{j - 1}={A[i-1][j - 1]}', f'i:{i-2},j:{j - 2}={A[i-2][j - 2]}',f'i:{i-3},j:{j - 3}={A[i-3][j - 3]}']
        elif (A[i][j] * A[i-1][j] * A[i-2][j] * A[i-3][j])> mayor:
            mayor= A[i][j] * A[i-1][j] * A[i-2][j] * A[i-3][j]
            mayores= [f'i:{i},j:{j}={A[i][j]}', f'i:{i-1},j:{j}={A[i-1][j]}', f'i:{i-2},j:{j}={A[i-2][j]}',f'i:{i-3},j:{j}={A[i-3][j]}']
        elif (A[i][j] * A[i - 1][j+1] * A[i - 2][j+2] * A[i - 3][j+3])> mayor:
            mayor=A[i][j] * A[i - 1][j+1] * A[i - 2][j+2] * A[i - 3][j+3]
            mayores= [f'i:{i},j:{j}={A[i][j]}', f'i:{i-1},j:{j+1}={A[i-1][j+1]}', f'i:{i-2},j:{j+2}={A[i-2][j+2]}',f'i:{i-3},j:{j+3}={A[i-3][j+3]}']
        elif (A[i][j] * A[i][j+1] * A[i][j+2] * A[i][j+3])> mayor:
            mayor= A[i][j] * A[i][j+1] * A[i][j+2] * A[i][j+3]
            mayores= [f'i:{i},j:{j}={A[i][j]}', f'i:{i},j:{j+1}={A[i][j+1]}', f'i:{i},j:{j+2}={A[i][j+2]}',f'i:{i},j:{j+3}={A[i][j+3]}']
        elif (A[i][j] * A[i + 1][j + 1] * A[i + 2][j + 2] * A[i + 3][j + 3])> mayor:
            mayor= A[i][j] * A[i + 1][j + 1] * A[i + 2][j + 2] * A[i + 3][j + 3]
            mayores= [f'i:{i},j:{j}={A[i][j]}', f'i:{i+1},j:{j+1}={A[i+1][j+1]}', f'i:{i+2},j:{j+2}={A[i+2][j+2]}',f'i:{i+3},j:{j+3}={A[i+3][j+3]}']
        elif (A[i][j] * A[i + 1][j] * A[i + 2][j] * A[i + 3][j])> mayor:
            mayor= A[i][j] * A[i + 1][j] * A[i + 2][j] * A[i + 3][j]
            mayores= [f'i:{i},j:{j}={A[i][j]}', f'i:{i+1},j:{j}={A[i+1][j]}', f'i:{i+2},j:{j}={A[i+2][j]}',f'i:{i+3},j:{j}={A[i+3][j]}']
        elif (A[i][j] * A[i + 1][j - 1] * A[i + 2][j - 2] * A[i + 3][j - 3])> mayor:
            mayor= A[i][j] * A[i + 1][j - 1] * A[i + 2][j - 2] * A[i + 3][j - 3]
            mayores= [f' (i:{i},j:{j}) {A[i][j]} ',f' (i:{i+1},j:{j-1}) {A[i+1][j-1]} ',f' (i:{i+2},j:{j-2}) {A[i+2][j-2]} ',f' (i:{i+3},j:{j-3}) {A[i+3][j-3]} ']
print(f" el mayor producto es {mayor} y corresponde a los numeros {mayores}")



print("'Dame 2 matrices 2x2 con valores reales y te las muestro en pantalla' Descartes")
A=[]
B=[]
suma=0
media=[]
print()
print("Matriz 1")
for i in range(2):
    print(f"Numeros fila {i+1}")
    A.append([float(input(f"Numero 1: ")),float(input(f"Numero 2: "))])
print()
print("Matriz 2")
for i in range(2):
    print(f"Numeros fila {i+1}")
    B.append([float(input(f"Numero 1: ")),float(input(f"Numero 2: "))])
print()
print("Matriz 1")
for i in A:
    print(i)
print()
print("Matriz 2")
for i in B:
    print(i)
print()



print("'Dame una matriz 3x6 con valores reales y te sumo las columna impares, te hago la media de los elementos de las columnas 2 y 4, y sustituyo los valores de la columna 6 por la suma de cada elemento de las columnas 1 y 2' Descartes")
A=[]
suma=0
media=[]
for i in range(3):
    print(f"Numeros fila {i+1}")
    A.append([float(input(f"Numero 1: ")),float(input(f"Numero 2: ")),float(input(f"Numero 3: ")),float(input(f"Numero 4: ")),float(input(f"Numero 5: ")),float(input(f"Numero 6: "))])
for i in A:
    print(i)
print()
for i in range(3):
    for j in range(6):
        if (j+1)%2!=0 or j==0:
            suma += A[i][j]
print(f"La suma de las columnas impares es: {suma}")
for i in range(3):
    for j in range(6):
        if j==1 or j==3:
            media.append(A[i][j])
print(f"La media de los elementos en columnas 2 y 4 es: {sum(media)/len(media)}")
print()
print("Ahora el resultado de la suma de los elementos de las columnas 1 y 2 lo voy a guardar en la columna 5")
for i in range(3):
    suma = 0
    for j in range(2):
        suma += A[i][j]
    A[i][5] =suma
print()
print("La nueva matriz:")
for i in A:
    print(i)
print()



print("'Dame una matriz 5x4 que contiene informaciones de alumnos(C1:matricula de alumno, C2: media examenes, C3: media de trabajos, C4: nota final=C2+C3' Descartes")
A=[]
mayor=[]
suma=0
for i in range(5):
    A.append([int(input(f"Numero matricula del Alumno{[i+1]}= ")),float(input(f"Nota media de examenes del Alumno{[i+1]}= ")),float(input(f"Nota media de trabajos del Alumno{[i+1]}="))])
for i in A:
    print(i)
print()
for i in range(5):
    suma=0
    for j in range(1,3):
        suma += A[i][j]
    A[i].append(suma)
for i in A:
    print(i)
print()
for i in range(5):
    mayor.append(A[i][3])
print(f"La mayor nota es: {max(mayor)} y pertenece al alumno con numero de matricula: {A[mayor.index(max(mayor))][0]}")
mayor.clear()
for i in range(5):
    mayor.append(A[i][3])
print(f"La nota media de las notas finales de los 5 alumnos es: {sum(mayor)/len(mayor):.2f}")



print("'Dame una matriz 3x3 y te creo un vector unidimensional en que cada elemendto coincide con la suma de cada columna' Descartes")
A=[]
B=[]
suma=0
for i in range(3):
    A.append([int(input(f"disme valor de: A{[i],0}=")),int(input(f"disme valor de: A{[i],1}=")),int(input(f"disme valor de: A{[i],2}="))])
for i in A:
    print(i)
print()
for j in range(3):
    suma=0
    for i in range (3):
        suma += A[i][j]
    B.append(suma)
print(B)



import random
print("'Dame una matriz 10x3 refiriendose a las notas de 10 alumnos en 3 pruebas y te digo cual fue el mas burro de cada prueba' Descartes")
A=[]
peor=0
B=[]
for i in range(10):
    A.append([random.randint(0,10),random.randint(0,10),random.randint(0,10)])
for i in A:
    print(i)
print()
print()
for j in range(3):
    B.clear()
    for i in range(10):
            B.append(A[i][j])
    peor=min(B)
    print(f"El alumno {B.index(peor)+1} obtuvo la peor de la prueba {j+1} con {peor} puntos")



import random
import string
print("'Dame una matriz 5x3 refiriendose a las respuestas de 10 preguntas tipo test de 3 alumnos, una plantilla de respuestas y el porcentaje de aciertos y sus respuestas guardadas en un DIC' Descartes")
A=[]
B=['a','b','c','c','e','a','e','a','a','d']
resultado={}
aciertos=0
for i in range(3):
    A.append([chr(random.randint(ord('a'), ord('e'))),chr(random.randint(ord('a'), ord('e'))),chr(random.randint(ord('a'), ord('e'))),chr(random.randint(ord('a'), ord('e'))),chr(random.randint(ord('a'), ord('e'))),chr(random.randint(ord('a'), ord('e'))),chr(random.randint(ord('a'), ord('e'))),chr(random.randint(ord('a'), ord('e'))),chr(random.randint(ord('a'), ord('e'))),chr(random.randint(ord('a'), ord('e')))])
for i in A:
    print(i)

print()
print(B)

for i in range(3):
    aciertos=0
    for j in range(10):
        if A[i][j]==B[j]:
            aciertos +=1
    resultado[f'alumno {i+1}']= f'{((aciertos * 100) / 10)}% acertado', A[i]
    print(f"El alumno {i+1} tuvo {aciertos} acierto/s")
print()
print(resultado)



import random
import string
print("'Dame una matriz 5x10 refiriendose a las respuestas de 10 preguntas tipo test de 5 alumnos, una plantilla de respuestas y te digo los aprobados' Descartes")
A=[]
B=['a','b','c','c','d','a','b','a','a','d']
resultado={}
aciertos=0
for i in range(5):
    A.append([chr(random.randint(ord('a'), ord('d'))),chr(random.randint(ord('a'), ord('d'))),chr(random.randint(ord('a'), ord('d'))),chr(random.randint(ord('a'), ord('d'))),chr(random.randint(ord('a'), ord('d'))),chr(random.randint(ord('a'), ord('d'))),chr(random.randint(ord('a'), ord('d'))),chr(random.randint(ord('a'), ord('d'))),chr(random.randint(ord('a'), ord('d'))),chr(random.randint(ord('a'), ord('d')))])
for i in A:
    print(i)
print()
print(B)
for i in range(5):
    aciertos=0
    for j in range(10):
        if A[i][j]==B[j]:
            aciertos +=1
    resultado[f'alumno {i+1}']=aciertos
    print(f"El alumno {i+1} tuvo {aciertos} acierto/s")
print()
print(resultado)



import random
print("'Dame una matriz 5x5 y te creo unos cartones de bingo guapisimos(con numeros del 0 al 99 y sin repetirse en toda la matriz' Descartes")
A=[]
B={}
B=set(B)
num=0
contador=0
for i in range(5):
    A.append([random.randint(0,99),random.randint(0,99),random.randint(0,99),random.randint(0,99),random.randint(0,99)])
for i in range(5):
    for j in range(5):
        B.add(A[i][j])
if len(B)==25:
    num=25
else:
    B.clear()
    while num!=25:
        for i in range(5):
            for j in range(5):
                A[i][j]=random.randint(0,99)
        for i in range(5):
            for j in range(5):
                B.add(A[i][j])
        if len(B) == 25:
            num = 25
        else:
            B.clear()
        contador += 1
print()
print(f"despues de {contador} intentos consegui create un carton pal binguito, gozatelo")
print(len(B), end= ' ')
print(B)
print()
for i in A:
    print(i)



import random
print("'Dame una matriz 4x4 y te la transforma en una triangular inferior (a 0 todo lo que esta encima de la diagonal princial)' Descartes")
A=[]
num=0
for i in range(4):
    A.append([random.randint(1,20),random.randint(1,20),random.randint(1,20),random.randint(1,20)])
for i in A:
    print(i)

print()
for i in range(4):
    for j in range(4):
        if i<j:
            A[i][j]=0
print("La triangular inferior es:")
for i in A:
    print(i)



import random
print("'Dame una matriz 3x3 y te calculo su traspuesta' Descartes")
A=[]
num=0
for i in range(3):
    A.append([random.randint(1,20),random.randint(1,20),random.randint(1,20)])
for i in A:
    print(i)

print()
for i in range(3):
    for j in range(3):
        if i>j:
            num=A[i][j]
            A[i][j]=A[j][i]
            A[j][i]=num
print("La traspuesta es:")
for i in A:
    print(i)



import random
print("'Dame una matriz 3x3 y te calculo la suma de los elementos de la diagonal secundaria' Descartes")
A=[]
suma=0
num=0
for i in range(3):
    A.append([random.randint(1,20),random.randint(1,20),random.randint(1,20)])
for i in A:
    print(i)
A.reverse()
print()
for i in range(3):
    for j in range(3):
            if i==j:
                suma += A[i][j]
                print(A[i][j], end=' +')
A.reverse()
print(f"={suma}")



import random
print("'Dame una matriz 3x3 y te calculo la suma de los elementos de la diagonal principal' Descartes")
A=[]
suma=0
for i in range(3):
    A.append([random.randint(1,20),random.randint(1,20),random.randint(1,20)])
for i in A:
    print(i)
for i in range(3):
    for j in range(3):
        if j==i:
            suma += A[i][j]
            print(A[i][j], end=' +')
print(f"={suma}")




import random
print("'Dame una matriz 3x3 y te calculo la suma de los elementos por debajo de la diagonal principal' Descartes")
A=[]
suma=0
for i in range(3):
    A.append([random.randint(1,20),random.randint(1,20),random.randint(1,20)])
for i in A:
    print(i)
for i in range(3):
    for j in range(3):
        if j<i:
            suma += A[i][j]
            print(A[i][j], end=' +')
print(f"={suma}")



import random
print("'Dame una matriz 3x3 y te calculo la suma de los elementos por encima de la diagonal principal' Descartes")
A=[]
suma=0
for i in range(3):
    A.append([random.randint(1,20),random.randint(1,20),random.randint(1,20)])
for i in A:
    print(i)
for i in range(3):
    for j in range(3):
        if j>i:
            suma += A[i][j]
            print(A[i][j], end=' +')
print(f"={suma}")



print("'Dame una matriz 10x10 y te calculo sus elementos con unas formulas para i>j, i=j e i<j' Descartes")
print("i<j: A[i][j]= 2*i +7*j -2")
print("i==j: A[i][j]=3*(i**2)-1")
print("i>j: A[i][j]= 4*(i**3)-5*(j**2)+1")
A=[]
for i in range(10):
    A.append([0,0,0,0,0,0,0,0,0,0])
for i in A:
    print(i)
for i in range(10):
    for j in range(10):
        if i<j:
            A[i][j]= 2*i +7*j -2
        elif i==j:
            A[i][j]=3*(i**2)-1
        else:
            A[i][j]= 4*(i**3)-5*(j**2)+1
for i in A:
    print(i)



import random
print("'Dame una matriz 5x5, un valor X y te digo si ese valor esta en la matriz y su posicion' Descartes")
A=[]
B=[]
C=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(4):
    A.append([random.randint(1,20),random.randint(1,20),random.randint(1,20),random.randint(1,20)])
    B.append([random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)])
for i in range(4):
    print(A[i])
print()
for i in range(4):
    print(B[i])
print()
for i in range(4):
    for j in range(4):
        if A[i][j]>B[i][j]:
            C[i][j]=A[i][j]
        else:
            C[i][j] = B[i][j]
print("Los numeros mayores de cada fila/columna de las dos matrices anteriores son:")
for i in range(4):
    print(C[i])



import random
print("'Dame una matriz 5x5, un valor X y te digo si ese valor esta en la matriz y su posicion' Descartes")
A=[]
existe= False
for i in range(5):
    A.append([random.randint(1,20),random.randint(1,20),random.randint(1,20),random.randint(1,20),random.randint(1,20)])
for i in A:
    print(i)
num=int(input("Que numero buscabas? "))
for i in range(5):
    for j in range(5):
        if A[i][j]==num:
            print(f"El {num} está en la matriz y se encuentra en la linea:{i}, columna:{j}")
            existe= True
if not existe:
    print(f"Mira, no me quedan más {num}")
print()
for i in A:
    print(i)



print("'Dame una matriz 4x4 y te guardo en cada elemento el producto del numero de la fila por la columna en que se encuentra' Descartes")
A=[]
for i in range(4):
    A.append([0,0,0,0])
for i in A:
    print(i)
for i in range(4):
    for j in range(4):
        A[i][j]=i*j
print()
for i in A:
    print(i)



print("'Dame una matriz 5x5, te pongo a 1 la diagonal principal y el resto a cero' Descartes")
A=[]
contador=0
for i in range(5):
    A.append([1,1,1,1,1])
for i in A:
    print(i)
print()
for i in range(5):
    for j in range(5):
        if i==j:
            A[i][j]=1
        else:
            A[i][j] = 0
for i in A:
    print(i)



print("'Dame una matriz 4x4 y te digo los elementos mayores de 10' Descartes")
A=[[2,3,4,15],[10,2,5,7],[10,20,8,4],[10,10,10,10]]
contador=0
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j]>=10:
            contador += 1
print(f" Hay {contador} numeros mayores o iguales que 10")
"""