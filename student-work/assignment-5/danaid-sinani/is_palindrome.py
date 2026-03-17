def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        else:
	        return str(x) == str(x)[::-1]

# Test case
x = 121
result = isPalindrome(x)
print(f"Is {x} a palindrome? {result}")