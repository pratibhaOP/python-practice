import random

options = ["rock","paper","scissors"]
while True: 
    computer_choice = "scissors"
    user_choice =input("choose rock, paper or scissors: ").lower()

    if user_choice not in options:
        print("Invalid choice.Try again")
        continue
    print(f"computer choice {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "paper" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        
        print("You win!")
    else:
        print("You lose!")

    again = input("Play again? (y/n): ")
    if again.lower() not in ["y", "yes"]:
        print("Goodbye!")
        break


