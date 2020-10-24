# List Comprehensions

ls = [i for i in range(100) if i % 3 == 0]
print('\n', ls)


# Dictionary Comprehensions

dict1 = {i: f'Item {i}' for i in range(5)}
dict2 = {value: key for key, value in dict1.items()}
print('\n', dict1)
print('\n', dict2)

# Set Comprehensions

dresses = {dress for dress in ["Dress1", "Dress2", "Dress1", "Dress2",
                               "Dress1", "Dress2", "Dress1", "Dress2"]}

print('\n', dresses)
# print(type(dresses))


# Generator Comprehensions
evens = (i for i in range(6) if i % 2 == 0)
print(type(evens))
for item in evens:
    print(item)
