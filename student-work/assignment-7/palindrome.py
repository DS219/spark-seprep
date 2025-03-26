class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        n = x[::-1]
        if x == n:
            return True
        else:
            return False

# test       
num = 121
solution = Solution()
result = solution.isPalindrome(num)
print(f"Is {num} a palindrome? {result}")
