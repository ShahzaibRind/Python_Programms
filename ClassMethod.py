class Employee:
    no_of_leaves = 6

    def __init__(self, aname, asal, arole):
        self.name = aname
        self.sal = asal
        self.role = arole

    def printdetails(self):
        return f"My Name is {self.name} my Salary is {self.sal} and my role is {self.role}"

    @classmethod
    def changeleaves(cls, newleaves):
        cls.no_of_leaves = newleaves

harry = Employee("Hariss", 1000, "Programmer")
shazzy = Employee("Shahzaib", 100, "Student")
Employee.changeleaves(34)
print(harry.no_of_leaves)
print(shazzy.role)