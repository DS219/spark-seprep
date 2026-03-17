def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s)-1
        while(i<j):
            while i < j and not (self.alnum(s[i])):
                i = i+1
            while j > i and not (self.alnum(s[j])):
                j = j-1
            if s[i] != s[j]:
                return False
            i = i+1
            j = j-1
        return True
def alnum(self, ch):
    if ((ord("a") <= ord(ch) <= ord("z")) or
        (ord("0") <= ord(ch) <= ord("9"))):
        return True
    return False

# Test Case
s = "A man, a plan, a canal: Panama"
print(isPalindrome(None, s))