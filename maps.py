import math

ciudad=[('lisboa',25),('madrid',30),('barcelona',40),('santa cruz',37)]
print(ciudad)

c_to_f= lambda dato: (dato[0], (9/5)*dato[1]+32)

ciudad_faren= list(map(c_to_f, ciudad))
print(ciudad_faren)


"""
import math
def area(r):
    
    calcula el area de un circulo de radio 'r'
    :param r:
    :return:
    
    return math.pi * (r**2)
radios=[2,5,7.01,0.9,20,33]

areas2= map(area,radios)
print()

lista_area= list(areas2)
print(lista_area)

for i in areas2:
    print(i)

"""
"""
import math
def area(r):
    
    calcula el area de un circulo de radio 'r'
    :param r:
    :return:
    
    return math.pi * (r**2)

print(f"{area(5):.2f}")
radios=[2,5,7.01,0.9,20,33]
areas=[]
for i in radios:
    areas.append(area(i))
print(areas)

areas2= map(area,radios)
print()
print(areas2)
print(type(areas2))
lista_area= list(areas2)
print(lista_area)

print("areas2")
print(areas2)

print("1 areas2")
for i in areas2:
    print(i)


print()
print("lambda")
radios=[2,5,7.01,0.9,20,33]
print(list(map(lambda r:math.pi * (r**2), radios)))"""