import re
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        seperate out string into sections
        find instances of repetition happening 1,2 or 3 times
        find instances of subtraction
        calculate values left-to-right based on seperated instances
        
        if digit index value is more than the next
        split substring of i and i+1
        else split substring of repeating digits
        """
        myDict={
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        value = 0
        s = s.replace('IV', 'IIII').replace('IX','VIIII')
        s = s.replace('XL','XXXX').replace('XC','LXXXX')
        s = s.replace('CD','CCCC').replace('CM','DCCCC')
        for letter in s:
            value += myDict[letter]
        return value
