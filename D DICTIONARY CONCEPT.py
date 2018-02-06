#DEIFNE THE DICTIOANRY
address={}
address["John"]=" John@gmail.com"
address["Adam"]=" Adam@gmail.com"
address["Peter"]=" Peter@gmail.com"
print(address)

#UPDATE THE DICTIONARY
address['Adam']='harshchaurasiya6768@gmail.com'
print(address)

# predefined function
"""
del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary
"""

del(address['Peter'])
print(address)

address.clear()
print(address)

#str used to change the dictionary into string
#
address["John"]=" John@gmail.com"
address["Adam"]=" Adam@gmail.com"
address["Peter"]=" Peter@gmail.com"
print(str(address))
"""
Comparing the value

dict1 = {'Name': 'Zara', 'Age': 7};
dict2 = {'Name': 'Mahnaz', 'Age': 27};
dict3 = {'Name': 'Abid', 'Age': 27};
dict4 = {'Name': 'Zara', 'Age': 7};
print("Return Value : %d",cmp(dict1, dict2))
print("Return Value : %d",cmp(dict2, dict3))
print("Return Value : %d",cmp(dict1, dict4))
"""
