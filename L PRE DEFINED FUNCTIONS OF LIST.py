# some predefined function in the list



#append
list1=[1,2,3,4]
list1.append(20)                # append is used for to add the element in list at the last
print(list1)

#list.extend(seq)---Appends the contents of seq to list
list2=[5,7,"harsh"]
list1.extend(list2)             # extend is used to  increase the size of the list
print(list1)

#insert
list1.insert(3,10)             # first argument is the position of the list    ,,, insert the element in the specific location
print(list1)

#pop
print(list1.pop(3))              # pop is used to get the element form the specific location
print(list1)

#split
s1="welcome to lpu".split()            # split is  used to change the string into list
print(s1)

s2="04/09/2012".split('/')             # we can also the pass the argument int split function
print(s2)

#list
ttuple=('harsh','sumit','anand','himanshu')
list3=list(ttuple)                      #list function is used for
print(list3)

#list.count(obj)------ Returns count of how many times obj occurs in list

list1=[1,2,3,4,5,3,4,5,8,3]
print(list1.count(3))









