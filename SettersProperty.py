class Employee:

    def __init__(self, fname , lname ):
        self.fname = fname
        self.lname = lname

    def Explain(self):
        return f"Employee Name is: {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set it using setters."
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print("\nSetting now...")
        names = string.split("@") [0]
        self.fname = names.split(".") [0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        print("\nDeleting Method Running....")
        self.fname = None
        self.lname = None


touqeer = Employee("Touqeer", "Siraj")
jabar = Employee("Abdul", "Jabbar")

print()
print(touqeer.email)

touqeer.fname = "Taimor"
print(touqeer.email)

touqeer.email = 'Shahzaib.rind@gmail.com'
print(touqeer.email)

del touqeer.email
print(touqeer.email)

touqeer.email = 'New.mail'
print(touqeer.email)

del touqeer.email
print(touqeer.email)