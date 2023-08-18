

lista=[1,6,2,54,78,9]
print(lista)
lista.sort()
print(lista)
print(lista)

print()
numeros=(1,6,2,54,78,9)
print(numeros)
print(sorted(numeros))
print(numeros)

print(sorted(numeros, reverse=True))

print(set(sorted(numeros)))


usuarios=[
    {"user":"manuel","tweets":["is simply dummy text","is simply dummy text"]},
    {"user":"pedro","tweets":["is simply dummy text","is simply dummy text"]},
    {"user":"kevin","tweets":[]},
    {"user":"caslito","tweets":["is simply dummy text","is simply dummy text"]},
    {"user":"vicente","tweets":[]}]


print(usuarios)
print(sorted(usuarios, key=lambda person:person["user"]))



musicas=[
    {"grupo":'a', "verbenas":2},
    {"grupo":'b', "verbenas":45},
    {"grupo":'c', "verbenas":25},
    {"grupo":'d', "verbenas":8}
]
print(musicas)
print(sorted(musicas,key=lambda fiestas: fiestas["verbenas"], reverse=True))