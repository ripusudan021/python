class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary
    
    def showDetails(self):
        print(f"Role = {self.role}\nDepartment = {self.department}\nSalary = {self.salary}")
    
class Engineer(Employee):
    def __init__(self,name,age):
        super().__init__("Engineer", "IT", "75,000")
        self.name = name
        self.age = age
    def showDetails(self):
        print(f"Name = {self.name}\nAge = {self.age}")
        super().showDetails()
eng1 =Engineer("Rahul",25)
eng1.showDetails()


        
        