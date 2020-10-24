class Employee:
    var = 3
    _prot = 4
    __priva= 4

    def __init__(self, aname, asal, arole):
        self.name = aname
        self.sal = asal
        self.role = arole

    def printdetails(self):
        return f"My name is {self.name}, My Salary is: {self.sal} and My Role is: {self.role}"


sharry = Employee("Shahzaib Rind", 222, "Programmer")

print(sharry._prot)
# print(sharry._Employee.__priva)

# Polymorphisim example

print(10+12)
print("10" + "12")
