def isPalindrome(self, x):
        
    x = str(x)
    comp = ""
    for i in x[::-1]:
        comp+=i
    if comp==x:
        return True