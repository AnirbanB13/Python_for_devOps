# 1 for snake, -1 for water, 0 for gun 

import random

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
Dict = {"snake": 1, "water": -1, "gun": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}
you = Dict[youstr]

if computer == you:
    print("It's a tie!")
elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
    print("You win!")
else:
    print("Computer wins!")

print(f"Computer chose: {reverseDict[computer]}, You chose: {reverseDict[you]}")