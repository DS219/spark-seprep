def is_palindrome(x):
    # Negative numbers are not palindromes
    if x < 0:
        return False
    
    return str(x) == str(x)[::-1]


# Test case
num = 121
result = is_palindrome(num)
print(f"Is {num} a palindrome? {result}")


