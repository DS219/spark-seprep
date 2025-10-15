class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # convert to string and then compare
        s = str(x)
        return(s == s[::-1])

# Test Case
test = 1221
solution_instance = Solution() # Create an instance of the Solution class
result = solution_instance.isPalindrome(test) # Call the method on the instance
print('The result of the test for', test, 'is', result)