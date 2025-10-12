def romanToInt(s: str) -> int:
    # Mapping of Roman numerals to integer values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    # Traverse the string from right to left
    for char in reversed(s):
        value = roman_values[char]

        # Subtract if the current value is smaller than the previous value
        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return total


# Example test cases
if __name__ == "__main__":
    print(romanToInt("III"))      # Output: 3
    print(romanToInt("LVIII"))    # Output: 58
    print(romanToInt("MCMXCIV"))  # Output: 1994
