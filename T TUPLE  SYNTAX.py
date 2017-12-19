#TUPLE SYNTAX
"""
To create a tuple with a single element, we have to include the comma:
t1 = ('a',)
 type(t1)
<type 'tuple'>
Without the comma, Python treats ('a') as a string in parentheses:
 t2 = ('a')
 type(t2)		??

"""
ttuple=('a','b','c',4,5)
print(ttuple[0])           # tuple slicing

tuple1=('A',)+ttuple[1:]          #update the tuple

print(tuple1)

#CHANGE THE LIST TO TUPLE---------tuple()
list1=[1,2,3,4,5,6]

tuple2=tuple(list1)
print(tuple2)

