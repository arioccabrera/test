
nombres= ['vanessa', 'carla', 'ana']

lista= list(map(lambda name: f"Su profesora es {name}", filter(lambda name: len(name)<5,nombres)))

print(lista)



"""

usuarios=[
    {"user":"manuel","tweets":["is simply dummy text","is simply dummy text"]},
    {"user":"pedro","tweets":["is simply dummy text","is simply dummy text"]},
    {"user":"kevin","tweets":[]},
    {"user":"caslito","tweets":["is simply dummy text","is simply dummy text"]},
    {"user":"vicente","tweets":[]}]

print()
#inactivos= list(filter(lambda user: len(user["tweets"])==0, usuarios))
inactivos= list(filter(lambda user: not user["tweets"], usuarios))

print(inactivos)

paises=['','españa', '', 'portugal', '', 'mexico', 'argentina', 'uk']
print(paises)

resultado=filter(lambda pais: pais!='', paises)

print(list(resultado))
print(list(resultado))



import statistics

datos=[1.2, 3.0, 4.6, 0.9, 1 ,5.5]
media= statistics.mean(datos)
print(f"Media {media:.2f}")

resultado=filter(lambda valor: valor>media, datos)
print(resultado)
print(type(resultado))
print(list(resultado))

print(list(resultado))"""