def isPalindrome(x):
    if(x<0):
        return False
    x=str(x)
    return True if False not in [False for i in range(len(x)//2) if x[i]!=x[len(x)-i-1] ] else False 
    #list comprehension is the enemy of readability and the friend of fun
