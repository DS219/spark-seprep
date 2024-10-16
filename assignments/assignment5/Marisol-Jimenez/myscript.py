def is_palindrome(arr):
    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - 1 - i]:
            return False
    return True
