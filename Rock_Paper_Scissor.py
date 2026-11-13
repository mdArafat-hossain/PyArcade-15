#Rock Paper Scissor Game
import random
print("Welcome to Rock Paper Scissor Game!".center(50, " "))
# rock < paper
# paper < scissor
# scissor < rock
winning_rules = {"rock" : "paper", "paper" : "scissor", "scissor" : "rock"}

while True:
    #inital scoring
    score_user = 0
    score_computer = 0

    while True:
    #How many Rounds User wants to play
        try:
            n = int(input("Round : "))
            if (n <= 0 ):
                print("It must be Greater then 0")
            else:
                break
        except ValueError:
            print("Invalid Choice")

    for rounds in range(1, n+1):
        #computer choice
        computer = random.choice(["rock", "paper", "scissor"])

        while True:        
            #user choice
            user = input("(Rock // Paper // Scissor) : ").strip().lower()
            if user in ["rock", "paper", "scissor"]:
                break
            else:
                print("Invalid Choice")

        print(f"Your choosed {user.capitalize()} and Computer choosed {computer.capitalize()}")
        if (computer == user):
            print("Draw")

        #if computer choose rock, user have to choose paper to win 
        elif (winning_rules[computer] == user):
            print("You Win")
            score_user += 1
        else:
            print("Computer Wins")
            score_computer += 1

    if (score_user > score_computer):
        print("\nYou Win the Game 🏆\n")
    elif (score_user < score_computer):
        print("\nComputer Wins the Game 🤖 \n")
    else:
        print("\nIts a Draw 🤝 \n")

    #exit choice
    exit_choice = input("\nPlay Again? (Press N to exit) : ").strip().lower()
    if (exit_choice == "n"):
        print("Thank you for playing!\n")
        break