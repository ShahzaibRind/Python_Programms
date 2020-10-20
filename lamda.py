# Lamda Function or Ananymous Function
#
# def add(a,b):
#     return a+b
#
# minus = lambda x,y: x-y
#
# def minus(z,m):
#     return z-m
#
# print(minus(7,4))
# print(minus(3,2))

a = [[23,43], [4,5], [65,33]]
a.sort(key=lambda x: x[1])
print(a)

vowels = ['e', 'i', 'a', 'o', 'u']
vowels.sort(reverse=(True))
print(vowels)
