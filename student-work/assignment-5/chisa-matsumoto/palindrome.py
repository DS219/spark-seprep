def palindrome(x):
    og = str(x)
    reverse = og[::-1]
    return og == reverse

#test
x = 121  
result = palindrome(x)
print(f"{x} is a palindrome: {result}")

x = -121  
result = palindrome(x)
print(f"{x} is a palindrome: {result}")
