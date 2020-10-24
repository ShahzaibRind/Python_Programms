class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asal, arole):
        self.mame = aname
        self.sal = asal
        self.role = arole

    def print_details(self):
        return f"My Name is {self.name} Salary is {self.sal} and Role is {self.role}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves= new_leaves

class Player:
    var = 9
    game = 4
    def __init__(self, name,game):
        self.name = name
        self.game = game

    def print_det(self):
        return f"My Name is {self.name} and Game is {self.game}"

class CoolProgrammer(Employee, Player):
    languange = "Python"
    def print_lang(self):
        print(self.languange)


shazzy = Employee("Shahzaib", 9494, "Student")
harryy = Employee("Harris", 994, "Programmer")

touqer = CoolProgrammer("Touqeer", "Shops")

print(touqer.name)

# class CoolProgrammer(Employee, Player):
#     language = "Python"
#     def print_lang(self):
#         print(self.language)
#
# harry = Employee("Hariss", 900, "Student")
# shazzy = Employee("Shahzaib", 908, "Programmer")
#
# touqer = Player("Touqeer", ["Shopkeeper"])
# jabar  = CoolProgrammer("Jabbar", 988, "Cool Programmer")
#
#
#     # det = jabar.printDetails()
#     # jabar.print_lang()
#     # print(det)
# print(jabar.var)