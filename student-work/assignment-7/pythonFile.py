#!/usr/bin/env python

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


# Test cases
test = Solution()
listOfTestCases = [1000, 111, 101, 123, 12321, 123321, 1234321, 1234322, 12343212, 12343213, 123432123, 123432124]
for i in listOfTestCases:
    print(f"Input: {i}, Output: {test.isPalindrome(i)}")
