import random

def game(x):
    y = random.randint(1,10)
    if x == y:
        print("You win!")
    else:
        print("You lose!")
    if x > y:
        print("Your number was too high")
        print("The number was", y)
    else:
        print("Your number was too low")
        print("The number was", y)


print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 10")

x = int(input("What's your guess? "))
game(x)
