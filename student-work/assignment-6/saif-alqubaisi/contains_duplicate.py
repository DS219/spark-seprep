"""
LeetCode Easy: Contains Duplicate (LC 217)
Author: Saif Alqubaisi
Approach: Use a set to detect duplicates in O(n) time, O(n) space.
"""

from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False

if __name__ == "__main__":
    print("Test 1:", contains_duplicate([1,2,3,1]))         # True
    print("Test 2:", contains_duplicate([1,2,3,4]))         # False
    print("Test 3:", contains_duplicate([1,1,1,3,3,4,3,2,4,2]))  # True

