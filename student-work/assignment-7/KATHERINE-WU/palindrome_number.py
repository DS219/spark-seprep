def palindrome_number(x):
    """
    :type x: int
    :rtype: bool
    """
    x_reversed = str(x)[::-1]
    if str(x) == x_reversed:
        return True
    return False

# Test case
x = int(input("Enter a number: "))
result = palindrome_number(x)
print(f"Is {x} a palindrome?: {result}")