import collections
# declearing default dictionary
# if the key not found then return the message
defd=collections.defaultdoct(lambda: 'key not found ')

#gtts library chnge the
# pip install gtts

defd['a']=1
print("the value associated with 'a' is : ",end="")
print(defd['a'])

print("the value associated with 'c '",end='')
