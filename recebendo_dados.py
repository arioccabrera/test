print("'Dime tu salario y tiempo en la empresa y te digo cuanto te van a subir' Descartes")

salario=float(input("Salario: "))
anos=int(input("Años trabajados: "))




"""
print("'Dime tu salario y tiempo en la empresa y te digo cuanto te van a subir' Descartes")
salario=float(input("Salario: "))
anos=int(input("Años trabajados: "))
if salario<=500:
    salario=salario+salario*0.25
    print("25%")
elif salario>500 and salario<=1_000:
    salario = salario + salario * 0.2
    print("20%")
elif salario>1000 and salario<=1500:
    salario = salario + salario * 0.15
    print("15%")
elif salario>1500 and salario<=2000:
    salario = salario + salario * 0.1
    print("10%")
else:
    print("Tu ya ganas mucho pa estar aumentandote nada")
if anos<1:
    print("Tu acabas de llegar y ya estas pidiendo bonus??")
    print(f"Vas a cobrar {salario}€ y agracede")
elif anos>=1 and anos<=3:
    print(f"Vas a cobrar {salario+100}€ y agracede")
elif anos>3 and anos<=6:
    print(f"Vas a cobrar {salario+200}€ y agracede")
elif anos > 6 and anos <= 10:
    print(f"Vas a cobrar {salario+300}€ y agracede")
else:
    print(f"Vas a cobrar {salario+500}€ y agracede")



print("'Dime cuando llegaste y cuando te fuiste del parking y te digo cuanto te van a clavar' Descartes")
print("Horas y minutos de entrada")
horallegada=int(input("horas de entrada: "))
minutollegada=int(input("minutos de entrada: "))
print("Horas y minutos de salida")
horasalida=int(input("Horas de salida: "))
minutosalida=int(input("Minutos de salida: "))
if horallegada>horasalida:
    horastotales=(24-horallegada)+(horasalida)
    print(f"Llegó un dia y salio al dia siguiente: horastotales= {horastotales}")
elif horallegada==horasalida:
    horastotales=24
else:
    horastotales = horasalida - horallegada
    print(f"Llegó dia y salio en el mismo día: horastotales= {horastotales}")
if minutollegada<minutosalida:
    minutostotales = minutosalida - minutollegada
    print(f"minutollegada < minutosalida  minutostotales= {minutostotales}")
else:
    minutostotales= (60 -minutollegada) + minutosalida
    print(f"minutollegada > minutosalida  minutostotales= {minutostotales}")
if minutostotales!=0:
    horastotales+=1
if horastotales >=1 and horastotales<=2:
    print(f" Horas totales: {horastotales} x 1€/h= {horastotales*1}")
if horastotales>2 and horastotales<=4:
    print(f" Horas totales: {horastotales} x 1.4€/h= {float(horastotales) * 1.4}")
if horastotales>4:
    print(f" Horas totales: {horastotales} x 2€/h= {float(horastotales) * 2}")


print("'Dime el valor de la venta y te digo la comision que te llevas' Descartes")
venta=float(input("Valor vendido: "))
if venta>=100_000:
    print(f"1. una venta de {venta}€ da una comision de {700+venta*.16}")
elif venta>=80_000 and venta<100_000:
    print(f"2. una venta de {venta}€ da una comision de {650 + venta * .14}")
elif venta>=60_000 and venta<80_000:
    print(f"3. una venta de {venta}€ da una comision de {600 + venta * .14}")
elif venta>=40_000 and venta<60_000:
    print(f"4. una venta de {venta}€ da una comision de {550 + venta * .14}")
elif venta>=20_000 and venta<60_000:
    print(f"5. una venta de {venta}€ da una comision de {500 + venta * .14}")
else:
    print(f"6. una venta de {venta}€ da una comision de {400 + venta * .14}")
    

print("'Dime una fecha y te digo si es veridica' Descartes")
dia=int(input("Dia: "))
mes=int(input("Mes: "))
ano=int(input("Año(AAAA): "))
verdadD=False
verdadM=False
verdadA=True
if (dia>=1 and dia<=31):
    verdadD=True
    print(f"1.Dia= {verdadD}")
else:
    verdadD = False
    print(f"1.Dia= {verdadD}")
if (dia==31) and (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
    verdadM=True
    print(f"2.Mes= {verdadM}")
elif (dia<=30 and mes!=2) or (dia<=28 and mes==2):
    verdadM = True
    print(f"2.Mes= {verdadM}")
else:
    verdadM = False
    print(f"2.Mes= {verdadM}")
if dia==29 and mes==2:
    if (ano%400==0) or (ano%4==0 and ano%100!=0):
        verdadA=True
        verdadM=True
        print(f"3.Año bisiesto {verdadA}, Mes= {verdadM}")
    else:
        verdadA = False
        print(f"3.Año bisiesto {verdadA}, Mes= {verdadM}")
print(f"3.Año= {verdadA}")
if verdadD and verdadM and verdadA:
    print(f"El {dia}/{mes}/{ano} es una fecha veridica, que quieres un premio?")
else:
    print(f"El {dia}/{mes}/{ano} NO es una fecha veridica, alguien esta mientiendote")


print("'Dime el precio de un producto y te digo lo que va a aumentar de precio y lo caro que es' Descartes")
precio=float(input("Precio antiguo ahí: "))
if precio<50 and precio>0:
    print(f"Un producto de {precio}$ va a sufir un aumento del 5%")
    precio= precio + precio*.05
    print(f"Valor final: {precio}")
elif precio>=50 and precio<=100:
    print(f"Un producto de {precio}$ va a sufir un aumento del 10%")
    precio = precio + precio * .1
    print(f"Valor final: {precio}")
else:
    print(f"Un producto de {precio}$ va a sufir un aumento del 15%")
    precio = precio + precio * .15
    print(f"Valor final: {precio}")
if precio<80:
    print(f"{precio}? Pues pa haberle subido el precio esta baratisimo")
elif precio>=80 and precio<=120:
    print(f"{precio}? aah esta bien coño")
elif precio>=120 and precio<=200:
    print(f"{precio}? chias, un poquito caro, no?")
else:
    print(f"{precio}?? Tamos locos o que? eso yo me meto en interné y lo consigo mas barato")


print("'Dime peso y altura de una persona y te la clasifico' Descartes")
peso=float(input("peso ahí: "))
altura=float(input("altura ahí: "))
if peso<60:
    if altura<1.20:
        print("Categoria A")
    if altura>=1.20 and altura<=1.70:
        print("Categoria B")
    else:
        print("Categoria C")
elif peso>=60 and peso<=90:
    if altura<1.20:
        print("Categoria D")
    if altura>=1.20 and altura<=1.70:
        print("Categoria E")
    else:
        print("Categoria F")
else:
    if altura<1.20:
        print("Categoria G")
    if altura>=1.20 and altura<=1.70:
        print("Categoria H")
    else:
        print("Categoria I")


print("'Dime 3 numero y te los muestro en orden creciente' Descartes")
numero1=int(input("primer numero: "))
numero2=int(input("segundo numero: "))
numero3=int(input("tercer numero: "))
if numero1<numero2 and numero1<numero3:
    menor= numero1
elif numero2<numero1 and numero2<numero3:
    menor= numero2
else:
    menor= numero3
if (numero1>numero2 or numero1>numero3) and (numero1<numero3 or numero1<numero2):
    medio = numero1
elif (numero2>numero1 or numero2>numero3) and (numero2<numero3 or numero2<numero1):
    medio = numero2
else:
    medio = numero3
if numero1>numero2 and numero1>numero3:
    mayor= numero1
elif numero2>numero1 and numero2>numero3:
    mayor= numero2
else:
    mayor= numero3
print(f"los numeros ordenados son: {menor}, {medio}, {mayor}")


from random import randint
print("'Dime cuantos es la suma de dos numero aleatorios entre 1 y 100 y te digo si esta bien ' Descartes")
acierto=0
numero1 = randint(1,100)
numero2 = randint(1,100)
respuesta=int(input(f"cuanto es {numero1} + {numero2}?: "))
if numero1+ numero2==respuesta:
    acierto += 1
    print("correcto :)")
numero1 = randint(1,100)
numero2 = randint(1,100)
respuesta=int(input(f"cuanto es {numero1} + {numero2}?: "))
if numero1+ numero2==respuesta:
    acierto += 1
    print("correcto :)")
numero1 = randint(1,100)
numero2 = randint(1,100)
respuesta=int(input(f"cuanto es {numero1} + {numero2}?: "))
if numero1+ numero2==respuesta:
    acierto += 1
    print("correcto :)")
numero1 = randint(1,100)
numero2 = randint(1,100)
respuesta=int(input(f"cuanto es {numero1} + {numero2}?: "))
if numero1+ numero2==respuesta:
    acierto += 1
    print("correcto :)")
numero1 = randint(1,100)
numero2 = randint(1,100)
respuesta=int(input(f"cuanto es {numero1} + {numero2}?: "))
if numero1+ numero2==respuesta:
    acierto += 1
    print("correcto :)")
print(f"acertaste un total de: {acierto}, queee maquina \U0000263A ")


import math
print("'Dime una ecuacion de segundo grado y te la calculo ' Descartes")
print("ax^2 + bx + c = 0")
a=float(input("Dime cuanto vale 'a': "))
b=float(input("Dime cuanto vale 'b': "))
c=float(input("Dime cuanto vale 'c': "))
if a==0:
    print("Mentiroso, eso no es una ecuacion de segundo grado")
if (pow(b,2)-4*a*c)<0 and a!=0:
    print("No existe valor real")
if (pow(b,2)-4*a*c)==0 and a!=0:
    print(f"existe un unico resultado: {(-b)/(2*a)}")
if (pow(b,2)-4*a*c)>0 and a!=0:
    print(f"{pow(b,2)}")
    print(f"existen dos resultados:")
    print(f"-b + \U0000221A b^2-4ac: %.2f"%((-b + math.sqrt((pow(b, 2) - 4 * a * c))) / (2 * a)))
    print(f"-b - \U0000221A b^2-4ac: %.2f"%((-b - math.sqrt((pow(b, 2) - 4 * a * c))) / (2 * a)))


print("'Dime el precio del producto y el estado y te digo cuanto cuesta ' Descartes")
producto=float(input("Precio del producto: "))
estado=input("Codigo del estado(MG/SP/RJ/MS): ")
if estado=="MG":
    print(f"{producto}€ + impestos en MG: {producto+producto*.07}€  ")
elif estado == "SP":
    print(f"{producto}€ + impestos en SP: {producto + producto * .12}€  ")
elif estado == "RJ":
    print(f"{producto}€ + impestos en RJ: {producto + producto * .15}€  ")
elif estado == "MS":
    print(f"{producto}€ + impestos en MS: {producto + producto * .08}  ")
else:
    print("Codigo del estado erroneo")
    

print("'Dime un año y te digo si es bisiesto' Descartes")
ano=int(input("Añito ahí: "))
if ano%400==0 or (ano%4==0 and ano%100!=0 ):
    print(f"{ano} es bisiesto")
else:
    print(f"{ano} no es bisiesto ")


print("'Dime tu edad y años trabajados y te digo si te puedes jubilar' Descartes")
anos=int(input("Años de vida ahí: "))
trabajo=int(input("Años trabajados ahí: "))
if anos >= 65 or trabajo >= 30 or (anos >= 60 and trabajo >= 25):
    print("Es veridico, se puede jubilar pa morirse como quien dice")
else:
    print("Tiene que seguir trabajando pal diablo")


print("'Dime los 3 lados de un triangulo y te digo si son validos y el tipo de triangulo' Descartes")
lado1=float(input("Lado 1 ahí: "))
lado2=float(input("Lado 2 ahí: "))
lado3=float(input("Lado 3 ahí: "))
if (lado1 < lado2+lado3) and (lado2 < lado1+lado3) and (lado3 < lado1+lado2):
    if lado1==lado2==lado3:
        print("Eso es un triangulazo equilatero")
    elif lado1!=lado2!=lado3:
        print("Eso es un triangulazo escaleno")
    else:
        print("Eso es un triangulazo isosceles")
else:
    print("Error, un lado del triangulo no puede ser mayor o igual a la suma de los otros dos lados")


numero=int(input("Dime un numero entero entre 1000 y 9999 y te lo separo en 4 lineas: "))
numero= str(numero)
print(numero[0])
print(numero[1])
print(numero[2])
print(numero[3])
print(f"{numero.split()}")

numero=int(input("Dime un numero entero entre 100 y 999 y te lo viro: "))
numero= str(numero)
print("el numero virado es:",numero[::-1])

letra=input("Dime una letra mayuscula y te la muestro en minuscula: ")
print("la esta en minuscula es: %s"%letra.lower())

degrau=float(input("Altura del degrau: "))
altura=float(input("Altura escada: "))
print(f"Para subir una altura de {altura}m con una escalera de {degrau}cm por peldaño, vas a necesitar como minimo %.2f peldaños"%(degrau/altura))

base=float(input("salario base del currante: "))
print("este mes, con dietas del 5 por ciento y descuentos del 7 por ciento, el trabajador va a cobrar %.2f"%(base+(base*.05)-(base*.07)))

dias=int(input("Cuando dias trabajó el colega? "))
print(f"Aqui el amigo va cobrar 30€ por dia de trabajo -el 8 por ciento de impuesto, que seria= %.2f"%((dias*30)-(dias*30*.08)))

print("el primer ganador se lleva pa casita: %.f"%(780_000-(780_000*0.46)))
print("el segundo ganador se lleva pa casita: %.f"%(780_000-(780_000*0.32)))
print("el tercer ganador se lleva pa casita: %.f"%(780_000-(780_000*0.22)))

producto=float(input("precio del producto: "))
print(f"Precio {producto} con un descuento del 12 por ciento=  %.2f"%(producto-(producto*12/100)))

altura=float(input("Altura del cilindro: "))
radio=float(input("Radio del cilindro: "))
print(f"el volumen del cilindro de altura {altura} y radio {radio} es: %.2f"%(math.pi*pow(radio,2)*altura))

cateto1=float(input("Primer cateto: "))
cateto2=float(input("Segundo cateto: "))
print(f"la hipotenusa de los catetos {cateto1} y {cateto2} es: %.2f"%(math.sqrt(pow(cateto1,2)+pow(cateto2,2))) )

import math
'''\U0001F534 circulo'''
radio=float(input("dime radio de un \U0001F534 y te digo su área: "))
print(f"El área de un \U0001F534 de radio {radio} es: %.2f"%(math.pi*pow(radio,2)))

''' \U0001F7E6 son los caracteres ascii para el emoji dle cuadrado'''
cuadrado=float(input("ladito de un cuadrado ahí: "))
print(f"El área de un \U0001F7E6 de lado {cuadrado} es: %.2f"%pow(cuadrado,2))

numero=int(input("Numerito entero ahí: "))
print(f"si tu dijiste el {numero}, tonces el anterior es %d y el siguiente es %d, es o no es?"%(numero-1,numero+1))
numero=int(input("Numerito entero ahí: "))
print(f"si tu dijiste el {numero}, tonces el doble del anterior es %d y el tripe de {numero} mas el siguiente es %d, es o no es?"%(2*(numero-1),numero*3+numero+1))


euro= float(input("Cuantos € quieres cambiar a $? "))
dollar= float(input("a cuanto esta el € en $ mi niño? "))
print(f"Entonces si 1€ son {dollar}$, {euro}€ son %.2f$"%(euro*dollar))

import statistics '''para poder usar la funcion mean()'''
num1=float(input("numero 1: "))
num2=float(input("numero 2: "))
num3=float(input("numero 3: "))
num4=float(input("numero 4: "))
print(f"la media aritmetica de los 4 numeros es: %.2f"%(statistics.mean([num1,num2,num3,num4])))

import math '''contiene el numero PI'''
angulo=float(input("Te convierto Grados en radianes: "))
print(f"{angulo}º son %.2f radianes"%(angulo*math.pi/180))
angulo=float(input("Te convierto radianes en grados: "))
print(f"{angulo} radianes son %.2fº"%(angulo*180/math.pi))

distancia=float(input("dime unas millas y te tigo cuantos km son: "))
print(f"{distancia} milla(s) son %.2f km"%(distancia*1.61))
distancia=float(input("dime unos kilometritos y te tigo cuantas millitas son: "))
print(f"{distancia} Km son %.2f millas"%(distancia/1.61))

velocidad=float(input("dime unos km/h y te tigo cuantos m/s son: "))
print(f"{velocidad} k/m son %.2f m/s"%(velocidad/3.6))
velocidad=float(input("dime unos m/s y te tigo cuantos Km/h son: "))
print(f"{velocidad} m/s son %.2f Km/h"%(velocidad*3.6))

celsius= float(input("Dime unos graditos en ºC y te digo cuantos Kelvin son: "))
print(f" {celsius} ºC pasados a K son: %.2f"%(celsius+273.15))
temp = float(input("dime una temperatura en K y te digo cuantos ºC son: "))
print(f" {temp} K son  %.2f ºC"%(temp-276.15))
temp = float(input("dime una temperatura en F y te digo cuantos ºC son: "))
print(f" {temp} F son  %.2f ºC"%(5*(temp-32)/9))
temp = float(input("dime una temperatura en ºC y te digo cuantos Farenheit son: "))
print(f" {temp} ºC son  %.2f F"%(temp*(9.0/5.0)+32))

numero1 = float(input("dime un numero real y te calculo su quinta parte al toque: "))
print("La quinta parte de tu numerito es: %.3f, de locos eh?"%(numero1/5))
numero1 = float(input("dime un numero real y te calculo el cuadrado al toque: "))
print("El cuadrado de tu numerito es: %.3f, de locos eh?"%pow(numero1,2))

numero1 = int(input("dime un numero entero 1 "))
numero2 = int(input("dime un numero entero 2 "))
numero3 = int(input("dime un numero entero 3 "))
suma= numero1+numero2+numero3
print(f"La suma de esos 3 numeritos es: {suma}, qué te parece?")

nome = float(input("dime un numero real"))
print("Tu número es el  %.2f, lo adiviné?"%nome)
nome = int(input("dime un numero entero"))
print(f"Tu número es el  {nome}, lo adiviné?")

print("bienvenido  %s" %nome)
print(f"cuantos años tienes {nome}" )
edad = input(f"cuantos años tienes {nome}")
print(f"{edad} estas envejecido {nome}" )
"""