def is_palindrome(x):
    # A negative number cannot be a palindrome
    if x < 0:
        return False
    # Convert the number to a string and check if it's equal to its reverse
    return str(x) == str(x)[::-1]

# Test case
num = 121
result = is_palindrome(num)
print(f"Is {num} a palindrome? {result}")
