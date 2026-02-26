class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        checkS = {}
        checkT = {}
        for i in range(len(s)):
            checkS[s[i]] = checkS.get(s[i], 0) + 1
            checkT[t[i]] = checkT.get(t[i], 0) + 1
        return checkS == checkT
    
"""
Input: s = "racecar", t = "carrace"

Output: true
"""