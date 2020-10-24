# i =
# while(True):
#     i = i+1
#     continue
# print(i+1, end=" ")
# if(i==44):
#     break
# i= i+1

while True:
    inp = int(input("Enter the Number: \n"))
    if inp>100:
        print("Congrats You Have Won\n")
        break
    else:
        print("Try Again\n")
        continue
