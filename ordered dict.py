from collections import OrderedDict

dict1= {'a':1, 'b':2, 'c':3}
dict2= {'c':3, 'a':1, 'b':2}

print(dict1== dict2)

dict1= OrderedDict( {'a':1, 'b':2, 'c':3})
dict2= OrderedDict( {'c':3, 'a':1, 'b':2})

print(dict1== dict2)