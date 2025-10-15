from typing import List


def missing_number(nums: List[int]) -> int:
    length_of_numbers = len(nums)
    expected_sum = length_of_numbers * (length_of_numbers + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


if __name__ == "__main__":
    test_cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ]

    for numbers, expected in test_cases:
        result = missing_number(numbers)
        status = "OK" if result == expected else "FAIL"
        print(f"Input {numbers} | Missing {result} | Expected {expected} | {status}")


