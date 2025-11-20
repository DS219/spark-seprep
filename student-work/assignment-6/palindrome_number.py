
def isPalindrome1(self, x):
    """
    :type x: int
    :rtype: bool
    """
    x = str(x)
    return x == x[::-1]

'''
Follow up: Could you solve it without converting the integer to a string?
'''    


def isPalindrome2(self, x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    half = 0
    while x > half:
        half = (half * 10) + (x % 10)
        x = x//10
    return x == half or x == half//10


# Test cases for isPalindrome1
print("Testing isPalindrome1...")

x = 121
result = isPalindrome1(None, x)
print(f"Is {x} a palindrome? {result}")  # Expected: True

x = -121
result = isPalindrome1(None, x)
print(f"Is {x} a palindrome? {result}")  # Expected: False

x = 10
result = isPalindrome1(None, x)
print(f"Is {x} a palindrome? {result}")  # Expected: False

x = 0
result = isPalindrome1(None, x)
print(f"Is {x} a palindrome? {result}")  # Expected: True

x = 12321
result = isPalindrome1(None, x)
print(f"Is {x} a palindrome? {result}")  # Expected: True

x = 1001
result = isPalindrome1(None, x)
print(f"Is {x} a palindrome? {result}")  # Expected: True


# Test cases for isPalindrome2

print("\nTesting isPalindrome2...")

x = 121
result = isPalindrome2(None, x)
print(f"Is {x} a palindrome? {result}")  # Expected: True

x = -121
result = isPalindrome2(None, x)
print(f"Is {x} a palindrome? {result}")  # Expected: False

x = 10
result = isPalindrome2(None, x)
print(f"Is {x} a palindrome? {result}")  # Expected: False

x = 0
result = isPalindrome2(None, x)
print(f"Is {x} a palindrome? {result}")  # Expected: True

x = 12321
result = isPalindrome2(None, x)
print(f"Is {x} a palindrome? {result}")  # Expected: True

x = 1001
result = isPalindrome2(None, x)
print(f"Is {x} a palindrome? {result}")  # Expected: True




Added solutions for LeetCode's 'Palindrome Number' problem

- Implemented two functions, isPalindrome1 and isPalindrome2, to check if an integer is a palindrome.
- isPalindrome1 converts the integer to a string and compares it with its reverse.
- isPalindrome2 avoids string conversion by reversing half of the number and comparing it with the other half.
- Added comprehensive test cases for both methods, including edge cases like negative numbers, zeros, and numbers ending in zero.
- Verified correctness with sample inputs: 121, -121, 10, 0, 12321, and 1001.
