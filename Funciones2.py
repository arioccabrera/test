import math
import random
#print("'Dame dos strings y te creo una funcion que te intercala las dos strings caracter por caracter' Descartes")

#print("'Dame dos strings y te creo una funcion que te intercala las dos strings caracter por caracter' Descartes")
def intercala (*args):
    intercalada=''
    if len(args[0])>len(args[1]):
        for i in range(len(args[1])):
            intercalada += args[0][i]+args[1][i]
        intercalada += args[0][i+1:len(args[0])]
    else:
        for i in range(len(args[0])):
            intercalada += args[0][i]+args[1][i]
        intercalada += args[1][i+1:len(args[1])]
    return intercalada
#texto1=input("Dime la primera string: ")
#texto2=input("Dime la segunda string: ")
#print(f"{intercala(*[texto1, texto2])}")



""""

print("'Dame dos strings y te creo una funcion que te devuelve verdadero si las dos string son iguales' Descartes")
def igualitas(*args):
    if args[0]==args[1]:
        return True
    return False
texto1=input("Dime la string pa ver si es iguar que la otra: ")
texto2=input("Dime la string pa ver si es iguar que la otra: ")
if igualitas(*[texto1, texto2]):
    print("Igualitas, dos gota diagua")
else:
    print("No se parecen en nada")



print("'Dame una string y te creo una funcion que te devuelve verdadero si la string es un anagrama' Descartes")
def anagrama(arg):
    if arg== arg[::-1]:
        return True
texto=input("Dime la string pa ver si es iguar ar derehco y ar reves: ")
if anagrama(texto):
    print("Verdadero")
else:
    print("Eso no es, mijo")



import random
print("'Dame dos matrices de orden N y te creo una funcion que te recibe esas dos y te devuelve otra matriz con su producto matricial' Descartes")
fila=[]
fila2=[]
matriz1=[]
matriz2=[]
matriz12=[]
def producto_matricial(*args):
    matriz3=[]
    lista=[]
    lista2=[]
    suma=0
    for i in range (orden):
        for k in range(orden):
            for j in range(orden):
                print(f"+ [{i}][{j}]*[{j}][{k}] + ")
                print(f"i={i}")
                print(f"j={j}")
                print(f"k={k}")
                print()
                print(f"args[0][{i}][{j}]= {args[0][i][j]}")
                print(f"args[1][{j}][{k}]= {args[1][j][k]}")
                print()
                suma += args[0][i][j]*args[1][j][k]
                print(f"Suma={suma}")
            lista.append(suma)
            suma=0
            lista2=lista.copy()
        matriz3.append(lista2)
        lista.clear()
    return matriz3
orden=int(input("Querias las matrices de que orden mi ninio? "))
for i in range(orden):
    for j in range(orden):
        fila.append(random.randint(1,20))
    fila2=fila.copy()
    matriz1.append(fila2)
    fila.clear()
print()
print("Matriz 1")
for i in matriz1:
    print(i)
for i in range(orden):
    for j in range(orden):
        fila.append(random.randint(1,20))
    fila2=fila.copy()
    matriz2.append(fila2)
    fila.clear()
print()
print("Matriz 2")
for i in matriz2:
    print(i)
matriz12=[matriz1,matriz2]
print()
print("El producto matricial de las dos matrices es:")
for i in producto_matricial(*matriz12):
    print(i)



import random
matriz=[]
fila=[]
fila2=[]
print("'Dame una matrix de orden N y te creo una funcion que te devuelve su traspuesta' Descartes")
def matriz_traspuesta(*args):
    copia=0
    for i in range(orden):
        for j in range(orden):
            if j>i:
                copia=args[i][j]
                args[i][j]=args[j][i]
                args[j][i]=copia
    print()
    return args
orden=int(input("Querias la matriz de que orden mi ninio? "))
for i in range(orden):
    for j in range(orden):
        fila.append(random.randint(1,20))
    print(fila)
    fila2=fila.copy()
    matriz.append(fila2)
    fila.clear()
print()
for i in matriz:
    print(i)
print("La matriz traspuesta es:")
for i in matriz_traspuesta(*matriz):
    print(i)



import random
matriz=[]
print("'Dame una matrix 3x3 y te creo una funcion que te suma los valores que estan en la diagonal secundaria' Descartes")
def matriz_secundaria(*args):
    suma=0
    for i in range(3):
        for j in range(3):
            if j==i:
                print( args[i][j] , end=' ')
                suma += args[i][j]
    print()
    return suma
for i in range(3):
    matriz.append([random.randint(1,20),random.randint(1,20),random.randint(1,20)])
for i in matriz:
    print(i)
print("matriz invertida")
matriz.reverse()
for i in matriz:
    print(i)
print(f"La suma de los valores de la diagonal secundaria es igual a: {matriz_secundaria(*matriz)}")



import random
matriz=[]
print("'Dame una matrix 3x3 y te creo una funcion que te suma los valores por encima de la diagonal principal' Descartes")
def matriz_mayores(*args):
    suma=0
    for i in range(3):
        for j in range(3):
            if j>i:
                print( args[i][j] , end=' ')
                suma += args[i][j]
    print()
    return suma
for i in range(3):
    matriz.append([random.randint(1,20),random.randint(1,20),random.randint(1,20)])
for i in matriz:
    print(i)
print(f"La suma de los valores por encima de la diagonal principal es igual a: {matriz_mayores(*matriz)}")



import random
matriz=[]
print("'Dame una matrix 4x4 y te creo una funcion que te devuelve los valores mayores a 10' Descartes")
def matriz_mayores(*args):
    mayores=[]
    for i in range(4):
        for j in range(4):
            if args[i][j]>10:
                mayores.append(args[i][j])
    return mayores
for i in range(4):
    matriz.append([random.randint(1,20),random.randint(1,20),random.randint(1,20),random.randint(1,20)])
print(matriz)
print(f"Los valores mayores a 10 de la matriz son: {matriz_mayores(*matriz)}")



import math
vector=[]
print("'Dame un vector de enteros con N numeros y te creo una funcion que te devuelve la desviacion tipica del vector' Descartes")
def desvio_vector(*args):
    desvio=0
    sumatorio=0
    media=sum(args)/len(args)
    print(f"{sum(args)}/{len(args)} = media({media})")
    print()
    print()
    for i in range(len(args)):
        print(f" ({args[i]} - {media})^2 = {pow((args[i] - media), 2)}")
        sumatorio += pow((args[i]-media),2)
    print(sumatorio)
    print()
    desvio = math.sqrt(sumatorio/len(args))
    print(desvio)
    return desvio
for i in range(10):
    vector.append(float(input(f"Valor {i+1}/10: ")))
print(f"La desviacion tipica del vector {vector} es: {desvio_vector(*vector)}")



import random
vector=[]
num=0
print("'Dame un vector de enteros y te creo una funcion que te devuelve el vector lleno de numeros aleatorios sin repeticion' Descartes")
def vector_random(*args):
    for i in range(10):
        num=random.randint(1,100)
        if num in vector:
            print("repetido")
        else:
            vector.append(num)
    return vector
print(f"Dentro el vector están los siguientes numeros sin repeticion: {vector_random(*vector)}")



vector=[]
print("'Dame un vector de enteros y te creo una funcion que te devuelve los valores pares del vector' Descartes")
def pares_vector(*args):
    contador=0
    for i in args:
        if i%2==0:
            contador += 1
    return contador
for i in range(10):
    vector.append(int(input("Entero pal vector: ")))
print(f"Dentro del vector: {vector} hay {pares_vector(*vector)} numeros pares")



import math
print("'Dame un numero N entero y positivo y te creo una funcion que te devuelve el factorial exponencial de N' Descartes")
def factorial_exponencial(num):
    exfacto=0
    for i in range(1,num,1):
        exfacto=math.pow(i, exfacto)
        print(exfacto)
    return math.pow(num, exfacto)
num=int(input("Numerito pal fartorial exponeciar ahí: "))
print(f"El Factorial exponencial de {num} es igual a : {factorial_exponencial(num)}")



import math
print("'Dame un numero N entero y positivo y te creo una funcion que te devuelve el Hyperfactorial de N' Descartes")
def hyper_factorial(num):
    hyfactorial = 1
    for i in range(1,num+1,1):
        hyfactorial *= math.pow(i,i)
        print(f"{i}^{i}")
    return hyfactorial
num=int(input("Numerito pal hiper fatorial ahi: "))
print(f"El hiperfactorial de {num} es igual a: {hyper_factorial(num)} ")



import math
print("'Dame un numero N y te creo una funcion que te devuelve el superfactorial de N' Descartes")
def super_factorial(num):
    factorial=1
    for i in range(1,num+1,1):
        factorial *= math.factorial(i)
        print(i)
    return factorial
num=int(input("Numerito pa decirte el super fatorial ahi: "))
print(f"El superfactorial de {num} es igual a: {super_factorial(num)} ")



print("'Dame un numero N y te creo una funcion que te devuelve el factorial doble de sus numero impares' Descartes")
def suma_factorial_doble(num):
    factorial=1
    for i in range(1,num+1,1):
        if i%2!=0:
            factorial *= i
            print(i)
    return factorial
num=int(input("Numerito pa decirte el fatorial doble ahi: "))
print(f"El factorial doble de {num} es igual a: {suma_factorial_doble(num)} ")



import math
print("'Dame un numero N y te creo una funcion que te devuelve la suma de los digitos de N factorial' Descartes")
def suma_factorial(num):
    factorial=math.factorial(num)
    factorial= str(factorial)
    vector_factorial=[]
    for i in range(len(factorial)):
        vector_factorial.append(int(factorial[i]))
        print(f"{factorial[i]}")
    return math.factorial(num),sum(vector_factorial)
num=int(input("Numerito pa sumarte el fatorial ahi: "))
factorial, suma= suma_factorial(num)
print(f"El factorial de {num} es igual a: {factorial} y la suma de los digitos de su factorial es: {suma}")


print("'Dame un numero numerador y un denominador de una fraccion y te creo una funcion que te devuelve la fraccion simplificada por el mayor factor posible' Descartes")
def simplifica(numerador, denominador):
    num_simpli=0
    den_simpli=0
    factor=0
    mayor=max(numerador,denominador)
    for i in range(1,mayor+1,1):
        if numerador%i==0 and denominador%i==0:
            num_simpli=numerador/i
            den_simpli=denominador/i
            factor=i
    return num_simpli, den_simpli, factor
num=int(input("Numerado pa simplificarte la vida ahí: "))
den=int(input("Denominado pa simplificarte la vida ahí: "))
num2, den2, factor2= simplifica(num,den)
print(f"{num}/{den} simplificado al maximo, el dividirlo por {factor2} es igual a: {num2}/{den2}")



import math
print("'Dame un numero N y te creo una funcion que te devuelve la suma de los 'N' terminos de una serie para calcular el logaritmo neperiano' Descartes")
def serie_neperiano(n):
    suma=0
    for i in range(n+1):
        print(f" + 1/{i}!", end='')
        suma += 1/math.factorial(i)
    print()
    return suma
n=int(input("Numero de termino para sumar: "))
print()
print(f"El valor de la suma es igual a: {serie_neperiano(n)}")



import math
print("'Dame un angulo en grados y te creo una funcion que te devuelve el valor del seno de ese angulo usando la serie de Taylor de 0 a 5' Descartes")
def serie_taylor(x):
    suma=0
    for i in range(5):
        print(f"+ ({(-1 )** i}/{(2*i)+1}! X^{(2*i+1)})", end=' ')
        print()
        suma += ((-1)**i/(math.factorial((2*i)+1)))*x**(2*i+1)
    return suma
grados=float(input("Dime los graditos pa calcularte er seno ahí: "))
print()
print(f"Sen {grados} = {serie_taylor(math.radians(grados)):.2f}")
print()



print("'Dame un numero entero positivo 'N' y te creo una funcion que te devuelve el resultado de la serie (N^2+1)/(N+3)' Descartes")
def calculo_serie(n):
    valores=[]
    total=0
    for i in range(n+1):
        if i==0:
            valores.append(0)
        else:
            valores.append(((i**2)+1)/(i+3))
            total += valores[i]
    valores.append(total)
    return valores
numero=int(input("Numero 'N' de la serie: "))
for i in range(len(calculo_serie(numero))-1):
    print(end=' + ')
    print(f"{calculo_serie(numero)[i]:.2f}", end='')
print(f" = {calculo_serie(numero)[len(calculo_serie(numero))-1]:.2f}")



print("'Dame un numero entero positivo 'N' y te creo una funcion que te devuelve un triangulo de lado n y base 2*N-1' Descartes")
def triangulo_base(n):
    linea=[]
    for i in range(n):
        if i == 0:
            linea.append('*')
        elif i>0:
            linea.append(linea[i - 1] + '*')
            if len(linea[i])%2==0:
                linea[i]=linea[i]+ '*'
    return linea
alto=int(input("Cuanto es la altura del triangulo? "))
resultado=triangulo_base(alto)
for i in resultado:
    print(i)



print("'Dame un numero entero positivo 'N' y te creo una funcion que te devuelve un triangulo lateral de altura 2*N-1 y 'N' de largo' Descartes")
def triangulo_lateral(n):
    linea=[]
    for i in range(2*n-1):
        if i == 0:
            linea.append('*')
        elif i>0:
            if i>=n:
                linea.append(linea[i-1][0:(len(linea[i-1])-1)])
            else:
                linea.append(linea[i-1] + '*')
    return linea
alto=int(input("Cuanto es la altura del triangulo? "))
resultado=triangulo_lateral(alto)
for i in resultado:
    print(i)



print("'Dame un numero entero positivo 'N' y te creo una funcion que te devuelve 'N' lineas primos anteriores a ese numero' Descartes")
def lineas_exclamacion(n):
    linea=[]
    for i in range(n):
        if i == 0:
            linea.append('!')
        else:
            linea.append(linea[i-1]+'!')
    return linea
lineas=int(input("Cuantas lines quieres que te imprima con el '!'? "))
resultado=lineas_exclamacion(lineas)
for i in resultado:
    print(i)



print("'Dame un numero entero positivo y te creo una funcion que te devuelve los primos anteriores a ese numero' Descartes")
def devuelve_primos(n):
    primos=[]
    if n>2:
        for i in range(1,n):
            no_primo = 0
            for j in range(2,i):
                if i%j==0:
                    no_primo=1
            if no_primo==0:
                primos.append(i)
    else:
        return primos.append(n)
    return primos
numero= int(input("Quieres ver los primos anteriores al numero...? "))
print(devuelve_primos(numero))



print("'Dame un numero entero positivo y te creo una funcion que te devuelve su factorial' Descartes")
def factorial(n):
    total=1
    for i in range(n,1,-1):
        print(i, end=' ')
        total *= i
    return total
numero=int(input("Nupero pa saber el factorial: "))
print(f"El factorial de {numero} es: {factorial(numero)}")




print("'Dame dos numero enteros positivos y te creo una funcion que te devuelve la suma de los numeros existentes entre ellos' Descartes")
def suma_numeros(*args):
    suma=0
    for i in range(args[0]+1,args[1],1):
        print(i, end=' ')
        suma += i
    return suma
limites=[]
for i in range(2):
    limites.append(int(input(f"limite numero {i+1}/2: ")))
print(f"la suma de los numeros entre {limites[0]} y {limites[1]} es igual a: {suma_numeros(*limites)}  ")




print("'Dame numero que indique una cantidad y te creo una funcion que imprime '=' tantas veces como el numero indicado' Descartes")
def dibuja_linea(cantidad):
    linea= ''
    for i in range(cantidad):
        linea += "="
    return linea
cantidad=int(input("Cuantos '=' quieres que te muestre mijo?? "))
print()
print("Aqui tienes tu linea: ")
print(dibuja_linea(cantidad))




print("'Dame tres valores(>0) para cada lado de un triangulo y te creo dos funciones para saber si el triangulo existe y otra para el tipo de triangulo' Descartes")
def triangulo_existe(*args):
    if (args[0]< args[1]+args[2]) and (args[1]< args[0]+args[2]) and (args[2]< args[1]+args[0]):
        return 1
    return 0
def tipo_triangulo(*args):

    #:param args:
    #:return: 1= equilatero, 2= isosceles, 3=escaleno
    
    if args[0]== args[1]==args[2]:
        return 1
    elif args[0]== args[1] or args[0]==args[2] or args[1]==args[2]:
        return 2
    return 3
lados_triangulo=[]
for i in range(3):
    lados_triangulo.append(float(input(f"medida para el lado {i+1}/3: ")))
    while lados_triangulo[i]<0:
        print("la medida no puede ser menor que '0', boobo")
        lados_triangulo[i]=(float(input(f"medida para el lado {i + 1}/3: ")))
if triangulo_existe(*lados_triangulo):
    print("el triangulito existe")
    if tipo_triangulo(*lados_triangulo)==1:
        print("El triangulo es equilatero")
    elif tipo_triangulo(*lados_triangulo)==2:
        print("El triangulo es isosceles")
    elif tipo_triangulo(*lados_triangulo)==3:
        print("El triangulo es escaleno")
else:
    print("el triangulito no existe")




print("'Dame lo Km recorridos y los litros consumidos y te creo una funcion que te devuelve los km/l' Descartes")
def km_litro(*args):
    return args[0]/args[1]
km=int(input("Dime loh Km recorridos: "))
litros=int(input("Dime loh litro que se mama er coye: "))
if km_litro(km,litros) < 8:
    print(f"{km_litro(km,litros)}km/l ?? Ese coche bebe gasolina como un diablo")
elif km_litro(km,litros) >= 8 and km_litro(km,litros) < 12:
    print(f"{km_litro(km,litros)}km/l ?? Bueno no esta mal")
elif km_litro(km,litros) >= 12:
    print(f"{km_litro(km, litros)}km/l ?? Un mecherito")



print("'Dame un numero entero mayor que 0 y te creo una funcion que te devuelve la suma de todas sus cifras' Descartes")
def suma_cifras(numero):
    numero=str(numero)
    suma=0
    for i in range(len(numero)):
        suma += int(numero[i])
    return suma
numero=int(input("Numerito mayor que cero ahí: "))
print(f"la suma de cada cifra del numero {numero} es igual a: {suma_cifras(numero)}")



print("'Dame 3 notas de un alumno y una letra 'A' o 'P' y te creo una funcion que te devuelve media aritmetica(A) o ponderada(P)' Descartes")
def media_notas(media,*args):
    if 'a' in media or 'A' in media:
        return sum(args)/len(args)
    elif 'p' in media or 'P' in media:
        return (args[0]*5+args[1]*3+args[2]*5)/(5+3+2)
    return 0
notas=[]
for i in range(3):
    notas.append(int(input(f"Nota {i+1}/3: ")))
media=input("introduzca 'A' para media arirmetica o 'P' para ponderada: ")
print(f" Las notas {notas} con una media tipo '{media}' da una media de: {media_notas(media,*notas)}")



print("'Dame dos numeros y te creo una funcion que te devuelve el mayor de los dos' Descartes")
def mayor(a,b):
    if a > b:
        return a
    return b
num1= float(input("Numero 1: "))
num2= float(input("Numero 2: "))
print(f"{mayor(num1, num2)} es el numero mayor")



import math
print("'Dame radio y altura y te creo una funcion que te devuelve el volumen de un cilindro' Descartes")
def vol_cilindro(radio, altura):
    return math.pi*(radio**2)*altura
radio= float(input("Radio: "))
altura= float(input("Altura: "))
print(f"Un cilindro de base {radio} y altura {altura} tiene un volumen de {vol_cilindro(radio,altura):.2f}")



import math
print("'Dame dos catetos 'a' y 'b' y te creo una funcion que te devuelve el valor de la hipotenusa' Descartes")
def hipotenusa(cateto1, cateto2):
    return math.sqrt((pow(cateto1,2))+(pow(cateto2,2)))
cateto1= float(input("Cateto 1: "))
cateto2= float(input("Cateto 2: "))
print(f"raiz cuadrada de ({cateto1}^2 + {cateto2}^2) es igual a la hipotenusa {hipotenusa(cateto1,cateto2):.2f}")



import math
print("'Dame dos catetos 'a' y 'b' y te creo una funcion que te devuelve el valor de la hipotenusa' Descartes")
def hipotenusa(cateto1, cateto2):
    return math.sqrt((pow(cateto1,2))+(pow(cateto2,2)))
cateto1= float(input("Cateto 1: "))
cateto2= float(input("Cateto 2: "))
print(f"raiz cuadrada de ({cateto1}^2 + {cateto2}^2) es igual a la hipotenusa {hipotenusa(cateto1,cateto2):.2f}")



print("'Dame una tempratura en ºC y te creo una funcion que te la devuelve convertida en F' Descartes")
def celsius_to_fahrenheit(temp):
    return temp*(9.0/5.0)+32.0
celsius=float(input("Temperatura en celsius: "))
print(f"{celsius}ºC = {celsius_to_fahrenheit(celsius)} F")



print("'Dame 3 enteros que indiquen horas minutos y segundosy te creo una funcion que te devuelve el total de segundos' Descartes")
def total_segundos(horas,minutos,segundos):
    return horas*3600+minutos*60+segundos
minuto=60
segundo=60
hora=int(input("Numero de horas: "))
while minuto>59:
    minuto=int(input("Numero de minutos(<=59): "))
while segundo>59:
    segundo=int(input("Numero de segundos (<=59): "))
print()
print(f"{hora}:{minuto}:{segundo} Hacen un total de: {total_segundos(hora,minuto,segundo)} segundos")



import math
print("'Dime el radio de una esfera y te creo una funcion que te devuelve el volumen de esa esfera' Descartes")
def vol_esf(radio):
    return 4/3*math.pi*pow(radio,3)
radio= float(input("Radio de la esferita: "))
print(f"El volumen de la esfera es: {vol_esf(radio):.2f}")



import math
print("'Dime un numero y te creo una funcion que te devuelve si ese numero es un cuadrado perfecto o no' Descartes")
def cuadrado_perfect(numero):
    if math.sqrt(numero).is_integer():
        return 1
    return 0
numero = int(input("Que numero quieres adivinar? "))
print()
if cuadrado_perfect(numero):
    print("Tu numero viene de un cuadrado perfecto")
else:
    print("Hmmm me parece que te dieron gato por cuadrado perfecto, vete pa que te lo cambien")




print("'Dime un numero y te creo una funcion que te devuelve si es positivo, negativo o cero' Descartes")
def verifica(a):
    if a >0:
        return 1
    elif a<0:
        return -1
    return 0
num= int(input("Dime un numero para ver si es '+', '-' o '0'"))
print()
if verifica(num)==1:
    print("Ay! tu numero es positivo, sigue así")
elif verifica(num)==-1:
    print("Tu numero es negativo, no seas como el")
else:
    print("Tu numero es un cero, como mis ganas de ser pobre Hoistes")




print("'Dime una fecha en formato dd/mm/aaa, y te la muestro como texto' Descartes")
def fecha_texto(fecha):
    
    :param fecha: es la fecha es una string en formato dd/mm/aaaa
    en X guardo una lista con cada elemento separado por '/' de la string y despues paso el mes a int para ver que numero del mes es
    :return: devuelve la fecha con el mes en palabras 

    X= fecha.split('/')
    if int(X[1]) == 1:
        return f" Día {X[0]} de enero de {X[2]}"
    elif int(X[1]) == 2:
        return f" Día {X[0] } de febrero de {X[2]}"
    elif int(X[1]) == 3:
        return f" Día {X[0] } de marzo de {X[2]}"
    elif int(X[1]) == 4:
        return f" Día {X[0] } de abril de {X[2]}"
    elif int(X[1]) == 5:
        return f" Día {X[0] } de mayo de {X[2]}"
    elif int(X[1]) == 6:
        return f" Día {X[0]} de junio de {X[2]}"
    elif int(X[1]) == 7:
        return f" Día {X[0]} de julio de {X[2]}"
    elif int(X[1]) == 8:
        return f" Día {X[0]} de agosto de {X[2]}"
    elif int(X[1]) == 9:
        return f" Día {X[0]} de septiembre de {X[2]}"
    elif int(X[1]) == 10:
        return f" Día {X[0]} de octubre de {X[2]}"
    elif int(X[1]) == 11:
        return f" Día {X[0]} de noviembre de {X[2]}"
    elif int(X[1]) == 12:
        return f" Día {X[0]} de diciembre de {X[2]}"
    return f" Argo no me cuadra en esa fecha a mi"
fecha= input("Dime fecha (asi: dd/mm/aaaa): ")
print(fecha_texto(fecha))



print("'Dime un numero, te calculo el doble en una funcion y te lo devuelvo' Descartes")
def doble(a):
    return a*2
num= int(input("Un numero ahí: "))
print(doble(num))"""