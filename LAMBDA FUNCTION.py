"""
LAMBDA FUNCTION:
it is funciton without  a name
"""
f=lambda x,y:x+y
print(f(1,1))



"""

lambda is always used with map function
map two 


"""

Celsius=[39.5,36.5,37.3,37.8]
Fahrenhiet=list(map(lambda x:(float(9)/5)*x +32,Celsius))
print(Fahrenhiet)

c=list(map(lambda x:(float(5)/9)*(x-32),Fahrenhiet))
print(c)


a=[1,2,3,4]
b=[17,12,11,10]

print(list(map(lambda x,y:x+y,a,b)))