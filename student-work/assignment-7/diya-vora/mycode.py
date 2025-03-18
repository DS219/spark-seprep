#!/usr/bin/env python3
def isPalindrome(x):
  y=str(x)
  z=""
  for i in range(len(y)):
    z=z+ y[-1]
    y=y[:-1]
    
  if z==str(x):
    print("This is a palindrome")
    return True
  else:
    print("This is not a palindrome")
    return False

test=isPalindrome(121)
