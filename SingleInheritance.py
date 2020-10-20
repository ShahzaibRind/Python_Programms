class Employee:
    no_of_leaves = 9

    def __init__(self, aname, asal, arole):
        self.name = aname
        self.sal = asal
        self.role = arole

    def printDetails(self):
        return f"My Name is {self.name} salary is {self.sal} and Role is {self.role}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def print_good(cls, string):
        print("This is Good" + string)

class Prgrammer(Employee):
    def __init__(self, aname, asal, arole, alangs):
        self.name = aname
        self.sal = asal
        self.role = arole
        self.languages = alangs

    def print_prog(self):
        return f"My Name is {self.name} salary is {self.sal} and Role is {self.role} Languages Are {self.languages}"
harry = Employee("Hariss", 1000, "Programmer")
shazy = Employee("Shahzaib", 900, "Student")

jabar = Prgrammer("Jabbar", 890, "Freelancer", ['Python', 'Java', 'C++'])
toqeer = Prgrammer("Touqeer", 900, "Programmer", ['Python'])

print(jabar.print_prog())