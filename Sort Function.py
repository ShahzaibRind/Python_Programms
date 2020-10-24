# Take Second Element for Sor
def takeSecond(elem):
    return elem[1]
# Random List
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

#Sort List with key
random.sort(key=takeSecond)

# Print List
print("Sorted List: ", random)