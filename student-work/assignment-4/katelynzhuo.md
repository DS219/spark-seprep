#Katelyn Zhuo

Hi, my name is Katelyn Zhuo ans my favorite programing language is Python because Rust is hard.

## Example Code
'''
import random

def play_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

'''

### Code Explaination
This code plays a number guessing game, and it tells you if your guess is too low, too high, or correct.
