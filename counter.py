from collections import Counter

lista=[1,1,2,44,5,6,8,9,8,8,8,9,9,4,4,44,3,3,3,7,7,7,7]

res= Counter(lista)
print(type(res))
print(res)

print()
print(Counter('Arioc Silvera Cabrera'))

print()
texto= "Wells Cathedral is an Anglican cathedral in Wells, Somerset, commenced around 1175 on the site of a late-Roman " \
       "mausoleum and an 8th-century abbey church. The cathedral has been described by the historian John Harvey as " \
       "Europe's first truly Gothic structure, lacking the Romanesque work that survives in many other cathedrals. It " \
       "is the seat of the bishop of Bath and Wells. This photograph depicts the interior of Wells Cathedral's chapter " \
       "house, built by unknown architects between 1275 and 1310 in the Geometric style of Decorated Gothic architecture."

palabras= texto.split()
res=Counter(palabras)
print(palabras)
print(res)
print(res.most_common(10))

print()
print(dir(res))
