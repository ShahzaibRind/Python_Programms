print("How many rows do you want print: ")
row = int(input())
print("Type 1 or 0")
con = int(input())
new = bool(con)
if new == True:
    for i in range(1,row+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new == False:
    for i in range(row,0,-1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()