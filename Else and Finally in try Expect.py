f1 = open("first.txt")

try:
    f = open('does.txt')

except EOFError as e:
    print('Printed! EOF Error: ', e)

except IOError as e:
    print('Printed! IO Error: ', e)

else:
    print('This will run only when Except in not running...')
# This is used for Code Clean up
finally:
    print('Run this Anyway...')
    f1.close()

print('This Line is Important')