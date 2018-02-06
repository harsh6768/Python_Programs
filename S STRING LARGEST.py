import string
str1=""
a="MAHABHARAT"
b="MAHAAKAL"
str2=0
if(len(a)<len(b)):
    str2=len(b)
elif(len(a)>len(b)):
    str2=len(a)
else:
    str2=len(a)
for i in range(str2):
    j=i
    if(a[i]==b[j]):
        str1=str1+a[i]
        i=i+1
        j=j+1
print(str1)





