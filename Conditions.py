var1 = 5
var2 = 4
print("Enter the Number: ")
var3 = int(input())

if var1>var3:
    print("Greater")
elif var1==var3:
    print("Equal")
else:
    print("Less than")

list = [5,6,7,8]
# True or False
print(15 in list)
if 5 in list:
    print("Yes 5 is in the list")

print("Enter your Age: ")
age = int(input())
if age>18 and age<80:
    print("Yu are Ready to Drive")
elif age==18:
    print("Your age equal 18 You Must need make you driving licence")
elif age>80:
    print("You are out of age")
else:
    print("You are under age")
