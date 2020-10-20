# # if 6 > 7:
# #     print("six is greater than 2")
# # if 6 < 7:
# #     print("Six is Lessthan 7")
# # else:
# #     print("Incorrect")
#
#
# # x = "Shahzaib"
# # y = 47
# # print(x,y)
#
#
#
# # x = "awesome"
# #
# # def myfunc():
# #   x = "fantastic"
# #   print("Python is " + x)
# #
# # myfunc()
# #
# # print("Python is " + x)
#
#
# # x = 1
# # y = 2.2
# # z = 1j
# # a = float(x)
# # b = int(y)
# # c = complex(z)
# # print(a,b,c)
# # print(type(a))
# # print(type(b))
# # print(type(c))
#
# x = int(1)
# y = int(2.45)
# z = int(00.2)
# print(x,y,z)
#
# # a = "Shahzaib Rind"
# # print(a.strip())
#
#
# print("\t\t\tWelcome To Bank Management\n\n")
#
# print("1 for New Account: ")
# print("2 for Deposit Money: ")
# print("3 for Withdraw Money: ")
# print("4 for Account Details: ")
# print("0 for Exit: \n")
#
#
# choice = int(input("Choose Number: "))
#
# if choice == 1:
#     print("\t\nWelcome to Create New Account..\n")
#     name = input("Enter your Name: ")
#     addr = input("Enter Your Address: ")
#     accnum = int(input("Enter your Account Num: "))
#     accpin = int(input("Enter Your Account PIN: "))
#     print("\nAccount Created Successfully...")
#
# elif choice == 2:
#     print("\n\tWelcome to Withdraw Money..")
#
# elif choice == 3:
#     print("\n\tWelcome to Deposit Money..")
#
# elif choice == 4:
#     print("\n\tWelcome to Account Details")
# elif choice == 0:
#     print(exit())
#
# else:
#     print("Invalid Input!!")



class Employee:
    no_of_emp = 0
    raise_amount = 1.2
    no_of_leaves = 0

    def __init__(self, first, last, sal, role):
        self.first = first
        self.last = last
        self.sal = sal
        self.role = role
        # self.email = f'{self.first}.{self.last}@yahoo.com'

        Employee.no_of_emp += 1

    def fullname(self):
        return self.first + ' ' + self.last

    def print_emp_details(self):
        return f'My Name is: {self.first} {self.last} My Salary is: {self.sal} and Role is: {self.role}'
    @property
    def email(self):
        if self.first == None or self.last == None:
            return 'Please Set the Email. Email is not set'
        return f'{self.first}{self.last}@yahoo.com'

    @classmethod
    def add_amount(cls, amount):
         cls.add_amount(amount)

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves


class Manager(Employee):
    lang = 'Python'

    def pro_lang(self):
        print(self.lang)

    def __init__(self, first, last, sal, underEmp):
        self.last = last
        self.first = first
        self.sal = sal
        self.unEm= underEmp

    def Mana_Det(self):
        return f'Manager Name is: {self.first} {self.last}Salary is: {self.sal} and Working Under Manager: {self.unEm}'


shahzaib = Employee('Shahzaib', 'rind', 300, 'student')
miraj = Employee('Miraj', 'khan', 400, 'Programmer')
touqer= Employee('Touqeer', 'Siraj', 200, 'Shop kepper')
jabar = Manager('Abdul', 'jabbar', 1000, Employee.no_of_emp)

print('Name: ', shahzaib.fullname())
print('Salary is: ', shahzaib.sal)

shahzaib.change_leaves(23)

print(shahzaib.print_emp_details())
print('No of Leaves: ', shahzaib.no_of_leaves)
print('Name: ', miraj.fullname())


print('Total Employees: ', Employee.no_of_emp)
print('Manager Details: ', jabar.Mana_Det())
print('Manager Email is: ', jabar.email)
print('Shahzaibs Email is: ', shahzaib.email)
jabar.change_leaves(25)
print("Total Leaves of Manager in one year is: ", jabar.no_of_leaves)
print(jabar.lang)