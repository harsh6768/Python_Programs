
class employee:
    ec=0
    def __init__(self,n,s):                       #constructor
        self.name=n # data memeber
        self.salary=s
        employee.ec+=1             # for the calcualting the no. of employee
    def disp(self):
        print("name:",self.name)
        print("salary:",self.salary)
    def empcount(self):
        print("total employee:=%d"% employee.ec)      ##
emp1=employee("sun",2000)
emp1.disp()
print(emp1.name)
print(emp1.salary)


emp2=employee("harsh",1000)
emp3=employee("deepak",10000)
emp1.empcount()
