lista1=[1,34,5,653,23,6]
lista2=['g','e','e','k',' ', 'u','n','i','v','e','r','s','i','t','y']
lista3= list(range(11))
lista4= list('Geek University')

print(lista1)
print(lista2)
print(lista3)
print(lista4)

print()
if 8 in lista3:
    print("El 8 esta en la lista3")
else:
    print("El 8 NO esta en la lista3")

if 'U' in lista4:
    print("Hay una 'U' en la lista4")
else:
    print("No hay 'U' en la lista4")

print()
lista1=[1,34,5,653,23,6]
print(lista1)
lista1.sort()
print(lista1)

print()
lista1=[1,3,4,5,65,3,23,6]
lista4= list('Geek University')
print(lista1.count(3))
print(lista4.count('e'))
print(type(lista1.count('e')))

print()
lista1=[1,3,4,5,65,3,23,6]
print(lista1)
lista1.append(999)
print(lista1)
lista1.append([1,2,3])
print(lista1)

if [1 ,2 ,  3] in lista1:
    print("lista encontrada")
else:
    print("lista NO encontrada")

print()
lista1=[1,3,4,5,65,3,23,6]
print(lista1)
lista1.extend([1,2,3])
print(lista1)


print()
lista1=[1,3,4,5,65,3,23,6]
print(lista1)
lista1.extend(['G','e','e','k'])
print(lista1)
lista1.extend(['Geek'])
print(lista1)
lista1.extend(['5'])
print(lista1)
print(type(lista1[10]))

print()
lista1=[1,34,5,653,23,6]
print(lista1)
lista1.insert(3, 'valor nuevo')
print(lista1)


print()
lista1=[1,34,5,653,23,6]
lista2=['g','e','e','k',' ', 'u','n','i','v','e','r','s','i','t','y']
lista3= list(range(11))
lista4= list('Geek University')

print(lista1)
print(lista2)
lista5= lista1 + lista2
print(lista5)
print()
lista1.extend(lista2)
print(lista1)

print()
lista1=[1,34,5,653,23,6]
lista2=['g','e','e','k',' ', 'u','n','i','v','e','r','s','i','t','y']

print(lista1)
print(lista2)
lista1.reverse()
print(lista1)
lista2.reverse()
print(lista2)

print()
lista1=[1,34,5,653,23,6]
lista2=['g','e','e','k',' ', 'u','n','i','v','e','r','s','i','t','y']

print(lista1[::-1])
lista1.reverse()
print(lista1)
lista2.reverse()
print(lista2)


print()
lista1=[1,34,5,653,23,6]
lista2=['g','e','e','k',' ', 'u','n','i','v','e','r','s','i','t','y']
print()
lista6= lista2.copy()
print(lista6)


print()
lista1=[1,34,5,653,23,6]
print(len(lista1))
nombre='arioc'
print(len(nombre))

print()
print()

lista1=[1,34,5,653,23,6]
print(lista1)
lista1.clear()
print(lista1)


print()
nombre= 'Arioc,Silvera,Cabrera'
print(nombre)
nombre= nombre.split(',')
print(nombre)

print()
lista1=[1,34,5,653,23,6]
print(lista1[1:])

print(lista1[:2])
print(lista1[:4])
print(lista1[::-1])
print(lista1[::2])

print()
print()
lista1=[1,34,5,653,23,6]
print(max(lista1))
print(min(lista1))
print(sum(lista1))
print(len(lista1))

print()
print()
lista1=[1,34,5,653,23,6]
print(lista1)
tupla= tuple(lista1)
print(tupla)

print()
print()
lista1=[1,5,653]
lista2=lista1

print(lista1)
print(lista2)

lista1.append(54)
print(lista1)
print(lista2)


