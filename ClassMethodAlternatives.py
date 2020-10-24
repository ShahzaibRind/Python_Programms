class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asal, arole):
        self.name = aname
        self.salr = asal
        self.role = arole

    def printDetails(self):
        return f"My Name is {self.name} my salary is {self.salr} and my role is {self.role}"

    @classmethod
    def changeLeaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

harry = Employee("Harris", 1000, "Programmer")
shazy = Employee("Shahzaib", 000, "Student")
karan = Employee.from_dash("Karan-10-Actor")

harry.changeLeaves(30)

print(harry.name, harry.role, harry.no_of_leaves)
print(shazy.name)
print(karan.role)
