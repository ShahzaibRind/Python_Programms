class Employee:
    no_of_leaves = 5

    def __init__(self, aname, asal, arole):
        self.name = aname
        self.sal = asal
        self.role = arole

    def printDetails(self):
        return f"My name is {self.name} salary is {self.sal} and role is {self.sal}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def pring_good(string):
        print("This is Good", string)

harry = Employee("Hariss", 200, "Programmer")
shazzy = Employee("Shahzaib", 000, "Student")
karan = Employee.from_dash("Karan-22-Johar")

Employee.change_leaves(30)

print(harry.sal)
print(shazzy.name)
print(karan.role)
Employee.pring_good("shazzy")