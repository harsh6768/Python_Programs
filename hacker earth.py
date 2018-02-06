x=input()
count=0
countt=0
sum1=0
sum2=0
avgg=0
for i in range(len(x)):
    if(x[i]>=0):
        count=count+1
        sum1=sum1+x[i]
    else:
        countt=countt+x[i]
        sum2=sum2+x[i]
avgg=(sum1+sum2)/(count+countt)
print("Total positive numbers:"+count)
print("Total negative numbers:"+countt)
print("Total Sum:"+sum1)
print("Average:"+avgg)
if(count==countt and sum1==sum2 ):
    print("Perfect Collection")
else:
    print("Not a Perfect Collection")