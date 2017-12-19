# MergeSort
def merge(a, b):
    c = []
    while (len(a) != 0 and len(b) != 0):
        if (a[0] < b[0]):
            c.append(a[0])
            a.pop(0)  # the main concept
        else:
            c.append(b[0])
            b.pop(0)
    if (len(a) == 0):
        c = c + b                                  # append the b list with the c list if a list is empty
    else:
        c = c + a                                   # append the a list with the c list if b list is empty
    return c


def mergeSort(list1):
    if (len(
            list1) == 1):                       # when we are dividing the list then at  last it will contain the one number then there is no  need to call the recursion functin
        return list1
    else:
        mid = len(list1) // 2
        a = mergeSort(list1[:mid])
        b = mergeSort(list1[mid:])
    return merge(a, b)                          # list c return


def main():
    list1 = []
    num = int(input("how many u want to insert into the list:"))
    for i in range(num):
        list1.append(int(input("enter a number:")))
    print(mergeSort(list1))


if __name__ == "__main__":
    main()
























