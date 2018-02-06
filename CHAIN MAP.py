"""

dic1={1:'a',2:'b',3:'c'}
dic2={3:'d',4:'e',3:'f'}
dic3={5:'g',6:'h',3:'i'}
dic4={}
dic4={**dic1,**dic2,**dic3}
print(dic4)

for i in range(dic1,dic2,dic3):
    dic4.update(i)
print(dic4)
"""
"""
 chain integrate or incapculates multile dictionarries into one unit
"""

import collections
dic1={'a':1,'b':2}
dic2={'b':3,'d':4}

chain=collections.ChainMap(dic1,dic2)

# print chainmapusing chainmap
print(chain.maps)


