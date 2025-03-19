#!/usr/bin/env python

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        my_list = []
        for d in str(x):
            my_list.append(int(d))
            
        reversed_list = my_list.copy()
        reversed_list.reverse()

        if my_list == reversed_list:
            return True
        else:
            return False

# Test cases
test = Solution()
x = [121, -121, 10]
for i in x:
    print(f"Input: {i}, Output: {test.isPalindrome(i)}")
