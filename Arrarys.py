



"""
print("'Dame 10 elementos te los guardo en un vector y no te dejo guardar los que esten repes' Descartes")
A=[]
B=[]
C=[]
a=0
b=0
suma1= False
num=1

a=int(input("Numero1 positivo menor de 10_000: "))
b=int(input("Numero2 positivo menor de 10_000: "))
while a >10_000 or b >10_000:
    print("Error, inserta numero menor de 10_000 ahí")
    a=int(input("Numero1 positivo menor de 10_000: "))
    b=int(input("Numero2 positivo menor de 10_000: "))

A=list(str(a))
B=list(str(b))
print(A)
print(B)
A.reverse()
B.reverse()
print()
print(A)
print(B)

if len(A)<len(B):
    for i in range(len(A)):
        if suma1:
            C.append(int(A[i])+int(B[i])+1)
        else:
            C.append(int(A[i]) + int(B[i]))

        if i==0 and (int(A[i]) + int(B[i])) >= 10:
            C[i] = (int(A[i]) + int(B[i])) - 10
            suma1 = True
        elif i>0 and (int(A[i])+int(B[i])) >= 10:
            C[i]= (int(A[i])+int(B[i])+1)-10
            suma1= True
        else:
            suma1 = False

else:
    for i in range(len(B)):
        print(f"i={i}")
        if suma1:
            C.append(int(A[i]) + int(B[i])+ 1)
        else:
            C.append(int(A[i]) + int(B[i]))

        if i==0 and (int(A[i]) + int(B[i])) >= 10:
            C[i] = (int(A[i]) + int(B[i])) - 10
            suma1 = True
        elif i>0 and (int(A[i])+int(B[i])) >= 10:
            C[i]= (int(A[i])+int(B[i])+1)-10
            suma1= True
        else:
            print("suma false")
            suma1 = False


print(len(A))
print(len(B))
if len(A)>len(B):
    for i in range(len(B), len(A), 1):
        if suma1:
            C.append(int(A[i])+1)
            suma1 = False
        else:
            C.append(int(A[i]))

elif len(B)>len(A):
    for i in range(len(A), len(B), 1):
        if suma1:
            C.append(int(B[i])+1)
            suma1 = False
        else:
            C.append(int(B[i]))

print()
C.reverse()
A.reverse()
B.reverse()
print(f"A{A}")
print(f"B{B}")
print(f"C{C}")



print("'Dame 10 elementos te los guardo en un vector y no te dejo guardar los que esten repes' Descartes")
A=[]
num=0
contador=0
num=int(input("Numero pal vector: "))
while contador<10:
    if num in A:
        print("Dame un numero que no esté repetido anda, no me hagas calental")
    else:
        A.append(num)
        contador+=1
    num = int(input("Numero pal vector: "))
    print(f"Contador{contador}")
print(A)



print("'Dame 1 vectores con 15 elementos, te elimino los elementos con valor '0' y ruedo a la izquierda los que están despues de este' Descartes")
A=[]
for i in range(15):
    A.append(int(input(f"Numero ({i+1}/15) pal vector A: ")))
print(A)
for i in A[::-1]:
    print()
    print(f"voy por {i}")
    if i==0:
        print(f"index{A.index(i)}", end=' ')
        print(" Elimino: ", end='')
        print(A.pop(A.index(i)))
    print(A)
print(A)



print("'Dame 2 vectores con 10 elementos y te guardo en otro los valores de ambos sin estar repetidos' Descartes")
A=[]
B=[]
C={}
for i in range(10):
    A.append(int(input(f"Numero ({i+1}/10) pal vector A: ")))
    B.append(int(input(f"Numero ({i+1}/10) pal vector B: ")))
print(A)
print(B)
A=set(A)
B=set(B)
#C= set(A+B)
C= A.union(B)
print(A)
print(B)
print(C)



print("'Dame 2 vectores con 10 elementos y te guardo en otro los valores comunes de ambos' Descartes")
A=[]
B=[]
for i in range(10):
    A.append(int(input(f"Numero ({i+1}/10) pal vector A: ")))
    B.append(int(input(f"Numero ({i+1}/10) pal vector B: ")))

print(A)
print(B)
A=set(A)
B=set(B)
C= A.intersection(B)
print(A)
print(B)
print(C)



print("'Dame 6 enteros en un vector y te digo los pares y te los sumo o los impares y te digo cuantos hay' Descartes")
A=[]
suma=0
contador=0
for _ in range(6):
    A.append(int(input("Numero cualquier pal vector: ")))
for i in A:
    if i%2==0:
        suma += i
    else:
        contador += 1
print(A)
print(f"Suma de pares: {suma}")
print(f"total de impares de pares: {contador}")



print("'Dame 10 enteros en un vector 'V' y guardo los pares e impares en dos vectores V1 y V2' Descartes")
V=[]
V1=[]
V2=[]
for _ in range(10):
    V.append(int(input("Numero cualquier pal vector: ")))
for i in V:
    if i%2==0:
        V2.append(i)
    else:
        V1.append(i)
print(f"pares, V2={V2}")
print(f"Impares, V1={V1}")



print("'Da 10 enteros en un vector y te digo cuales son primos y su posicion' Descartes")
A=[]
primo=True
for i in range(10):
    A.append(int(input("Numero par vertor :")))
print(A)
for i in A:
    primo = True
    for j in range(2,i):
        if (i%j==0 and i!=2) or (i%j==0 and i!=1):
            primo= False
    if primo:
        print(f"A[{A.index(i)}]={i}")



import math
print("'Te calculo el desvio  de un vector para n=10 numeros' Descartes")
A=[]
desvio=0
sumatorio=0
media=0
for i in range(10):
    numero=float(input("Numero pal desvio ahí: "))
    A.append(numero)
media=sum(A)/len(A)
for i in A:
    sumatorio += pow((i-media),2)
desvio = math.sqrt((1 / (len(A) - 1))*sumatorio)
print(f"{desvio:.2f}")



print("'Te imprimo un vector de los 100 primeros naturales NO multiplos de 7 o acabados en 7' Descartes")
A=[]
contador=0
i=0
j=0
while contador<100:
    j=str(i)
    print(f"j:{j}, i {i}")
    print(f"tamaño J: {len(j)}, ultimo numero J:{j[len(j)-1]}")

    if i%7!=0 or (int(j[len(j)-1]))==7:
        if i%7!=0:
            print(f"{i} no es multipo de 7")
        if (int(j[len(j) - 1])) == 7:
            print(f"i={i} acaba en 7")
        A.append(i)
        contador += 1
    print()
    i+= 1
print()
print(contador)
print(i)
print(A)



print("'Dame 10 conjuntos de 2 elementos(ID alumno: altura) y te digo el mas bajo y el más alto' Descartes")
A={}
numero=0
altura=0
for _ in range(5):
    numero=int(input("ID del alumno: "))
    altura=float(input("Altura del alumno(en metros): "))
    A[numero]=altura
print()
for key in A.keys():
    if A[key] == min(A.values()):
        print(f" El alumno mas bajito mide: {min(A.values())} y su ID es:{key} ")
    elif A[key] == max(A.values()):
        print(f" El alumno mas alto mide: {max(A.values())} y su ID es: {key} ")
print()
print(A.keys())
print(A.values())



print("'Dame 2 vectores con 5 reales y te creo otro con el producto escalar de los 2' Descartes")
A=[]
B=[]
escalar=0
for i in range(5):
    print()
    A.append(int(input(f"Numerito ({i+1}/5) pal vectorito A:")))
    print()
    B.append(int(input(f"Numerito ({i+1}/5) pal vectorito B:")))
print(f"A= {A}")
print(f"B= {B}")
for i in range(5):
    escalar += A[i]*B[i]
    print(f"+ A[{i}]={A[i]} x B[{i}]={B[i]}", end=' ')
print(f"= {escalar}")



print("'Dame 2 vectores con 10 enteros y te creo otro con la resta de los 2' Descartes")
A=[]
B=[]
C=[]
indexA=0
indexB=0
for i in range(10):
    print()
    A.append(int(input(f"Numerito ({i+1}/10) pal vectorito A:")))
    print()
    B.append(int(input(f"Numerito ({i+1}/10) pal vectorito B:")))
for i in range(20):
    if i%2==0:
        C.insert(i, B[indexB])
        indexB += 1
    else:
        C.insert(i, A[indexA])
        indexA += 1
print()
print(A)
print(B)
print(C)



print("'Dame 2 vectores con 10 enteros y te creo otro con la resta de los 2' Descartes")
A=[]
B=[]
C=[]
for i in range(10):
    print()
    A.append(int(input(f"Numerito ({i+1}/10) pal vectorito A:")))
    print()
    B.append(int(input(f"Numerito ({i+1}/10) pal vectorito B:")))
    C.append(A[i]-B[i])
print()
print(A)
print(B)
print(C)



print("'te guardo 10 enteros entre [0,50] en un vector y te creo otro con lo impares' Descartes")
A=[]
B=[]
cuenta=0
numero=0
while cuenta<10:
    numero=int(input("Numerazo pal vectorazo ahí :"))
    if numero >=0 and numero <=50:
        A.append(numero)
        cuenta += 1
for i in A:
    if i%2!=0:
        B.append(i)
print(A)
print()
for i in range(0,len(A),2):
    print(f"A[{i}]: {A[i]}, A[{i+1}]: {A[i+1]}")
print()
print(B)
print()
for i in range(0,len(B),2):
    print(f"B[{i}]: {B[i]}, B[{i+1}]: {B[i+1]}")
    


print("'te guardo 50 numeros en un vector con la formula (i+5*i)%(i+1)' Descartes")
A=[]
for i in range(50):
    A.append((i+5*i)%(i+1))
print(A)



print("'Dame 10 numero, te los guardo en un vector y te digo cuales son los multiplos de un numero X' Descartes")
A=[]
num=0
for _ in range(10):
    A.append(float(input("Numerazo pal vectorazo: ")))
num=int(input("Ahora dime los multiplos de cual quieres encontrar en el vector: "))
for i in range(10):
    if A[i]%num==0:
        print(f"el {A[i]} es multiplo de {num}")



print("'Dame 10 numero, te los guardo en un vector y cambio por 0 los negativos' Descartes")
A=[]
for _ in range(10):
    A.append(float(input("Numerazo pal vectorazo: ")))
print(A)
for i in range(10):
    if A[i]<0:
        A[i]=0
print()
print(A)



print("'Dame 5 reales, te los guardo en un vector y si quieres te los muestro al derehco o al reves' Descartes")
A=[]
codigo=0
for _ in range(5):
    A.append(float(input("Numerazo pal vectorazo: ")))

codigo=int(input("1. al derecho / 2. al revés: "))
if codigo==1:
    print(A)
elif codigo==2:
    A.reverse()
    print(A)
else:
    print("Pibe, ese codigo no me vale")



print("'Dame 20 enteros, te los guardo en un vector y te elimino los repetidos' Descartes")
A=[]
B={}
for _ in range(20):
   A.append(int(input("Numerito pal vector ahí: ")))
print(A)
B=set(A)
print(f"el Vector sin repetidos seria {B}")



print("'Dame 15 notas de alumnos y te los guardo en un vector pa calcularte la media' Descartes")
A=[]
for i in range(15):
    nota=float(input(f"Notitas pal vector ahí({i+1}/15): "))
    A.append(nota)
print(f"La media de las notas es: {sum(A)} / {len(A)}=  {sum(A)/len(A)}")



print("'Dame 6 valores pares y te los guardo en un vector pa mostrastelos al reves' Descartes")
A=[]
contador=6
i=0
while i<contador:
    numero = int(input("Numerito pal vector ahi: "))
    if numero%2==0:
        A.append(numero)
        i+=1
print(A[::-1])
print()
A.reverse()
print(A)



print("'Dame 6 valores y te los guardo en un vector pa mostrastelos al reves' Descartes")
A=[]
for i in range(6):
    numero=int(input("Numerito pal vector ahi: "))
    A.append(numero)
print(A[::-1])
print()
A.reverse()
print(A)


print("'Dame 8 valores reales y te cojo dos valores cualquiera pa sumartelos' Descartes")
A=[]
for i in range(10):
    numero=int(input("Numerito pal vector ahi: "))
    A.append(numero)
print(A)
print(f"El mayor valor del vector es A[{A.index(max(A))}]={max(A)}")


print("'Dame 8 valores reales y te cojo dos valores cualquiera pa sumartelos' Descartes")
A=[]
for i in range(10):
    numero=int(input("Numerito pal vector ahi: "))
    A.append(numero)
print(f"El mayor valor del vector es {max(A)}")
print(f"El menor valor del vector es {min(A)}")


print("'Dame 8 valores reales y te cojo dos valores cualquiera pa sumartelos' Descartes")
A=[]
cuenta=0
for i in range(10):
    numero=int(input("Numerito pal vector ahi: "))
    A.append(numero)
for i in A:
    if i%2==0:
        print(i, end=' ')
        cuenta += 1
print(f"Dentro del vector hay {cuenta} numero/s par/es")



from random import randint
print("'Dame 8 valores reales y te cojo dos valores cualquiera pa sumartelos' Descartes")
A=[]
for i in range(8):
    numero=float(input("Numerito pal vector ahí: "))
    A.append(numero)
index1=randint(0,7)
index2=randint(0,7)
print(A)
print(f"al azar, por ejemplo A[{index1}]= {A[index1]} + A[{index2}]={A[index2]} es igual a {A[index1]+A[index2]}")



print("'Dame 10 valores reales y te guardo hago el cuadrado de esos 10 en otro vector' Descartes")
A=[]
for i in range(10):
    numero=int(input("Numerito pal vector ahí: "))
    A.append(numero)
B=A.copy()
for i in range(10):
    B[i]=pow(B[i],2)
print(A)
print(B)



print("'Dame 6 valores enteros y te los muestro en pantalla' Descartes")
A=[]
for i in range(6):
    numero=int(input("Numerito pal vector ahí: "))
    A.append(numero)
print(A)


print("'Dame un vector de 6 numeros y te los muestro' Descartes")
A=[1,0,5,-2,-5,7]
soma= A[0]+A[1]+A[5]
print(soma)
A[3]=100
print()
print(A)
print()
for i in A:
    print(i)
"""