
import random

secret_number = random.randint(1, 20)
attempts = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 20.")
print("You have 5 attempts to guess it!")

for attempt in range(1, attempts + 1):
    while True:
        try:
            guess = int(input(f"\nAttempt {attempt}: Enter your guess: "))
            break
        except ValueError:
            print("Please enter a valid whole number.")

    if guess == secret_number:
        print("Congratulations! You guessed correctly!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
else:
    print(f"\nGame over! The number was {secret_number}.")

print("Thanks for playing!")
