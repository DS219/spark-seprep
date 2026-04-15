def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    return [1] + digits


# Test case
digits = [9, 9, 9]
target = [1, 0, 0, 0]

result = plusOne(digits)

print("Input digits:", [9,9,9])
print("Expected output:", target)
print("Actual output:", result)
