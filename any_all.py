


print(all([0,1,2,3,4]))
print(all([1,2,3,4]))
print(all([]))
print(all((1,2,3,4)))
print(all({1, 2, 3, 4}))
print(all('Arioc'))

print()
nombres=['Caslo','Cesar','Caslota','Casla']

print([persona[0]=='C' for persona in nombres])

print(all([persona[0]=='C' for persona in nombres]))

print()

print(([letra for letra in 'eio' if letra in 'aeiou']))


print()
print()

print(any([0,1,2,3,False]))
print(any([]))
print(any([False]))
print(any([{},{} ,{} ,{} , 1]))

print()

nombres=['Caslo','Cesar','Caslota','Casla', 'Vanessa']


print(any([persona[0]=='C' for persona in nombres]))
