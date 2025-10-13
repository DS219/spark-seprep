def isPalindrome(x):
        return str(x) == str(x)[::-1]

# Test Case
test1 = 121
print(f"input 121, expect True, result: {isPalindrome(test1)}")

test2 = -121
print(f"input -121, expect False, result: {isPalindrome(test2)}")
