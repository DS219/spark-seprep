# SangHyup Lee

Hi! My favorite programming language is Python because it is simple, powerful, and great for data analysis and backend development.

## Example code

```python
import random

def generate_password(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(random.choice(chars) for _ in range(length))


if __name__ == "__main__":
    password = generate_password(12)
    print("Generated Password:", password)


### Code Explanation

This program defines a function that generates a random password using letters and numbers.

The generate_password function selects random characters from a predefined string and combines them into a password of a specified length.

When executed, the script generates a 12-character password and prints it to the console.