def partition(list1):
    pivot=list1[len(list1)-1]
    left=[]
    right=[]
    i=0
    while(i<len(list1)-1):
        if(list1[i]<pivot):
            left.append(list1[i])
        else:
            right.append(list1[i])
        i+=1
    return (pivot,left,right)    #return the pivot element ,left list(having nnumber less than ) and right list (having number greater than the pivot number)

def quickSort(list1):
    if(len(list1)<=1):
        return list1
    else:
        (piv,leftSort,rightSort)=partition(list1)           #get the value of pivot ,left list and right list
        a=quickSort(leftSort)
        b=quickSort(rightSort)
    return (a+[piv]+b)              #return the sorted list

def main():
    list1=[]
    num=int(input("how many numbers u want to insert:"))
    for i in range(num):
        list1.append(int(input("enter a number:")))
    print(quickSort(list1))
if __name__=="__main__":
    main()








