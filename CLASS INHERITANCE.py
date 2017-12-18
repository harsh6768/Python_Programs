class vehicle():  # parent class
    def __init__(self):
        self.__name = input("enter the name of the car:")  # private member
        self.__color = input("enter the color of the car:")


class Car(vehicle):         # child class
    def __init__(self):
        super(Car, self).__init__()                        # call the parent
        self.__model = input("enter the model of the car:")

    def getDescription(self):
        print("Description of the Car")
        return self._vehicle__name + " " + self.__model + " in " + self._vehicle__color + " color!"

def main():
    c = Car()
    print(c.getDescription())

if __name__ == "__main__":
    main()
