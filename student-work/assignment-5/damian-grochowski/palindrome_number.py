def is_palindrome(x):
    if x < 0:
        return False
    s = str(x)
    return s == s[::-1]

# Test cases
print(is_palindrome(121))   # True
print(is_palindrome(-121))  # False
print(is_palindrome(10))    # False
