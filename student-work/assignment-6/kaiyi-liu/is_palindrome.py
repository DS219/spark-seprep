def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    
    rev = 0
    num = x
    while num != 0:
        rev = rev * 10 + num % 10
        num //= 10
    
    return rev == x

# Test cases (similar to the two_sum example)
tests = [121, -121, 10, 0, 12321, 123]
for t in tests:
    result = is_palindrome(t)
    print(f"Is {t} a palindrome? {result}")
