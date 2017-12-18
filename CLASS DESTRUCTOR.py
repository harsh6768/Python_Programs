class point:
    def __init__(self,x,y):     #constructor
        self.x=x
        self.y=y
    def __del__(self):         #destructor
        class_name=self.__class__.__name__                # predi
        print(class_name,"destructor")
    def show(self):
        print("x=",self.x,"y=",self.y)

p1=point(1,2)
p2=p1                #copy
p3=p1

print(id(p1))
print(id(p2))         # id is predefined to see tthe id of the any

del p1
p2.show()             # print the value
del p2
del p3                    # DESTRUCTOR CALL