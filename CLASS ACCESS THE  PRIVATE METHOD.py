class P:
    def __init__(self,name,alias):
        self.name=name  #public
        self.alias=alias   #private
    def who(self):
        print('name:',self.name)
        print('alias:',self.__alias)
    def __foo(self):                          # private method
        print("this is private method")
    def foo(self):
        print('this is public method')
        self.__foo()


x=P('Aditya','adi')
# print(x.__foo())
x._P__foo()     ## call the private method

