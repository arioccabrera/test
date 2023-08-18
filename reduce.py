from functools import reduce


datos=[1,2,3,4,5,6]

print(reduce(lambda x,y: x*y, datos))


res=1
for i in datos:
    res *= i

print(res)