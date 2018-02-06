from collections import OrderedDict
print("this is a  Dict:\n")
d={}
d['a']=1
d['b']=2
d['c']=3
d['d']=4

for key,value in d.items ():
    print(key,value)
print("\n this is an ordered Dict:\n")
od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4
for key ,value in od.items ():
    print(key,value)


"""
how to handle missing keys in dictionary

"""
