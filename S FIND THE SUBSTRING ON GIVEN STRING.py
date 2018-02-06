# find the string

"""
"string1="abcdcdc"
print(string1.count("cdc"))
"""

string1 =input("enter the string:")
sub=input("enter substring:")
count=0
def sub_string(string1,sub):
    for x in range(len(string1)):
        global count
        count=string1[x:].find(sub)
        count=count+1
        count = string1[x+1:].find(sub)
print(count)
sub_string(string1,sub)



