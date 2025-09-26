# Sofia Felan
Hi, my name is Sofia Felan and my favorite programming language is Python because it is the first one I learned and easy to understand.

## Example code
```
import random

def guessing_game():
    secret_number = random.randint(1, 10)
    low = 1
    high = 10
    guess = int(input(f"Guess a number between {low} and {high}: "))
    while guess != secret_number:
        if guess > secret_number:
            high = guess - 1
            guess = int(input(f"Too high! Guess a number between {low} and {high}: "))
        elif guess < secret_number:
            low = guess + 1
            guess = int(input(f"Too low! Guess a number between {low} and {high}: "))
    print(f"You guessed it! The secret number was {secret_number}.")
```

### Code Explanation
This is a function that when executed, will ask for a number input until the random secret number is guessed. You can execute in a Python environment such as Jupyter Notebook or Google Colab by copying the above code and then running `guessing_game()`.
