def roman_to_int(s):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    prev_value = 0

    for char in s:
        current_value = roman_values[char]
        if current_value > prev_value:
            # Subtraction case (e.g., IV or IX)
            result += current_value - 2 * prev_value
        else:
            result += current_value
        prev_value = current_value

    return result

# Test cases:
print(roman_to_int("III"))      # Output: 3
print(roman_to_int("IV"))       # Output: 4
print(roman_to_int("IX"))       # Output: 9
print(roman_to_int("LVIII"))    # Output: 58