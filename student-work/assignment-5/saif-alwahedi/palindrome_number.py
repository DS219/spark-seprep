def is_palindrome(x):
    if x < 0:
        return False

    original = x
    reversed_num = 0

    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x = x // 10

    return original == reversed_num


# Test cases
print("121 ->", is_palindrome(121))    
print("-121 ->", is_palindrome(-121))   
