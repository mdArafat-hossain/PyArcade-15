import random
print("Welcome to Guess the Number Game!".center(50, " "))

def input_validation(value):
    while True:
        try:
            number = int(input(value))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


while True:
    attempt_count = 0
    print("Set your game range 🎯")
    minimum_number = input_validation("Enter the minimum number: ")
    while True:
        maximum_number = input_validation("Enter the maximum number: ")
        if maximum_number <= minimum_number:
            print("Maximum number must be greater than minimum number. Please try again.")
        else:
            break

    random_number = random.randint(minimum_number, maximum_number)
    while True:
        user_guess = input_validation(f"Guess a number between {minimum_number} and {maximum_number}: ")
        attempt_count += 1

        if user_guess < random_number:
            print(f"The number is Greater than {user_guess}.")
        elif user_guess > random_number:
            print(f"The number is Less than {user_guess}.")
        else:            
            print(f"\nCongratulations! You took {attempt_count} attempts to guess the number {random_number} correctly.")
            break
    exit_choice = input("\nDo you want to play again? (Press N to Exit): ").strip().lower()
    if exit_choice == 'n':
        print("Thank you for playing!\n")
        break