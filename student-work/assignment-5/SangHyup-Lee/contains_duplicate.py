"""
LeetCode Easy Problem: Contains Duplicate (#217)

Problem:
Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.

Input:
nums = list of integers

Output:
True  -> if any duplicate exists
False -> if all elements are unique

Examples:

Example 1:
Input: nums = [1, 2, 3, 1]
Output: True

Example 2:
Input: nums = [1, 2, 3, 4]
Output: False

Example 3:
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: True
"""


def contains_duplicate(nums):
    """
    Checks whether the input list contains any duplicate values.

    Parameters:
        nums (list of int): list of integers

    Returns:
        bool: True if duplicate exists, False otherwise
    """

    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False  