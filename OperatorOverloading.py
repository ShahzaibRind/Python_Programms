class Employee:
    def __init__(self, aname, asal, arole):
        self.name = aname
        self.sal = asal
        self.role = arole

    def printdetails(self):
        return f"My Name is: {self.name} Salary is: {self.sal} and Role is: {self.role}"

    def __str__(self):
        return f"My Name is: {self.name} Salary is: {self.sal} and Role is: {self.role}"

shazzy = Employee("Shahzaib", 789, "Programmer")
print(repr(shazzy))


# rohan = Employee("Rohan", 829, "Student")
# print("Addition: ", shazzy + rohan)
# print("Division: ", shazzy / rohan)


