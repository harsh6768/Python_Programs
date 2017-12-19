# some predefined function in the list


list1=[1,2,3,4]
list1.append(20)                # append is used for to add the element in list at the last
print(list1)

list2=[5,7]
list1.extend(list2)             # extend is used to  increase the size of the list
print(list1)

list1.insert(3,10)             # first argument is the position of the list    ,,, insert the element in the specific location
print(list1)

print(list1.pop(3))              # pop is used to get the element form the specific location
print(list1)

s1="welcome to lpu".split()            # split is  used to change the string into list
print(s1)

s2="04/09/2012".split('/')             # we can also the pass the argument int split function
print(s2)
ttuple=('harsh','sumit','anand','himanshu')
list3=list(ttuple)                      #list function is used for
print(list3)



