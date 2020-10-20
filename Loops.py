# Print First 10 natural numbers using while loop
# i = 0
# while i <= 10:
#     print(i)
#     i+=1

# Print the following pattern
print("Second Number Pattern ")
lastNumber = 6
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")