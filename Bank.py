import datetime
def gettime():
    return datetime.datetime.now()

print("\n--------------Welcome to Bank Al Shahzaib--------------\n")

print("1 for Create New Account")
print("2 for Deposit Money")
print("3 for Withdraw Money")
print("4 for View Your Account")
print("O for Exit")

choice = int(input("Enter a Number: "))
while choice in ['1', '2', '3', '4', '0']:

    if choice==1:
        print("--------------Welcome to Create New Account--------------\n")
        fs = input("Enter First Name: ")
        ls = input("Enter Last Name: ")
        num = input("Choose Account Number: ")
        pin = input("Enter Account PIN: ")

    with open("first.txt", "a") as op:
        op.write(str([str(gettime())]) + ": " + fs + ls + num + pin + "\n")
        print("Account Successfully Created...")
    if choice==2:
        print("--------------Deposit Money--------------\n")
    if choice==3:
        print("--------------Withdraw Money--------------\n")
    if choice==4:
        print("--------------View Account Details--------------\n")
        n = input("Enter Account Number: ")
        p = input("Enter Account PIN: ")

       #  if n==num and p == pin:
       # print("True")
    if choice==0:
        exit()
    else:
        print("Invalid!!!")