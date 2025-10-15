def palindrome(x):
      if x > 0 and x <= 2**31 -1:
         return str(x) == str(x)[::-1]
      else:
         return False

# Test case
num = 121
result = palindrome(num)
print(f"{num} is a palindrome: {result}")