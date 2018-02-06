c=0
try:
    n=int(input("enter the no:"))
    if(n<0):
        n="blabla"
    elif(n==0):
        n=n/0
    for i in range(1,n+1):
        if(n%1==0):
            c=c+1
except ValueError:
    print("it in not an interger:")
except TypeError:
    print("it is no t a positive number")
except ZeroDivisionError:
    print("0 is not natural no. ")
else:
    if(c==2):
        print("it is an prime no.")
    else:
        print("it is not a prime no.")

