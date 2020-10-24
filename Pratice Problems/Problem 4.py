'''
Author: Shahzaib Rind
Date: 12 August 2020
Purpose: Learning the Python
Problem Statement:-
A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:

676, 616, mom, 100001.

You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number. Your first input should be the number of test cases and then take all the cases as input from the user.

Input:
3

451

10

2133

Output:
Next palindrome for 451 is 454

Next palindrome for 10 is 11

Next palindrome for 2311 is 2222

These tasks will improve your logic making skills and logic is the basics of programming. The solution is
'''


def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':

    n = int(input("Enter the Number of test Cases: \n"))
    numbers = []

    for i in range(n):
        numb = int(input("Enter the Number: \n"))
        numbers.append(numb)
    print(numbers, "\n")

    for i in range(n):
        print(f"Next Palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")