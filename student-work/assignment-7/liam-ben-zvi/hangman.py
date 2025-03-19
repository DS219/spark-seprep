import random

# List of words to choose from
words = ["cat", "dog", "sun", "hat", "pen", "cup"]

def play_hangman():
    # Pick a random word and set up variables
    word = random.choice(words).upper()
    word_letters = set(word)  # Letters in the word to guess
    guessed_letters = set()   # Letters guessed by the player
    tries = 6                 # Number of incorrect guesses allowed

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    # Game loop
    while tries > 0 and word_letters:
        # Show the current state
        print(f"\nTries left: {tries}")
        print("Guessed letters:", " ".join(guessed_letters))
        # Display word with underscores for unguessed letters
        display = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word:", " ".join(display))

        # Get player's guess
        guess = input("Guess a letter: ").upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (A-Z).")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            print("Good guess!")
            word_letters.remove(guess)
        else:
            print("Wrong guess!")
            tries -= 1

    # Game over: check if player won or lost
    if tries == 0:
        print("\nGame Over! You ran out of tries.")
        print("The word was:", word)
    else:
        print("\nYou win! The word was:", word)

# Run the game
play_hangman()
