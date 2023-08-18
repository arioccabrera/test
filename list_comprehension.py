import random

tablero=[[int(input("numero ahi: ")) for numero in range(3)] for valor in range(3)]
print(tablero)



"""
numeros=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(numeros)):
    for j in range(len(numeros)):
        print(numeros[i][j])

print("otro ejemplo")
[[print(j) for j in i] for i in numeros ]



numeros=[1,2,3,4]
aumenta= [elemento*10 for elemento in numeros]
print(aumenta)


numeros=[1,2,3,4,5,6,7,8,9,10]


#cualquier numero par modulo de 2 es =0 y '0' en Python es False, por tanto: not False= True
pares= [digito for digito in numeros if not digito % 2]


#cualquier numero impar modulo de 2 es =1 y '1' en Python es True, por tanto: 1= True
impares= [digito for digito in numeros if digito % 2]


print(pares)
print(impares)


calculos=[numero*2 if numero %2==0 else numero/2 for numero in numeros]
print(calculos)


letras= 'Texo de pruebas'
print([caracter.upper() for caracter in letras ])


nombres= ['arioc', 'pepe', 'caslo', 'juan']
print([palabra.upper() for palabra in nombres])


print([numeros *3 for numeros in range(1,11)])

print([bool(valor) for valor in [0, [], '', 1,3.8, True]])

print([int(num) for num in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] ])

print([letra for letra in "Arioc"])


numeros=[1,2,3,4,5,6]
numeros_dobles=[]
numeros_dobles2=[]
for i in numeros:
    numeros_dobles.append(i*2)
print(numeros_dobles)

print(f"{[j * 2 for j in numeros]}")



numeros=[1,2,3,4]
aumenta= [elemento*10 for elemento in numeros]
print(aumenta)

numeros=[1,2,3,4]
divide= [elemento/2 for elemento in numeros]
print(divide)

def cuadrado(elemento):
    return elemento * elemento
numeros=[1,2,3,4]
eleva= [cuadrado(enteros) for enteros in numeros]
print(eleva)
"""