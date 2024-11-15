class Employee():
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    def showDetails(self):
        print("Role:",self.role)
        print("Department:",self.dept)
        print("Salary: Rs",self.salary,end="/-\n")
class Engineer(Employee):
    def __init__(self,name,age,role,dept,salary):
        self.name=name
        self.age=age
        super().__init__(role,dept,age)
    def showDetails(self):
        print("Name:",self.name)
        print("Age:",self.age)
        super().showDetails()
name=input("Enter the name of the Employee: ")
age=int(input("Enter the age of the Employee: "))
role=input("Enter the role of your Employee: ")
dept=input("Enter the department of your Employee: ")
sal=int(input("Enter the salary of your Employee: "))
e1=Employee(role,dept,sal)
engg1=Engineer(name, age, role, dept, sal)
engg1.showDetails()