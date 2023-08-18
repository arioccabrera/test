

""""
print("'te convierto los numeros a letras' Descartes ")
numero1=110
numero2=0
for n in range(1,numero1+1):
    print(f"vuelta numero:{n}")
    numero1=str(n)
    print(f"tamaño de la string: {int(len(numero1))}")
    for i in range(0, len(numero1)):
        print(numero1[i], end='')
    if int(len(numero1)) == 1:
        if int(numero1[0])==1:
            print(" uno", end='')
        if int(numero1[0])==2:
            print(" dos", end='')
        if int(numero1[0])==3:
            print(" tres", end='')
        if int(numero1[0])==4:
            print(" cuatro", end='')
        if int(numero1[0])==5:
            print(" cinco", end='')
        if int(numero1[0])==6:
            print(" seis", end='')
        if int(numero1[0])==7:
            print(" siete", end='')
        if int(numero1[0])==8:
            print(" ocho", end='')
        if int(numero1[0])==9:
            print(" nueve", end='')
    if int(len(numero1))==2 and int(numero1[0])==1:
        if int(numero1[1]) == 0:
            print(" diez", end='')
        if int(numero1[1]) == 1:
            print(" once", end='')
        if int(numero1[1]) == 2:
            print(" doce", end='')
        if int(numero1[1]) == 3:
            print(" trece", end='')
        if int(numero1[1]) == 4:
            print(" catorce", end='')
        if int(numero1[1]) == 5:
            print(" quince", end='')
        if int(numero1[1]) == 6:
            print(" dieciseis", end='')
        if int(numero1[1]) == 7:
            print(" diecisiete", end='')
        if int(numero1[1]) == 8:
            print(" dieciocho", end='')
        if int(numero1[1]) == 9:
            print(" diecinueve", end='')
    if int(len(numero1))==2 and int(numero1[0])==2:
        if int(numero1[1]) == 0:
            print(" veinte", end='')
        if int(numero1[1])==1:
            print(" veintiuno", end='')
        if int(numero1[1])==2:
            print(" veintidos", end='')
        if int(numero1[1])==3:
            print(" veintitres", end='')
        if int(numero1[1])==4:
            print(" veinticuatro", end='')
        if int(numero1[1])==5:
            print(" veinticinco", end='')
        if int(numero1[1])==6:
            print(" veintiseis", end='')
        if int(numero1[1])==7:
            print(" veintisiete", end='')
        if int(numero1[1])==8:
            print(" veintiocho", end='')
        if int(numero1[1])==9:
            print(" veintinueve", end='')
    if int(len(numero1))==2 and int(numero1[0])==3:
        print(" treinta", end='')
        if int(numero1[1])==1:
            print(" y uno", end='')
        if int(numero1[1])==2:
            print(" y dos", end='')
        if int(numero1[1])==3:
            print(" y tres", end='')
        if int(numero1[1])==4:
            print(" y cuatro", end='')
        if int(numero1[1])==5:
            print(" y cinco", end='')
        if int(numero1[1])==6:
            print(" y seis", end='')
        if int(numero1[1])==7:
            print(" y siete", end='')
        if int(numero1[1])==8:
            print(" y ocho", end='')
        if int(numero1[1])==9:
            print(" y nueve", end='')
    if int(len(numero1))==2 and int(numero1[0])==4:
        print(" cuarenta", end='')
        if int(numero1[1])==1:
            print(" y uno", end='')
        if int(numero1[1])==2:
            print(" y dos", end='')
        if int(numero1[1])==3:
            print(" y tres", end='')
        if int(numero1[1])==4:
            print(" y cuatro", end='')
        if int(numero1[1])==5:
            print(" y cinco", end='')
        if int(numero1[1])==6:
            print(" y seis", end='')
        if int(numero1[1])==7:
            print(" y siete", end='')
        if int(numero1[1])==8:
            print(" y ocho", end='')
        if int(numero1[1])==9:
            print(" y nueve", end='')
    if int(len(numero1))==2 and int(numero1[0])==5:
        print(" cincuenta", end='')
        if int(numero1[1])==1:
            print(" y uno", end='')
        if int(numero1[1])==2:
            print(" y dos", end='')
        if int(numero1[1])==3:
            print(" y tres", end='')
        if int(numero1[1])==4:
            print(" y cuatro", end='')
        if int(numero1[1])==5:
            print(" y cinco", end='')
        if int(numero1[1])==6:
            print(" y seis", end='')
        if int(numero1[1])==7:
            print(" y siete", end='')
        if int(numero1[1])==8:
            print(" y ocho", end='')
        if int(numero1[1])==9:
            print(" y nueve", end='')
    if int(len(numero1))==2 and int(numero1[0])==6:
        print(" sesenta", end='')
        if int(numero1[1])==1:
            print(" y uno", end='')
        if int(numero1[1])==2:
            print(" y dos", end='')
        if int(numero1[1])==3:
            print(" y tres", end='')
        if int(numero1[1])==4:
            print(" y cuatro", end='')
        if int(numero1[1])==5:
            print(" y cinco", end='')
        if int(numero1[1])==6:
            print(" y seis", end='')
        if int(numero1[1])==7:
            print(" y siete", end='')
        if int(numero1[1])==8:
            print(" y ocho", end='')
        if int(numero1[1])==9:
            print(" y nueve", end='')
    if int(len(numero1))==2 and int(numero1[0])==7:
        print(" setenta", end='')
        if int(numero1[1])==1:
            print(" y uno", end='')
        if int(numero1[1])==2:
            print(" y dos", end='')
        if int(numero1[1])==3:
            print(" y tres", end='')
        if int(numero1[1])==4:
            print(" y cuatro", end='')
        if int(numero1[1])==5:
            print(" y cinco", end='')
        if int(numero1[1])==6:
            print(" y seis", end='')
        if int(numero1[1])==7:
            print(" y siete", end='')
        if int(numero1[1])==8:
            print(" y ocho", end='')
        if int(numero1[1])==9:
            print(" y nueve", end='')
    if int(len(numero1))==2 and int(numero1[0])==8:
        print(" ochenta", end='')
        if int(numero1[1])==1:
            print(" y uno", end='')
        if int(numero1[1])==2:
            print(" y dos", end='')
        if int(numero1[1])==3:
            print(" y tres", end='')
        if int(numero1[1])==4:
            print(" y cuatro", end='')
        if int(numero1[1])==5:
            print(" y cinco", end='')
        if int(numero1[1])==6:
            print(" y seis", end='')
        if int(numero1[1])==7:
            print(" y siete", end='')
        if int(numero1[1])==8:
            print(" y ocho", end='')
        if int(numero1[1])==9:
            print(" y nueve", end='')
    if int(len(numero1))==2 and int(numero1[0])==9:
        print(" noventa", end='')
        if int(numero1[1])==1:
            print(" y uno", end='')
        if int(numero1[1])==2:
            print(" y dos", end='')
        if int(numero1[1])==3:
            print(" y tres", end='')
        if int(numero1[1])==4:
            print(" y cuatro", end='')
        if int(numero1[1])==5:
            print(" y cinco", end='')
        if int(numero1[1])==6:
            print(" y seis", end='')
        if int(numero1[1])==7:
            print(" y siete", end='')
        if int(numero1[1])==8:
            print(" y ocho", end='')
        if int(numero1[1])==9:
            print(" y nueve", end='')
    if int(len(numero1)) == 3 and int(numero1[0]) == 1:
        if int(numero1[0]) == 1 and int(numero1[1]) == 0 and int(numero1[2]) == 0:
            print(" cien", end='')
        if int(numero1[0]) == 1 and int(numero1[1]) == 0 and int(numero1[2]) == 1:
            print(" ciento uno", end='')
        if int(numero1[0]) == 1 and int(numero1[1]) == 0 and int(numero1[2]) == 2:
            print(" ciento dos", end='')
        if int(numero1[0]) == 1 and int(numero1[1]) == 0 and int(numero1[2]) == 3:
            print(" ciento tres", end='')
        if int(numero1[0]) == 1 and int(numero1[1]) == 0 and int(numero1[2]) == 4:
            print(" ciento cuatro", end='')
        if int(numero1[0]) == 1 and int(numero1[1]) == 0 and int(numero1[2]) == 5:
            print(" ciento cinco", end='')
        if int(numero1[0]) == 1 and int(numero1[1]) == 0 and int(numero1[2]) == 6:
            print(" ciento seis", end='')
        if int(numero1[0]) == 1 and int(numero1[1]) == 0 and int(numero1[2]) == 7:
            print(" ciento siete", end='')
        if int(numero1[0]) == 1 and int(numero1[1]) == 0 and int(numero1[2]) == 8:
            print(" ciento ocho", end='')
        if int(numero1[0]) == 1 and int(numero1[1]) == 0 and int(numero1[2]) == 9:
            print(" ciento  nueve", end='')
    print()




print("'Te digo el mayor palindromo que se pueden hacer multiplicando dos numeros de 3 digitos' Descartes ")
numero1=0
numero2=0
palindromo=0
mayor=-999
for i in range(100, 1000):
    for j in range(100, 1000):
        palindromo= i * j
        palindromo=str(palindromo)
        if(palindromo==palindromo[::-1]):
            palindromo= int(palindromo)
            if palindromo > mayor:
                mayor= palindromo
                numero1 = i
                numero2 = j
print(f"El mayor palindromo que se puede conseguir es {mayor} al multiplicar {numero1} x {numero2}")


print("'Dime el intervalo de los  numeros primos que quieres sumar' Descartes ")
numero1=int(input("Numeros primos desde(inicio): "))
numero2=int(input("hasta (fin): "))
primo= False
contador=numero1
suma=0
while contador<=numero2:
    if contador==1 or contador==2:
        print(f" + {contador} ", end='')
        suma += contador
    else:
        for i in  range(2, contador):
            if contador%i==0:
                primo= False
                break
            elif contador%i!=0:
                primo=True
        if primo or contador==2 or contador==1:
            print(f" + {contador}", end='')
            suma += contador
    contador +=1
print(f" = {suma} ")



print("'Dime cuantos numeros primos quieres sumar' Descartes ")
numero=int(input("Numero: "))
primo= False
contador=1
cuenta=0
suma=0
while cuenta<numero:
    if contador==1 or contador==2:
        print(f" + {contador} ", end='')
        suma += contador
        cuenta += 1
    else:
        for i in  range(2, contador):
            if contador%i==0:
                primo= False
                break
            elif contador%i!=0:
                primo=True
        if primo or contador==2 or contador==1:
            print(f" + {contador}", end='')
            suma += contador
            cuenta += 1
    contador +=1
print(f" = {suma} ")



print("'Dime un numero y te digo si es primo' Descartes ")
numero=int(input("Numero: "))
primo= False
for i in  range(2, numero):
    print(i)
    if numero%i==0:
        primo= False
        break
    elif numero%i!=0:
        primo=True
if primo or numero==2 or numero==1:
    print(f" El {numero} SI es primo")
else:
    print(f" El {numero} NO es primo")



print("'Dime un numero y te hago el triangulo de Floyd' Descartes ")
numero=int(input("Tamaño del triangulo: "))
numero2=1
for i in range(1,numero+1):
    for num in range(1,i+1):
        print(numero2, end=' ')
        numero2 +=1
    print()


print("'Dime cuanto sacas del banco y te digo cuantos billetes son' Descartes ")
notas100=0
notas50=0
notas20=0
notas10=0
notas5=0
notas2=0
notas1=0
dinero=int(input("Cuanto vas a sacar? "))
if dinero>=100:
    notas100 = int(dinero/100)
    dinero=dinero%100
if dinero>=50 and dinero<100:
    notas50 = int(dinero/50)
    dinero=dinero%50
if dinero>=20 and dinero<50:
    notas20 = int(dinero/20)
    dinero=dinero%20
if dinero>=10 and dinero<20:
    notas10 = int(dinero/10)
    dinero=dinero%10
if dinero>=5 and dinero<10:
    notas5 = int(dinero/5)
    dinero=dinero%5
if dinero>=2 and dinero<5:
    notas2 = int(dinero/2)
    dinero=dinero%2
if dinero>=1 and dinero<2:
    notas1 = int(dinero/1)
    dinero=dinero%1
print(f"Sus perras:")
if notas100!=0:
    print(f"{notas100} de 100€")
if notas50 != 0:
    print(f"{notas50} de 50€")
if notas20 != 0:
    print(f"{notas20} de 20€")
if notas10 != 0:
    print(f"{notas10} de 10€")
if notas5 != 0:
    print(f"{notas5} de 5€")
if notas2 != 0:
    print(f"{notas2} de 2€")
if notas1 != 0:
    print(f"{notas1} de 1€")
print(f"total: {notas1*1+notas2*2+notas5*5+notas10*10+notas20*20+notas50*50+notas100*100} €€€")



from datetime import datetime
print("'Dime cuanto aumentan el sueldo del trabajador y te digo cuanto cobra a dia de hoy' Descartes ")
funcionario=float(input("cuanto cobra carlos? "))
aumento= 0.015
ano=1996
while ano<int(datetime.today().strftime('%Y')):
    print(f"en {ano} esta cobrando {funcionario}€ y te van a subir un {aumento*100}%,", end=' ')
    funcionario += (funcionario*aumento)
    print(f" por lo que vas a cobrar: {funcionario:.2f} €")
    ano += 1
    aumento=aumento*2
print(f"actualmente, en {ano} estas cobrando: {funcionario:.2f}, te quejaras, no?")


print("'Dime cuanto cobran dos trabajadores y te digo cuanto tiempo tardan en ahorrar lo mismo' Descartes ")
carlos=float(input("cuanto cobra carlos? "))
joao=carlos/3
mes=0
while joao<carlos:
    print(f"mes: {mes}")
    print(f"carlos: {carlos}")
    print(f"joao: {joao}")
    carlos= carlos + (carlos*0.02)
    joao= joao + (joao*0.05)
    mes += 1
print()
print(f"tienen que pasar {mes} meses ({mes/12:.2f} años)para que joao tenga mas dinero que carlos")


print("'Te sumo los pares de la sucesion de Fibonacci hasta llegar a los 4 millones' Descartes ")
contador=0
a=0
b=1
c=0
suma=0
print(a, end=' ')
print(b, end=' ')
print()
while suma<=4000000:
    print(f"vuelta:{contador}, valor suma:{suma}")
    c= a + b
    if c%2==0 :
        print("c",c, end=' ')
        suma=suma+c
    a= b + c
    if a%2==0 :
        print("  a:",a, end='')
        suma=suma+a
    b= a + c
    if b % 2 == 0 :
        print("b", b, end=' ')
        suma = suma + b
    print()
    contador+=1


print("'Dime numero positivo y te muestro la sucesion Fibonacci hasta ese numero' Descartes ")
a=0
b=1
c=0
numero=int(input("Hasta donde quieres el fibonacci, mijo? :"))
continua=True
print(a, end=' ')
print(b, end=' ')
while continua:
    #print(f"cont:{contador}", end='')
    c= a + b
    print(c, end=' ')
    if a>= numero or b>= numero or c>= numero:
        continua= False
        break
    a= b + c
    print(a, end=' ')
    if a >= numero or b >= numero or c >= numero:
        continua= False
        break
    b= a + c
    print(b, end=' ')
    if a >= numero or b >= numero or c >= numero:
        continua= False
        break


print("'Dime R1 y R2 y te digo su valor en paralelo' Descartes ")
R1=1
R2=1
while R1!=0 or R2!=0:
    print()
    print("para salir mete un cerito(0) en una cualquiera ")
    R1=int(input("Valor R1: "))
    if R1==0:
        break
    R2=int(input("Valor R2: "))
    if R2==0:
        break
    R=(R1*R2)/(R1+R2)
    print(f"R1={R1}\U00002126 en paralelo con R2={R2}\U00002126 da una resistencia total de: {R:.2f} \U00002126")


print("'Dime dos catetos de un triangulo y te digo la hipotenusa' Descartes ")
cateto1=int(input("Primer cateto: "))
cateto2=int(input("Segundo cateto: "))
print(f"{cateto1}\U000000B2 + {cateto2}\U000000B2 = {cateto1**2+cateto2**2}")


print("'Dame un numero entre 1000 y 9999 y te digo si cumplen la propiedad de suma de sus dos digitos izquierdos y derechos al cuadrado es igual al numeor original ' Descartes ")
numero=int(input("numero entre 1000 y 9999 ahí: "))
numero=str(numero)
numero1= numero[0]+numero[1]
numero1=int(numero1)
numero2= numero[2]+numero[3]
numero2=int(numero2)
suma= numero1+numero2
cuadrado= suma**2
numero=int(numero)
if numero==cuadrado:
    print(f"{numero} cumple la propiedad, {numero1} +  {numero2} = {suma} y {suma}\U000000B2 = {cuadrado}. Perfeee")
else:
    print(f"{numero} no cumple la propiedad de que la suma de los dos digitos de más baja orden con los dos de mayor orden al cuadrado es igual al numero original, lo entendiste? yo tampoco")



print("'Te digo la suma de los cuadrados de los 100 primeros numeros naturales' Descartes ")
suma=0
for num in range(1,101):
    print(f"{num}\U000000B2 + ", end='')
    suma += pow(num,2)
print(f"= {suma}")
print(f"{suma}\U000000B2 - {suma}= {pow(suma,2)-suma}")


print("'Te digo el menor numero divisible entre los numero del 1 al 10")
continua = True
numero=1
bandera= 0
while continua:
    #print(f"numero:{numero}")
    for i in range(1,11):
        if numero%i==0:
            #print(f"2.{i} es divisor de {numero}")
            bandera+=1
        else:
            bandera=0
            #print(f"3.NO {i} es divisor de {numero}")
    if bandera==10:
        print(f"El {numero} es divisible entre los numeros del 1 al 20")
        continua=False
    #print(f"3.{numero}")
    numero+=1



print("'Te digo los N primeros numeros naturales multiplos de i y j' Descartes")
n=int(input("N primeros numero? "))
i=int(input("multiplo de: "))
j=int(input("y multiplo de: "))
contador=1
pares=0
while pares<n:
    if contador%i==0 or contador%j==0:
        print(contador, end=' ')
        pares += 1
    contador += 1


from random import randint
print("'Dame dos dados y te digo que jugada fue mayor, menor o igual' Descartes")
tirar=int(input("cuantas tiradas quieres: "))
for _ in range(tirar):
    dado1 = randint(1,6)
    print(f"1. {dado1}")
    dado2 = randint(1, 6)
    print(f"2. {dado2}")
    if dado1==dado2:
        print("empate")
    if dado1> dado2:
        print("gana el dado1")
    if dado1< dado2:
        print("gana el dado2")
    print()

print("'Valor de S' Descartes")
suma=0
i=0
print("S= ", end='')
for num in range(1,100):
    if num%2!=0:
        i+=1
        suma += (num/i)
        print(f"+ {num}/{i}!", end='')
print(f"= {suma}")



import math
print("'Dime N y te calculo la suma de la formula' Descartes")
numero=int(input("Numero: "))
suma=0
print("S= 0 ", end='')
for num in range(1,numero+1):
    suma += (num/math.factorial(num*2))
    print(f"+ {num}/{num*2}!", end='')
print(f"= {suma}")


import math
print("'Dime N y te calculo la suma de la formula' Descartes")
numero=int(input("Numero ahí: "))
suma=1
print("E= 1 ", end='')
for num in range(1,numero+1):
    print(f"+ 1/{num}! ", end='')
    suma += (1/(math.factorial(num)))
print(f" = {suma}")


print("'Dime N y te calculo la suma de la serie harmonica' Descartes")
numero=int(input("Numero entero positivo ahí: "))
suma=0
print(f"H({numero})=", end=' ')
for num in range(1,numero+1):
    print(f"+ 1/{num} ", end='')
    suma +=(1/num)
print(f"= {suma}")


print("'Dame un numero y te digo cual es el primer multipo de 11, 13 o 17 que viene despues de ese' Descartes")
numero=int(input("numero ahi: "))
i=numero
ok= True
while ok:
    if i%11==0:
        print(f"Despues del {numero} el {i} es el primer multiplo de 11 que te encuentras, flipa")
        break
    elif i%13==0:
        print(f"Despues del {numero} el {i} es el primer multiplo de 13 que te encuentras, flipa")
        break
    elif i%15==0:
        print(f"Despues del {numero} el {i} es el primer multiplo de 15 que te encuentras, flipa")
        break
    i += 1


print("'Te sumo los numeros multiplos de 3 o 5 hasta 1_000' Descartes")
sum=0
for num in range(1,1000):
    if num%3==0 or num%5==0:
        sum += num
print(f"la suma total es: {sum}")


print("'Dame un entero positivo y te digo sus divisores' Descartes")
numero=int(input("Numero ahí: "))
i=1
suma=0
while i<numero:
    if numero%i==0:
        print(f"{i} es divisor de {numero}")
        suma +=i
    i += 1
print(f"Suma de los divisores: {suma}")


print("'Dame notas y te digo la media' Descartes")
i=0
suma=0
nota=float(input("Notita ahí: "))
while nota>=10 and nota<=20:
    suma += nota
    print(f"1.S {suma}")
    i += 1
    print(f"2.i {i}")
    nota=float(input("Notita ahí: "))
print()
print("Salimoooo")
print(f"la nota media es: {suma/i}")


print("'Dame un intervalo y te sumos los pares y multiplico los impares' Descartes")
inicio=int(input("inicio del intervalo: "))
fin=int(input("fin del intervalo: "))
suma=0
multi=1
i=inicio
while i<=fin:
    if i%2==0:
        suma  += i
    else:
        multi *= i
    i+=1
print(f"La suma de los pares da: {suma}")
print(f"La multiplicacion de los impares da: {multi}")


print("'Dame numeros y te digo cuantos metiste y los pares' Descartes")
numero=0
contador=0
pares=0
while numero!=1000:
    numero = int(input("Numerito ahí (el 1000 acaba todo): "))
    if numero%2==0:
        pares+=1
    contador+=1
print(f"metiste un total de {contador} de los cuales {pares} son pares")
print("salimoooo")


print("'Dame un numero entre 100 y 999 y te lo separo en 3 numeros' Descartes")
numero=int(input("Numerito entre 100 y 999 ahí: "))
numero=str(numero)
i=0
while i<3:
    print(numero[i])
    i+=1


print("'Dame un bucle y de los N numeros cual es el mayor y cuantas veces se repite' Descartes")
numero=int(input("Cuantos numeros naturales quieres meter? "))
contador=0
mayor=-9999
while contador<numero:
    numero2=int(input("Numerito ahí: "))
    if numero2> mayor:
        mayor= numero2
        repe = 1
    elif numero2==mayor:
        repe+=1
    contador += 1
print(f" el mayor numero es {mayor}", end=' ')
if repe>1:
    print(f"y esta repetido {repe} veces")
else:
    print(f"pero no parece que este repe")
print(f"Salimooo")


print("'Dame un bucle y te digo la suma de los N numeros natural en order ascendente' Descartes")
numero=int(input("Cuantos numeros naturales quiere? "))
contador=0
suma=0
while contador<=numero:
    contador += 1
    suma+=contador
    print(f"+ {contador}", end='')
print(f"= {suma}")
print(f"Salimooo")


print("'Dame un bucle y te digo la suma de los 50 primeros pares' Descartes")
suma=0
par=0
contador=1
while par<50:
    if contador%2==0:
        print(f"{contador} + ", end='')
        par += 1
        suma += contador
    contador+=1
print()
print(f"Salimooo, la suma de los {par} primeros numeros pares es: {suma} ")


print("'Dame 1 numero N y te digo los N primeros impares' Descartes")
numero=int(input("Cuantos impares quieres mijo? "))
impar=0
contador=1
while impar<numero:
    if contador%2!=0:
        print(contador)
        impar+=1
    contador+=1
print("Salimooo")



print("'Dame 10 numero, un bucle for y te digo el mayor y el menor' Descartes")
numero=0
mayor=0
menor=99999999
for i in range(1,11):
    numero=int(input("Numerito pa sumar ahí: "))
    if numero>mayor:
        mayor=numero
        print(f"mayol{mayor}")
    elif numero<menor:
        menor=numero
        print(f"menol: {menor}")
print(f"El mas chico es: {menor} y el mayor es suso, que tiene ya {mayor}")
print("FIN!(el humano)")


print("'Dame 10 numero, un bucle for y te hago la media' Descartes")
numero=0
sumita=0
contador=0
for i in range(1,11):
    numero=int(input("Numerito pa sumar ahí: "))
    if numero>0:
        sumita+=numero
        contador+=1
print(contador)
print(f"la sumita es: {sumita} y la media es: {sumita/contador}")
print("FIN!(el humano)")


print("'Dame 10 numero, un bucle for y te lo sumo' Descartes")
numero=0
sumita=0
for _ in range(10):
    numero=int(input("Numerito pa sumar ahí: "))
    sumita+=numero
print(f"la sumita es: {sumita}")
print("FIN!(el humano)")


print("'Dame un bucle while y sumo de 1_000 en 1_000 hasta 100_000' Descartes")
numero2=0
while numero2<=100_000:
    print(numero2)
    numero2+=1000
print("FIN!(el humano)")


print("'Dame un bucle while y te hago una cuenta atras de 10 a 0' Descartes")
numero2=10
while numero2>=0:
    print(numero2)
    numero2-=1
print("FIN!(el humano)")


print("'Dame un bucle while y te digo los numeros del 1 al 100 3 veces' Descartes")
numero2=0
while numero2<3:
    print("while 3")
    numero = 1
    while numero<101:
        print("while 101 ", end='')
        print(numero, end=' ')
        numero+= 1
    print()
    numero2+=1
    

print("'Dame un bucle For y te digo los numeros del 1 al 100 3 veces' Descartes")
for _ in range(3):
    print()
    for numero in range(1,101):
        print(numero, end=', ')

print("'Dame un bucle For y te digo los 5 primeros multiplos de 3' Descartes")
contador=0
for numero in range(1,20):
    if numero%3==0:
        print(numero)
        contador+= 1
        print(f"conta: {contador}")
    if contador==5:
        break
print("salimoooo")
"""