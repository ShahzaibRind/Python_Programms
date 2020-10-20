# Built In Function
# a = 5
# b = 6
# c = sum((a,b))
# print(c)

def func1(a,b):
    print("You are in the Function 1: ", a+b)
def func2(a,b):
    """This Function will calculate the two Numbers"""
    average = (a+b)/2
    return average

# v = func2(1,2)
# print(v)
print(func2.__doc__)