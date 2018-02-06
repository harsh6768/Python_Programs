"""
read(): it retuns the specified charracter for the file if the argument is omitted the entire content of the file the read
readline():it return the nextline of file as string
readlines(): it return the remaining string
"""
file=open("myfile.txt","w")
l=["this is delhi \n ", "this is paris \n","this is london"]

file.write("hello\n")
file.writelines(l)
file.close()

file1=open("myfile.txt","r+")

print("output of read funciton is")

print(file1.read())
print()

file1.seek(0)

print("output od read(9) functions")
print(file1.read(9))
print()

file1.seek(0)

print("output of the readline functions is ")
print(file1.read(9))
print()

print("output of the readline(9) functions is ")
print(file1.readline(9))

file1.seek(0)

print("output of the readlines funcitons")
print(file1.readlines())
print()
file1.close()