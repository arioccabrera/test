import time
from multiprocessing import Pool

CONTADOR = 50000000

def cuenta_regresiva(n):
    while n >0:
        n -=1

if __name__ == '__main__':
    pool = Pool(processes=2)
    inicio = time.time()
    r1 = pool.apply_async(cuenta_regresiva, [CONTADOR//2])
    r2 = pool.apply_async(cuenta_regresiva, [CONTADOR // 2])
    pool.close()
    pool.join()
    fin = time.time()
    print(f"tiempo en segundos {fin - inicio}")




"""
import time
from threading import Thread

CONTADOR = 50000000

def cuenta_regresiva(n):
    while n >0:
        n -=1

t1= Thread(target=cuenta_regresiva, args=(CONTADOR//2,))
t2= Thread(target=cuenta_regresiva, args=(CONTADOR//2,))

inicio = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
fin= time.time()

print(f"tiempo en segundos {fin - inicio}")








import time
from threading import Thread

CONTADOR = 50000000

def cuenta_regresiva(n):
    while n >0:
        n -=1

inicio = time.time()
cuenta_regresiva(CONTADOR)
fin= time.time()

print(f"tiempo en segundos {fin - inicio}")






import sys

a=[]
b = a
print(sys.getrefcount(a))"""