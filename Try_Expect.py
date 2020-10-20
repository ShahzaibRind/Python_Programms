print("Please Enter num 1: ")
a = input()
print("Please Enter num 2: ")
b = input()
try:
    print("Sum of Two Numbers: ", int(a)+int(b))
except Exception as e:
    print(e)

print("This Line is Very Important")