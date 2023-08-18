lista1=(1,2,3,10)
lista2=[4,5,6,7]
lista3={'a':1,'b':2,'c':3,'d':4}

zip1= zip(lista1,lista2, lista3.values())

print(zip1)
print(type(zip1))

print(list(zip1))
zip1= zip(lista1,lista2, lista3.values())
print(tuple(zip1))
zip1= zip(lista1,lista2, lista3.values())
print(set(zip1))
zip1= zip(lista1,lista2)
print(dict(zip1))

datos=[(0,1),(1,2),(2,3),(3,4),(4,5)]
print(list(zip(*datos)))


print()
print()
examen1=[8,9,7]
examen2=[5,7,8]
alumno=['jonay','pepe','maikol']

final={notas[0]:max(notas[1],notas[2]) for notas in zip(alumno,examen2,examen1)}
print(final)
