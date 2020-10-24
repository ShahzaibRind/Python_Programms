# l = 10 # GLOBAL VARIABLE
# def fun1(n):
#     # l = 5 # Local Variable
#     m = 6 # Local Variable
#     global l
#     l = l+5
#     print(l,m)
#
#     print(n, "I am printing")
# fun1("This is me")
# #print(l)
age = 89
def shazzy():
    age = 20
    def jabbar():
        global age
        age = 88 # It will check if the if the age is the outside of the function or not
    print("Before Calling Jabbar ", age)
    jabbar()
    print("After Calling Jabbar ", age)
shazzy()
print(age)