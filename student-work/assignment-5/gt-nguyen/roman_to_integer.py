def roman_to_int(s: str) -> int:
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    total = 0

    for i in range(len(s)):
        curr = values[s[i]]

        if i + 1 < len(s) and curr < values[s[i + 1]]:
            total -= curr
        else:
            total += curr

    return total


# Test cases
tests = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
for t in tests:
    print(f"{t} -> {roman_to_int(t)}")