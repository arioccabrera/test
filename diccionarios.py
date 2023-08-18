paises= {'br': 'brasil', 'us': 'estados unidos', 'sp': 'españa'}

print(paises)
print(type(paises))

print()
paises= dict(br='brasil', us='estados unidos', sp='españa')
print(paises)
print(type(paises))

print()
print(paises.get('jp'))

paises= dict(br='brasil', us='estados unidos', sp='españa')
pais= paises.get('sp', 'Error')
print(pais)

paises= {'br': 'brasil', 'us': 'estados unidos', 'sp': 'españa'}
print('br' in paises)
print('españa' in paises)


paises= {'br': 'brasil', 'us': 'estados unidos', 'sp': 'españa'}
print(paises)
paises['uk']= 'reino unido'
print(paises)

paises= {'br': 'brasil', 'us': 'estados unidos', 'sp': 'españa'}
print(paises)
paises.update({'br': 'Brazil'})
print(paises)

print()
paises= {'br': 'brasil', 'us': 'estados unidos', 'sp': 'españa'}
print(paises.pop('br'))
print(paises)


print()
d= dict(a=1, b=2, c=3)
print(d)
print(type(d))
d.clear()
print(d)

print()
d= dict(a=1, b=2, c=3)
print(d)
print(type(d))
nuevo= d.copy()
print(nuevo)
nuevo['d']=4
print(nuevo)
print(d)

print()
d= dict(a=1, b=2, c=3)
print(d)
nuevo=d
print(nuevo)
nuevo['d']=4
print(nuevo)
print(d)

print()
print()
otro= {}.fromkeys('a', 'b')
print(otro)
print(type(otro))

print()
otro= {}.fromkeys(['nombre', 'apellido', 'mail'], 'vacio')
print(otro)
print(type(otro))

print()
otro= {}.fromkeys('tests', 'vacio')
print(otro)
print(type(otro))


print()
otro= {}.fromkeys(range(1,11), 'vacio')
print(otro)
print(type(otro))