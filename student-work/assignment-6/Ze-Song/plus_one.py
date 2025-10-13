def plusOne(digits):
    """
    Given a list of digits representing a non-negative integer,
    increment the integer by one and return the result as a list of digits.
    """
    n = len(digits)

    # Traverse from last digit backwards
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0  # carry over

    # If all digits were 9 (like 999 -> 1000)
    return [1] + digits


# Test cases
print(plusOne([1, 2, 3]))  # [1, 2, 4]
print(plusOne([9, 9, 9]))  # [1, 0, 0, 0]
print(plusOne([4, 3, 2, 1]))  # [4, 3, 2, 2]