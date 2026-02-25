def is_palindrome(x):
    # Negative numbers cannot be palindromes
    if x < 0:
        return False

    # Convert number to string
    num_str = str(x)

    # Compare string with its reverse
    return num_str == num_str[::-1]


# Test cases
numbers = [121, -121, 10, 1331]

for num in numbers:
    print(f"{num} -> {is_palindrome(num)}")