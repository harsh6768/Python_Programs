class vehicle():
    def __init__(self,name,color):
        self.__name=name        # private member
        self.__color=color
    def getcolor(self):
        return self.__color
    def setcolor(self,color):
        self.__color=color
    def getname(self):
        return self.__name
class Car(vehicle):
    def __init(self,name,color,model):
        super(Car,self).__init__(name,color)                # call the parent
        self.__model=model
    def getDedcription(self):
        return self.getname()+self.__model+"in "+self.getcolor()+"color"
c=Car("Ford Mustang","REd","GT350")
print(c.getDescription())
print(c.getname())