# Given a string s consisting of words and spaces, 
# return the length of the last word in the string.
#A word is a maximal substring consisting of non-space characters only
# Example:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Solution 

def lengthOfLastWord(s: str) -> int:
        words = []
        for i in s.strip().split(" "):
            words.append(i)
        return len(words[-1])

# Test Case
s = "To be honest"
print(f"The word honest has {lengthOfLastWord(s)} letters")