num = int(input("Enter 0 or 1: "))
if num==0:
    def pypart(n):
        for i in range(0,n):
            for j in range(0, i+1):
                print("* ", end="")
            print("\r")
if num==1:
    def pypart(n):
        for x in range(4,n):
            for y in range(4, x-1):
                print("* ", end=" ")
            print("\r")
else:
    print("Please Enter correct Number")
n = 4
pypart(n)

