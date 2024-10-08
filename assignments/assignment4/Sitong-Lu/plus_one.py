# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1k6UV8kHDAJM_GlB80d5cRw8kzzUywiXl
"""

class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        
        # Start from the last digit and move backwards
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # If all digits are 9, we need to add an extra digit at the beginning
        return [1] + digits
