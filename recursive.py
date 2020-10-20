# def factorial_iterative(n):
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
#
# def factorail_resursive(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorail_resursive(n-1)
#
# num = int(input("Enter The Number: "))
# print("Factorial Using iterative Method ", factorial_iterative(num))
# print("Factorial Using Factorial Method ", factorail_resursive(num))

def fibonacii(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacii(n-1)+fibonacii(n-2)

num = int(input("Enter the number: "))
print(fibonacii(num))