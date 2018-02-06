from random import*
x=random()                     #RANDOM RETURNS THE FLOAT VALUE

print(x)

def randomList(n):
    t=[0]*n
    for i in range(n):
        t[i] =random.random()
        return t

