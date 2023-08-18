"""
numeros=[1,2,3,4,5,6]

res={num:('par' if num %2==0 else 'impar') for num in numeros}

print(res)


print()
key='abcde'
valor=[1,2,3,4,5]

mezcla={key[i]:valor[i] for i in range(len(key))}
print(mezcla)

print()
print()
lista= [1,2,3,4,5]

cuadrado= {valor:valor**2 for valor in lista}
print(cuadrado)


diccionario= {'a': 1 ,'b': 2 ,'c': 3 ,'d': 4}
print(diccionario)

cuadrado= {key:valor**2 for key,valor in diccionario.items()}
print(cuadrado)"""