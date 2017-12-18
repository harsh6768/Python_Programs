list1 = []


def fac(n):
    list1.append(1)  # to multiply the list1[i-1]*i we need the 1 for the factorial
    for i in range(1, n + 1):            ## main concept
        list1.append(list1[i - 1] * i)
    return (list1[n])


n = int(input('Enter The Number: '))
s = fac(n)
print(s)
print(list1)

"""
##second programme for the factorial programme
print()
dic={}
def facs(n):
     dic[0]=1
     for i in range(1,n+1):
          dic[i]=dic[i-1]*i
     return(dic[n])
s=facs(n)
print(s)
print(dic.values())

"""
