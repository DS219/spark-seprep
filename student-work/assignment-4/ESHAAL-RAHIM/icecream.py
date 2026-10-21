import random

def main():
    flavors = ["Vanilla", "Chocolate", "Barf", "Mixed Berry"]
    toppings = ["Chocolate Chips", "Fruit", "Nuts", "Insects", "Caramel"]

    randomFlavor = random.choice(flavors)
    randomTopping = random.choice(toppings)

    print(f"Your ice cream is {randomFlavor} with {randomTopping}!")

main()
