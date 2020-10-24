'''
Problem Statement:-
You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, based on their amount of calories. You have to reserve this list of food items containing calories.

You have to use the following three methods to reserve a list:

Inbuild method of python
List name [::-1] slicing trick
Swapping the first element with the last one and second element with second last one and so on like,
[6 7 8 34 5] -> [5 34 8 7 6]

Input:
Take a list as an input from the user

[5, 4, 1]

Output:
[1, 4, 5]

[1, 4, 5]

[1, 4, 5]

All three methods give the same results!


'''

# Python Practice Problem 3

# Take the Size of the list from the User
print("\n\tEnter the Number of the list one by one\n")

size = int(input("Enter the Size of the list: \n"))
# Initialize the Blank List
mylist = []

# Take the Input from the user one by one
for i in range(size):
    mylist.append(int(input("Enter List Element: \n")))

print(f"Your list is {mylist}\n")


reverse1 = mylist[:]
reverse1.reverse()

reverse2 = mylist[::-1]
print(f"My First Reversed List of {mylist} is: {reverse1}")
print(f"My Second Reversed List of {mylist} is: {reverse2}")

reverse3 = mylist[:]
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3) -i -1 ] = reverse3[len(reverse3) -i -1], reverse3[i]
    print(f"My Third Reversed List of {mylist} is: {reverse3}\n")
if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three Methods gives the Same Results...")