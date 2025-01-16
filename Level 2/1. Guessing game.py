import random

def guessing_game():
    name = input("Type in your name: ")
    print(f"Hello, {name}! Welcome to the Guessing Game.")
    print("I am thinking of a number between 1 and 100.")
    print("Can you guess what it is? Keep guessing until you're correct!")

    # Generate a random number
    guess = random.randint(1, 100)

    while True:
        try:
            user_input = int(input("Take a guess: "))

            if user_input < 1 or user_input > 100:
                print("Invalid input! Please pick a number between 1 and 100.")
                continue

            if user_input == guess:
                print(f"Good job, {name}! You guessed the number correctly!")
                break
            elif user_input > guess:
                print("Your guess is too high.")
            else:
                print("Your guess is too low.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Run the game
guessing_game()
