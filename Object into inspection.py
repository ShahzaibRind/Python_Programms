class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def explain(self):
        return f'this is {self.first} {self.last}'

    @property
    def email(self):
        if self.first == None or self.last == None:
            return 'Please Set the Email. This is not set'
        return f'{self.first}.{self.last}@yahoo.com'

    @email.setter
    def email(self, string):
        print("Setting Now...")
        names = string.split("@")[0]
        self.first = names.split('.')[0]
        self.last = names.split('.')[1]

    @email.deleter
    def email(self):
        self.first = None
        self.last = None

shahzaib = Employee('Shahzaib', 'rind')
print(shahzaib.email)

print(type(shahzaib))
print("ID is: ", id("shahzaib Rind"))

print(dir(shahzaib))

import inspect
print(inspect.getmembers(shahzaib))