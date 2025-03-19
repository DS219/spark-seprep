import random

def get_joke():
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta.",
        "Why don’t oysters share their pearls? Because they’re shellfish.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why don’t some couples go to the gym? Because some relationships don’t work out."
    ]
    return random.choice(jokes)

if __name__ == "__main__":
    print(get_joke())
