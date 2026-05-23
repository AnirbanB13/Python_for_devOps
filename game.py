import random

def game():
    print("You are playing the game!")
    score = random.randint(1, 100)
    print(f"Your score {score}")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else: 
            hiscore = 0
    if score > hiscore or hiscore == "":
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
            print("Congratulations! You have the new high score!")
game()