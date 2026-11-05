import random


def flip_coins(flips=100):
    # random.choice picks True (Heads) or False (Tails)
    heads = sum(random.choice([True, False]) for _ in range(flips))
    tails = flips - heads

    print(f"Flipped a coin {flips} times!")
    print(f"Heads: {heads}")
    print(f"Tails: {tails}")


if __name__ == "__main__":
    flip_coins()
