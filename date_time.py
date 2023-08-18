import datetime
import functools
import timeit


def test(n):
    suma = 0
    for num in range(n*200):
        suma = suma + num ** num +4
    return suma

print(timeit.timeit((functools.partial(test,2)), number=10000))






"""
import datetime
import timeit

#bucle for
tiempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tiempo)

#list comprehension
tiempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tiempo)

#map
tiempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tiempo)








nacimiento = datetime.datetime.strptime('28/11/1988', '%d/%m/%Y')
print(nacimiento)

nacimiento = input("fecha de nacimiento: (dd/mm/aaaa)")
nacimiento = datetime.datetime.strptime(nacimiento, '%d/%m/%Y')
print(nacimiento)

almuerzo = datetime.time(14, 30, 0)
print(almuerzo)




nacimiento = datetime.datetime.strptime('28/11/1988', '%d/%m/%Y')
print(nacimiento)

nacimiento = input("fecha de nacimiento: (dd/mm/aaaa)")
nacimiento = datetime.datetime.strptime(nacimiento, '%d/%m/%Y')
print(nacimiento)

almuerzo = datetime.time(14, 30, 0)
print(almuerzo)




from textblob import TextBlob

def formatea_fecha(fecha):
    return f"{fecha.day} de {TextBlob(fecha.strftime('%B')).translate(to='pt-br')} de {fecha.year}"

hoy = datetime.datetime.today()
print(formatea_fecha(hoy))




def formatea_fecha(fecha):
    if fecha.month == 1:
        return f"{fecha.day} de enero de {fecha.year}"
    elif fecha.month == 2:
        return f"{fecha.day} de febrero de {fecha.year}"
    elif fecha.month == 3:
        return f"{fecha.day} de marzo de {fecha.year}"
    elif fecha.month == 4:
        return f"{fecha.day} de abril de {fecha.year}"
    elif fecha.month == 5:
        return f"{fecha.day} de mayo de {fecha.year}"
    elif fecha.month == 6:
        return f"{fecha.day} de junio de {fecha.year}"
    elif fecha.month == 7:
        return f"{fecha.day} de julio de {fecha.year}"
    elif fecha.month == 8:
        return f"{fecha.day} de agosto de {fecha.year}"
    elif fecha.month == 9:
        return f"{fecha.day} de septiembre de {fecha.year}"
    elif fecha.month == 10:
        return f"{fecha.day} de octubre de {fecha.year}"
    elif fecha.month == 11:
        return f"{fecha.day} de noviembre de {fecha.year}"
    elif fecha.month == 12:
        return f"{fecha.day} de diciembre de {fecha.year}"


hoy =  datetime.datetime.today()
print(hoy)

hoy_formateado = hoy.strftime('%d/%b/%y')
print(hoy_formateado)

print(formatea_fecha(hoy))






nacimiento = input("Año de nacimento (dd/mm/aaa): ")
nacimiento = nacimiento.split('/')
nacimiento= datetime.datetime(int(nacimiento[2]),int(nacimiento[1]),int(nacimiento[0]))

if nacimiento.weekday() == 0:
    print("Naciste un Lunes")
elif nacimiento.weekday() == 1:
    print("Naciste un martes")
elif nacimiento.weekday() == 2:
    print("Naciste un miercoles")
elif nacimiento.weekday() == 3:
    print("Naciste un jueves")
elif nacimiento.weekday() == 4:
    print("Naciste un viernes")
elif nacimiento.weekday() == 5:
    print("Naciste un sabado")
elif nacimiento.weekday() == 6:
    print("Naciste un domingo")


matenimiento = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)),datetime.time())
print(matenimiento)
print(type(matenimiento))
print(repr(matenimiento))

print(matenimiento.weekday())




ahora = datetime.datetime.now()
print(ahora)
print(type(ahora))
print(repr(ahora))

hoy = datetime.datetime.today()
print(hoy)
print(type(hoy))
print(repr(hoy))




fecha_compra= datetime.datetime.now()
print(fecha_compra)

regla_voucher = datetime.timedelta(days=5)
print(regla_voucher)

fin_voucher = fecha_compra + regla_voucher

print(fin_voucher)




dia_hoy= datetime.datetime.now()
cumpleaños = datetime.datetime(2022, 11, 28, 0)

tiempo_para_cumple= cumpleaños - dia_hoy

print(type(tiempo_para_cumple))
print(repr(tiempo_para_cumple))

print(tiempo_para_cumple.days)
print(f"falta {tiempo_para_cumple.days} días pa mi cumple! :D")



print(datetime.MAXYEAR)
print(datetime.MINYEAR)
print(datetime.datetime.now())
print(repr(datetime.datetime.now()))
print()

inicio = datetime.datetime.now()
print(inicio)
inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)
print(inicio)
print()
print()

evento= datetime.datetime(2025, 1, 1, 0)
print(type(evento))
print(type('04/11/2022'))
print(evento)
print()

nacimiento = input("Año de nacimento (dd/mm/aaa): ")
print(nacimiento)
nacimiento = nacimiento.split('/')
print(nacimiento)

nacimiento= datetime.datetime(int(nacimiento[2]),int(nacimiento[1]),int(nacimiento[0]))
print(nacimiento)
print(type(nacimiento))
print()

inicio = datetime.datetime.now()

print(inicio.year)
print(inicio.month)
print(inicio.day)
print(inicio.hour)
print(inicio.minute)
print(inicio.microsecond)

print(dir(inicio))
"""