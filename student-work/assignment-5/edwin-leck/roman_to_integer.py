class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Mapping of Roman numerals to their integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # Get the value of the current symbol
            current_value = roman_to_int[s[i]]
            
            # If the current value is less than the next value, subtract it
            if i < n - 1 and current_value < roman_to_int[s[i + 1]]:
                total -= current_value
            else:
                total += current_value
        
        return total
    

solution = Solution()
print(solution.romanToInt("III"))       # Output: 3
print(solution.romanToInt("LVIII"))     # Output: 58
print(solution.romanToInt("MCMXCIV"))   # Output: 1994