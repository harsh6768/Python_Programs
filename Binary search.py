count=0
def BinarySearch(list1):
    global count
    count=0
    first=0
    last=len(list1)-1
    num=int(input("enter a number which u want to search:"))
    while(first<last):
        mid=int((first+last)/2)
        if(num>list1[mid]):
            first=mid+1
        elif(num<list1[mid]):
            last=mid-1
        elif(num==list1[mid]):
            print(list1[mid]," is found at position: ",mid+1)
            count+=1
            break
if(count==-1):
        print("Searching Unsuccessfull!")
def main():
    list1 = []
    a = int(input("how many number u want to insert:"))
    for i in range(a):
        list1.append(int(input("enter a number")))
    list1=sorted(list1)       #for sorting the list
    print(list1)
    BinarySearch(list1)

if __name__=="__main__":
    main()
