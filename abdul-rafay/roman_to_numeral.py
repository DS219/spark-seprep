class Solution:
    def romanToInt(self, s: str) -> int:
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
        n = len(s)

        for i in range(n - 1):
            current_value = roman_values[s[i]]
            next_value = roman_values[s[i+1]]

            if current_value < next_value:
                total -= current_value
            else:
                total += current_value
        total += roman_values[s[n-1]]

        return total
    

if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("I", 1),
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        ("DCXXI", 621),
        ("MDCCCLXXXIV", 1884),
        ("MMMCMXCIX", 3999)
    ]

    print("Running tests for romanToInt function:")
    for roman_numeral, expected_int in test_cases:
        actual_int = sol.romanToInt(roman_numeral)
        print(f"Input: '{roman_numeral}', Expected: {expected_int}, Got: {actual_int}", end=" ")
        if actual_int == expected_int:
            print("[PASS]")
        else:
            print(f"[FAIL] - Expected {expected_int}, but got {actual_int}")
