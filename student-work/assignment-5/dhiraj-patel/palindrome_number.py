def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    x = str(x)
    for idx in range(0,len(x)):
        if x[idx] != x[len(x) - 1 - idx]:
            return False
    
    return True

# Test Case
x = 121
if isPalindrome(x) == True:
    print("Test passed")
else:
    print("Test failed")