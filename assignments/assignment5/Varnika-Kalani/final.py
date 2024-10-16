def is_palindrome(x: int) -> bool:
    if x < 0:  # Negative numbers are not palindromes
        return False
    
    original = x
    reversed_num = 0

    while x > 0:
        reversed_num = reversed_num * 10 + x % 10
        x = x // 10

    return original == reversed_num

# Example test case
x = 121
result = is_palindrome(x)
print(f"Is {x} a palindrome? {result}")
