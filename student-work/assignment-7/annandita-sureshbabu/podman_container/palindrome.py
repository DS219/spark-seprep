def palindrome(number):
    if number < 0:
        return False
    num = str(number)
    if num == num[::-1]:
        return True
    return False

number = int(input("Enter a number: "))
if palindrome(number):
    print(f"{number} is a palindrome!")
else:
    print(f"{number} is not a palindrome!")
