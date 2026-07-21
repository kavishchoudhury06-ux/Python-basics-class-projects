#private access modifier

class Employee:
    
    def __init__(self, name, salary):
        self.name = name # public
        self.__salary = salary # private

    def get_salary(self):
        print("Salary:", self.__salary)
        
emp = Employee("Robert", 60000)

print(emp.name) # Public accessible
emp.get_salary() # Accessing private correctly
# print(emp.__salary) # Error: Not accessible directly

