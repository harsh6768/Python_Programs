class vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
def __add__(self, other):
    return vector(self.a + other.a, self.b + other.b)
def __str__(self):
    return'(%d,%d)'%(self.a, self.b)
p1=vector(2,5)
p2=vector(2,3)
print(p1+p2)