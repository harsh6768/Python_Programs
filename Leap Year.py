"""def leap():
    leap=int(input("Enter the any Year that u want to check the leap year or not :"))
    A="Leap Year"
    B="Not a Leap Year"
    if(leap%400==0):
        return A
    elif(leap%100==0):
        return A
    elif(leap%4==0):
        return A
    else:
        return B
year=leap()
print(year)
"""
x=int(input())
A="true"
B="false"
def leap():
    while(1900<=x and x<=100000):
        if(x%400==0):
            return A
        elif(x%100==0):
            return A
        elif(x%4==0):
            return A
        else:
            return B
l=leap()
print(l)
