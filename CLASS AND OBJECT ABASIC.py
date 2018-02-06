class employee :
    def __init__(self):          #constructor   self is a pointer
        self.name="abc"
        self.salary=10
    def disp(self):            # memeber function
        print("NAME:" ,self.name)
        print("salary:",self.salary)
emp=employee()
emp.disp()
print(emp.name)