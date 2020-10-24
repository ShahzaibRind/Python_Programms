# name = input("Enter your name: ")
# caste = input("Enter your caste: ")
#
# if int(caste) == 0:
#     raise ZeroDivisionError("b is zero so stopping the program")
#
# if name.isnumeric():
#     raise Exception("Numbers are not Allowed!!!")
#
# print(f'Hello {name}')

c = input("Enter Some Things...")
try:
    print(a)

except Exception as e:
    if c == 'shazzy':
        raise ValueError("Shahzaib is Blocked with Tina")

    print("Exception Handled")