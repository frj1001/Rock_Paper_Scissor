import random

winning = False

while winning==False:
    player1 = input("Hi Player enter your choice: ")
    computer = random.choice(["rock", "paper", "scissor"])
    print(computer)

    if(player1 == "rock" and computer == "scissor"):
        print("Player1 won")
        winning = True

    elif(player1 == "paper" and computer == "rock"):
        print("Player1 won")
        winning = True

    elif(player1 == "scissor" and computer == "paper"):
        print("Player1 won")
        winning = True

    elif(player1 == "rock" and computer == "paper"):
        print("Computer won")

    elif(player1 == "paper" and computer == "scissor"):
        print("Computer won")

    elif(player1 == "scissor" and computer == "rock"):
        print("Computer won")

    elif(player1 == computer):
        print("Draw")

    else:
        print("Enter in lower case or wrong input")