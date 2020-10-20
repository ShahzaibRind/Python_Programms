class Employee:
    leaves = 8

    def __init__(self, aname, asal, arole):
        self.name = aname
        self.sal = asal
        self.role = arole

    def print(self):
        return f"My Name is {self.name} my salary is {self.sal} and my role is {self.role}"



harry = Employee("Shahzaib", 1000, "Student")
print(harry.sal)