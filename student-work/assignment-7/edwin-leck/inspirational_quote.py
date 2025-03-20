import random

# List of inspirational quotes
quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Innovation distinguishes between a leader and a follower. – Steve Jobs",
    "Your time is limited, don't waste it living someone else's life. – Steve Jobs",
    "Stay hungry, stay foolish. – Steve Jobs",
    "The best way to predict the future is to invent it. – Alan Kay",
    "Dream big and dare to fail. – Norman Vaughan",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt",
    "It always seems impossible until it's done. – Nelson Mandela",
    "Act as if what you do makes a difference. It does. – William James",
    "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "Strive not to be a success, but rather to be of value. – Albert Einstein"
]

# Function to generate and display a random quote
def generate_quote():
    # Randomly select a quote from the list
    random_quote = random.choice(quotes)
    # Print the quote with some formatting
    print("\n✨ Here's your inspirational quote for the day: ✨")
    print("-" * 50)
    print(random_quote)
    print("-" * 50)

# Run the function
if __name__ == "__main__":
    generate_quote()