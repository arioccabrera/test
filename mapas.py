receita={'jan': 100, 'fev': 250, 'mar':400 }

print(receita)

print()
for chave in receita:
    print(chave)

print()
for chave in receita:
    print(receita[chave])

print()
for chave in receita:
    print(f"{chave} {receita[chave]}")
print(receita.keys())

print()
for chave in receita.keys():
    print(f"{chave} {receita[chave]}")

print()
print(receita.values())

for valor in receita.values():
    print(valor)

print()
print(receita.items())
for chave, valor in receita.items():
    print(f"{chave}: {valor}")

print()
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

receita={100,100, 250, 250, 400, 400 }
print(receita)
print(type(receita))

if 100 in receita:
    print("cierto")
else:
    print("falso")

receita={99,2,34,23,2,12,1,44,5,34}
print(receita)
print(type(receita))
print(len(receita))

print()
receita={'a',2.34,None,True}
print(receita)
print(type(receita))
print(len(receita))

print()
for valor in receita:
    print(valor)

print()
receita={99,2,34,23,2,12,1,44,5,34}
receita.add(4)
receita.add(4)
print(receita)

print()
receita={99,2,34,23,2,12,1,44,5,34}
receita.discard(2)
receita.discard(2)
print(receita)

print()
receita={99,2,34,23,2,12,1,44,5,34}
nuevo = receita.copy()
nuevo.add(99999)
print(receita)
print(nuevo)

print()
receita={99,2,34,23,2,12,1,44,5,34}
nuevo = receita
nuevo.add(99999)
print(receita)
print(nuevo)

print()
receita={99,2,34,23,2,12,1,44,5,34}
receita.clear()
print(receita)

print()
estudiandtes1={'pedro', 'maria', 'juan', 'laura', 'ana'}
estudiandtes2={'ana', 'antonio', 'vanessa'}
print(estudiandtes1)
print(estudiandtes2)

lista= estudiandtes1.union(estudiandtes2)
print(lista)

print()
estudiandtes1={'pedro', 'maria', 'juan', 'laura', 'ana'}
estudiandtes2={'ana', 'antonio', 'vanessa'}
print(estudiandtes1)
print(estudiandtes2)

lista= estudiandtes1 | estudiandtes2
print(lista)

print()
estudiandtes1={'pedro', 'maria', 'juan', 'laura', 'ana'}
estudiandtes2={'ana', 'antonio', 'vanessa'}
print(estudiandtes1)
print(estudiandtes2)

lista= estudiandtes1.intersection(estudiandtes2)
print(lista)

print()
estudiandtes1={'pedro', 'maria', 'juan', 'laura', 'ana'}
estudiandtes2={'ana', 'antonio', 'vanessa'}
print(estudiandtes1)
print(estudiandtes2)

lista= estudiandtes1 & estudiandtes2
print(lista)


print()
estudiandtes1={'pedro', 'maria', 'juan', 'laura', 'ana'}
estudiandtes2={'ana', 'antonio', 'vanessa'}
print(estudiandtes1)
print(estudiandtes2)

lista= estudiandtes1.difference(estudiandtes2)
print(lista)

lista= estudiandtes2.difference(estudiandtes1)
print(lista)

print()
receita={99,2,34,23,2,12,1,44,5,34}
print(sum(receita))
print(max(receita))
print(min(receita))
print(len(receita))