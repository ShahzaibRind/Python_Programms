'''
Author: Shahzaib Rind
Date: 14 August 2020
Purpose: Learning the Python
Project: Guess The Number

 Problem Statement:-
Generate a random integer from a to b. You and your friend have to guess a number between two numbers a and b. a and b are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep choosing the number and your program must tell whether the number is greater than the actual number or less than the actual number. Log the number of trials it took your friend to arrive at the number. You play the same game and then the person with minimum number of trials wins! Randomly generate a number after taking a and b as input and don’t show that to the user.

Input:
Enter the value of a

4

Enter the value of b

13

Output:
Player1 :

Please guess the number between 4 and 13

5

Wrong guess a greater number again

8



Wrong guess a smaller number again

6

Correct you took 3 trials to guess the number

Player 2:

Correct you took 7 trials to guess the number

Player 1 wins!

Accepting a coding challenge is an excellent way to improve your coding skills. So, keep practicing and keep yourself up to date with codewithharry.


'''

import random


def guess_Game(a, b, actual):
    guess = int(input(f"Guess a number between {a} and {b}\n"))
    nguess = 1
    while guess < actual:
        if guess < actual:
            guess = int(input(f"Enter a bigger Number\n"))
            nguess += 1
        else:
            guess = int(input(f"Enter a Smaller number\n"))
            nguess +=1
    print(f"You guessed the number in {nguess} guesses\n")
    return nguess


if __name__ == '__main__':
    a = int(input("Enter the Value of a: \n"))
    b = int(input("Enter the Value of b: \n"))
    actual1 = random.randint(a, b)
    print("Player 1's Turn\n")
    g1 = guess_Game(a, b, actual1)
    print("Player 2's Turn\n")
    actual2 = random.randint(a, b)
    g2 = guess_Game(a, b, actual2)

    if g1 < g2:
        print("Congrats!! Player 1 Won the Match\n")
    elif g1 > g2:
        print("Congrats!! Player 2 Won the Match\n")
    else:
        print("Match Tied!!\n")
    print(f"The number for Player 1 was {actual1} and Player 2 was {actual2}")