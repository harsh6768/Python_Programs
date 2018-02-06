

x=input('enter content to write in a.txt \n')
a=open('a.txt','w')
while x:
    a.write(x)
    a.write('\n')
    x=input()
a.close()
a=open('a.txt','r')
b=open('b.txt','w')
x=a.readline()  # to read the content from the file and write the variable
while x:
    if x.find('#')>-1:
        p=x.find('#')
        x=x[:p]
        b.write(x)
        b.write('\n')
        
