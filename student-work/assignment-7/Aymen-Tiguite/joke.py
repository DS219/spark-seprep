Python 3.10.10 (v3.10.10:aad5f6a891, Feb  7 2023, 08:47:40) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... # List of jokes
... jokes = [
...     "Why don't skeletons fight each other? They don't have the guts.",
...     "Why did the scarecrow win an award? Because he was outstanding in his field.",
...     "Why don't programmers like nature? It has too many bugs.",
...     "What do you call fake spaghetti? An impasta.",
...     "Why can't you trust an atom? Because they make up everything!",
...     "What did one ocean say to the other ocean? Nothing, they just waved.",
...     "Why was the math book sad? It had too many problems."
... ]
... 
... # Function to get a random joke
... def tell_joke():
...     return random.choice(jokes)
... 
... # Print a random joke
