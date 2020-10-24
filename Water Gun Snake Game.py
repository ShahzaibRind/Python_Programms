import random

lst = ["s","w","g"]

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print("\t\t\tWelCome to Snake Water Gun Game\n")
print("s for Snake\nw for Water \ng for Gun")

while no_of_chance < chance:
    _input = input("Snake, Water, Gun: ")
    _random = random.choice(lst)

    if _input == _random:
        print("Tied, 0 to each \n")

    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"Your Guees {_input} and computer guess is {_random} \n")
        print("Computer Wins 1 Point \n")
        print(f"Computer Point is {computer_point} and your point is {human_point} \n")

    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print(f"Your Guees {_input} and computer guess is {_random} \n")
        print("Human Wins 1 Point \n")
        print(f"Computer Point is {computer_point} and your point is {human_point} \n")

    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"Your Guees {_input} and computer guess is {_random} \n")
        print("Computer Wins 1 Point \n")
        print(f"Computer Point is {computer_point} and your point is {human_point} \n")

    elif _input == "w" and _random == "g":
        human_point = human_point + 1
        print(f"Your Guees {_input} and computer guess is {_random} \n")
        print("Human Wins 1 Point \n")
        print(f"Computer Point is {computer_point} and your point is {human_point} \n")

    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print(f"Your Guees {_input} and computer guess is {_random} \n")
        print("Human Wins 1 Point \n")
        print(f"Computer Point is {computer_point} and your point is {human_point} \n")

    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"Your Guees {_input} and computer guess is {_random} \n")
        print("Computer Wins 1 Point \n")
        print(f"Computer Point is {computer_point} and your point is {human_point} \n")

    else:
        print("Your input is Invalid!!")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game Over")
if computer_point == human_point:
        print("Game Tied")
elif computer_point > human_point:
        print("Computer won you loose")
else:
    print("Human Won by Computer")

    print(f"Your Point is {human_point} and computer Point is {computer_point}")
