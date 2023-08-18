from sys import getsizeof

nombres=['Caslo','Cesar','Caslota','Casla', 'Vanessa']

print(any(name[0]== 'C' for name in nombres))

result= [name[0]== 'C' for name in nombres]
print(type(result))
print(result)

result= (name[0]== 'C' for name in nombres)
print(type(result))
print(result)


print()

from sys import getsizeof

list_comp= getsizeof([x*10 for x in range(1000)])
set_comp= getsizeof({x * 10 for x in range(1000)})
dic_comp= getsizeof({x:x * 10 for x in range(1000)})
gen= getsizeof(x*10 for x in range(1000))

print(f"Tamaño de lista:{list_comp} bytes")
print(f"Tamaño de set:{set_comp} bytes")
print(f"Tamaño de diccionario:{dic_comp} bytes")
print(f"Tamaño de generator:{gen} bytes")



gen= (x*10 for x in range(10))
print(gen)
print(type(gen))

for i in gen:
    print(i, end=' ')