from collections import namedtuple

tupla =(1,2,3)
print(tupla[0])

cachorro= namedtuple('cachorro', 'edad raza nombre')
cachorro= namedtuple('cachorro', 'edad, raza, nombre')
cachorro= namedtuple('cachorro', ['edad', 'raza', 'nombre'])


perrito= cachorro(5, 'caniche', 'sultan')
print(perrito)

print(perrito[0])
print(perrito[1])
print(perrito[2])

print()
print(perrito.edad)
print(perrito.raza)
print(perrito.nombre)
