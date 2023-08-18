#f(x)= a * x **2 + b * x + c

def ecuacion(a,b,c):
    return lambda x: a * x ** 2 + b * x + c

test= ecuacion(2,3,-5)

print(test(0))
print(test(1))
print(test(2))




"""
personas= ['juan cervantes', 'george orwell', 'antonio machado', 'rosalia de castro', 'willian chespirrrr']

personas.sort(key=lambda apellido: apellido.split(' ')[-1].lower())
#aqui lo que hace es pasar cada elemento de la lista a una funcion lambda, separa las palabra cada vez que encuentra un espacio, coge solo el ultimo elemento y lo pone en minusculas para ordenarlo

print(personas)


def funcion(x):
    return x*3+1

print(funcion(4))


print()
print()
lambda x: x*3+1

prueba= lambda x: x*3+1
print(prueba(2))
print(type(prueba))


nombre_completo= lambda nombre, apellido: nombre.strip().title()+ ' '+ apellido.strip().title()
#strip() quita los espacios al principio y al final de una string
#title() Te pone la primera letra de la string en mayuscula y el resot en minuscula

print(nombre_completo('arioc', '    silVERa CABrera   '))



frase= lambda :'Python esta guapisimo'
uno= lambda x: x*3
dos= lambda x,y: x+y
tres= lambda x,y,z: x+y+z

print(frase())
print(uno(2))
print(dos(5,7))
print(tres(6,3,1))



"""