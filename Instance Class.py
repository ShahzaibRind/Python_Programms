class Employee:
    noOfLeaves = 9
    pass

harry = Employee()
shazy = Employee()

harry.name = "Haris"
harry.salr = "3000"
harry.role = "Programmer"

shazy.name = "Shahzaib"
shazy.salr = "0000"
shazy.role = "Student"

print(Employee.noOfLeaves)
shazy.noOfLeaves = 10
print(shazy.__dict__)
print(Employee.noOfLeaves)