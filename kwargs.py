def funargs(normal, *args, **kwargs):
    print(normal)
    for item in shah:
        print(item)
    print("\nSome of Our Class heroes\n")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

shah = ["Shahzaib", "jabbar", "Touqeer","Miraj","Sohail"]
normal = "\nThe list of Peoples\n"
clas = {"Shahzaib":"Programmer", "Jabbar":"Freelancer", "Touqeer":"Bussinessman","Miraj":"Develper"}
funargs(normal, *shah, **clas)