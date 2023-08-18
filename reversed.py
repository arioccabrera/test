
print(round(10.5))
print(round(10.6))
print(round(10.1))
print(round(10.5569999,3))
print(round(1.5999999,4))

print()

print(sum([1,2,3,4,5]))
print(sum([1,2,3,4,5],-5))
print(sum({'a':1, 'b':2, 'c':3, 'd':4, 'e':5}.values()))


print()

print(abs(-5))
print(abs(5))
print(abs(-3.14))
print(abs(-3.14))


print("arioc silvera".__len__())


lista=[1,2,3,4,5]

res=reversed(lista)

print(res)
print(type(res))

print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista)))


"""
lista=[1,55,997,232,5]
print(max(lista))

tuple=(1,55,997,232,5)
print(max(tuple))

set={1, 55, 997, 232, 5}
print(max(set))

dicci={'a':1, 'b':55, 'e':997, 'c':232, 'd':5}
print(max(dicci))
print(max(dicci.values()))


nombres=['Caslo','Cesar','Caslota','Antonio', 'Vanessaa', 'Zach']
print(max(nombres))
print(min(nombres))
print(max(nombres, key=lambda name: len(name)))
print(min(nombres, key=lambda name: len(name)))


musicas=[
    {"grupo":'a', "verbenas":2},
    {"grupo":'b', "verbenas":45},
    {"grupo":'c', "verbenas":25},
    {"grupo":'d', "verbenas":8}
]

print(max(musicas, key=lambda music: music["verbenas"]))
print(min(musicas, key=lambda music: music["verbenas"]))
print(max(musicas, key=lambda music: music["verbenas"])['grupo'])
print(min(musicas, key=lambda music: music["verbenas"])['grupo'])"""
