# wap to compute  the area and perimeter
import math
class circle:
    def __init__(self):
        self.radious=int(input("ENTER ANY NUMBER::::"))            # take the input from the user
    def area(self):
        area1=math.pi*pow(self.radious,2)            # pow is a predifened function in math library to squaring the numbers
        print("AREA OF CIRCLE IS :",area1)
    def cir(self):
        peri=2*math.pi*self.radious
        print("circumference of circle:",peri)
circle1=circle()
circle1.area()
circle1.cir()

