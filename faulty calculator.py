x = int(input("Enter first Number"))
print("press + for Addition")
print("press - for subtraction")
print("press * for Multiplication")
print("press / for Division")
a = input()
y = int(input("Enter second Number"))
if a=="+" or a=="-" or a=="*" or a=="-":
    if a == "+":
        if x == 56 and y == 9:
            print(77)
        else:
            print(x + y)
    elif a == "-":
        print(x - y)
    elif a == "*":
        if x == 45 and y == 3:
            print(555)
        else:
            print(x * y)
    elif a == "/":
        if x == 56 and y == 6:
            print(4)
        else:
            print(x / y)
else:
    print("Invalid Input")