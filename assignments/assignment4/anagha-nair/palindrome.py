class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        if x_str == x_str[::-1]:
            return True

        else:
            return False
        
solution = Solution()

# Test case
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))