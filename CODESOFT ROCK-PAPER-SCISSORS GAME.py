import random 
while True:
    print("\nRock-Paper-Scissors Game")
    user = input("choose rock , paper , or scissors:").lower()
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    print("You chose:",user)
    print("computer chose:", computer)
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
        (user == "paper" and computer == "rock" ) or \
        (user == "scissors" and computer == "paper"):
        print("You win!")
    else: 
        print("You lose!")
        again = input("play again? (yes/no):").lower()
        if again != "yes":
            print("Thanks for playing!")
            break