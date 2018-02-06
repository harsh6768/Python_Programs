#LIST SLICING
list1=['harsh','shubham',78,69.98,2,3,5,"sample"]

list3=list1[-1::]
print(list3)

list3=list1[::]           # copy the whole list1 by slicing from the list3
print(list3)

list3=list1[1]            # slice the element from the specific location
print(list3)

list3=list1[:3]                       # start from the index 0 and end in 2 index that is 78
print(list3)

list2=[5,"simple"]
list1.append(100)
print(list1)

# difference between append and extends
list1.append(list2)
print(list1)

del list1[9:10]             # del is used to delete the element from the list
list1.extend(list2)
print(list1)

print(list2*4)            #print of the element of the



