# Wap Fibonaci series Using dynamic Programming
fib = []

def fibs(n):
    fib.append(0)
    fib.append(1)
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


n = int(input("Enter the number that position u want: "))
s = fibs(n)
print(s)
print(fib)

"""
#second programme for the fibnaucci series 
# using the  dictionary
dic={}
def fibss(n):
     dic[0]=0
     dic[1]=1
     for i in range(2,n+1):
          dic[i]=dic[i-1]+dic[i-2]
     return(dic[n])
s=fibss(6)
print(s)
print(dic)

"""
