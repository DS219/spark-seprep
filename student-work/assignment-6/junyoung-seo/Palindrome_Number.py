"""
Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""


def is_palindrome(x):
    # Negative numbers and numbers ending with 0 (except 0 itself) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        digit = x % 10
        reversed_half = reversed_half * 10 + digit
        x //= 10

    # Check even and odd length cases
    return x == reversed_half or x == reversed_half // 10


# Test cases
nums = [121, -121, 10, 0, 12321, 12345]

for n in nums:
    print(f"{n} → {is_palindrome(n)}")