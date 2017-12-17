class person:
    def __init__(self,n):
        self.__name=n
    def __display(self):
        print(self.__name)

person1=person(19)
person1._person__display()

print(person1._person__name)
