import random
secret_number=7
attempts = 0

while True: 
    try: 
        guess = int(input(" guess a number between 1 to 100: "))
        attempts += 1

        if guess < secret_number:
            print("too low, try again: ")
        elif guess > secret_number:
            print("too high, try again: ")
        else: 
            print(f"correct! you guess after {attempts} attempts.")
            break
    except ValueError:
        print("thats not a valid number, try again")

        
    