import random

print("********Lets play Rock, Paper and Scissor*********\n")

user_score = 0
comp_score = 0
ties = 0

name = input("Enter your name: ")
print("\n****Let me tell you the winning rules of the game*******\n")
print("Paper v/s Rock ----> Paper win")
print("Paper v/s Scissor ----> Scissor win")
print("Scissor v/s Rock ----> Rock win")

play = input("\nDo you want to play this game (Type 'Yes' or 'No') : ")

print("\n******Lets start the game*******\n")


def gameWin(comp,user,user_score,comp_score,ties):
    if(comp == "Rock" and user == 1):
        ties = ties + 1
        print("Match Tied")
        print("Your score: ", user_score)
        print("Computer score: ", comp_score)
    elif(comp == "Rock" and user == 2):
        user_score = user_score + 1
        print("You won")
        print("Your score: ", user_score)
        print("Computer score: ", comp_score)
    elif(comp == "Rock" and user == 3):
        comp_score = comp_score + 1
        print("You loose")
        print("Your score: ", user_score)
        print("Computer score: ", comp_score)


    if(comp == "Paper" and user == 2):
        ties = ties + 1
        print("Match Tied")
        print("Your score: ", user_score)
        print("Computer score: ", comp_score)
    elif(comp == "Paper" and user == 1):
        comp_score = comp_score + 1
        print("You loose")
        print("Your score: ", user_score)
        print("Computer score: ", comp_score)
    elif(comp == "Paper" and user == 3):
        user_score = user_score + 1
        print("You won")
        print("Your score: ", user_score)
        print("Computer score: ", comp_score)


    if(comp == "Scissor" and user == 3):
        ties = ties + 1
        print("Match Tied")
        print("Your score: ", user_score)
        print("Computer score: ", comp_score)
    elif(comp == "Scissor" and user == 1):
        user_score = user_score + 1
        print("You won")
        print("Your score: ", user_score)
        print("Computer score: ", comp_score)
    elif(comp == "Scissor" and user == 2):
        comp_score = comp_score + 1
        print("You loose")
        print("Your score: ", user_score)
        print("Computer score: ", comp_score)

    print("Choose a valid option ")


while(play != "No"):

    print("Computer's turn: Rock(s), Paper(p), Scissor(s)\n")
    comp = random.randint(1, 3)
    if (comp == 1):
        comp = "Rock"
    elif (comp == 2):
        comp = "Paper"
    elif (comp == 3):
        comp = "Scissor"

    print("Computer has chosen its option\n")
    print(name, "Your turn:\n")
    print("Type 1 to choose Rock")
    print("Type 2 to choose Paper")
    print("Type 3 to choose Scissors")

    user = int(input("\nChoose your option: "))

    print("Computer choose: ",comp)

    if(user == 1):
        print("You choose: Rock\n")
    elif(user == 2):
        print("You choose : Paper\n")
    elif(user == 3):
        print("You choose: Scissor\n")

    gameWin(comp,user,user_score,comp_score,ties)

    play = input("\nDo you want to play this game again (Type 'Yes' or 'No') : ")


print("*******\nGAME OVER, THANKS FOR PLAYING********")