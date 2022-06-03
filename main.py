import random
list = ["R", "P", "S"]
prompt =  ("Welcome to the Rock-Paper-Scissors gameplay!\n")
prompt += ("Select (R)ock, (P)aper, (S)cissors: ")
player = False
while player == False:
    player = input(prompt)
    cpu = random.choice(list)
    if player == cpu:
        print("Tie!")
        game = input("Play again? (Y/N): ")
        if game == "Y":
            player = False
        elif game == "N":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input!")
            break

    elif player == "R":
        if cpu == "P":
            print (f"Player {player} : CPU {cpu}")
            print("You lose!")
        else:
            print (f"Player {player} : CPU {cpu}")
            print("You win!")
    
    elif player == "P":
        if cpu == "S":
            print (f"Player {player} : CPU {cpu}")
            print("You lose!")
        else:
            print (f"Player {player} : CPU {cpu}")
            print("You win!")

    elif player == "S":
        if cpu == "R":
            print (f"Player {player} : CPU {cpu}")
            print("You Lose!")
        else:
            print (f"Player {player} : CPU {cpu}")
            print("You win!")

    else:
        print("Invalid input, try again.")
        game = input("Play again? (Y/N): ")
        if game == "Y":
            continue
        else:
            break
    player = False
print("Thanks for playing!")