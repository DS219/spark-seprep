class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        #Determine if an integer is a palindrome without converting to string.
        
        #Reverse the integer mathematically by extracting digits and comparing with the original value.
        
        #Time Complexity: O(log n) where n is the number of digits
        #Space Complexity: O(1)
        
        # Negative numbers are not palindromes
        # Numbers ending in 0 are not palindromes (except 0 itself)
        
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_num = 0
        while x > reversed_num:
            # Extract the last digit
            digit = x % 10
            # Build reversed number
            reversed_num = reversed_num * 10 + digit
            # Remove the last digit from x
            x //= 10
        
        # For even length numbers: x == reversed_num
        # For odd length numbers: x == reversed_num // 10 (middle digit doesn't matter)
        return x == reversed_num or x == reversed_num // 10


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (1, True),
        (1221, True),
        (12321, True),
        (1234, False),
        (9, True),
        (1001, True),
    ]
    
    print("Testing the code:\n")
    for x, expected in test_cases:
        result = solution.isPalindrome(x)
        status = "yay pass" if result == expected else "failed"
        print(f"{status} | Input: {x:6} | Output: {result:5} | Expected: {expected}")