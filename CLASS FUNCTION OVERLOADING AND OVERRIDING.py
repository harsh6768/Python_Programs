class A:
    def fun(self):
        print('A')
class B(A):
    def fun(self):
        print('B')
        super(B,self).fun()
class C(A):
    def fun(self):
        print('C')
        super(C,self).fun()
class D(C,B):
    def fun(self):
        print('D')
        super(D,self).fun()
d=D()
d.fun()
