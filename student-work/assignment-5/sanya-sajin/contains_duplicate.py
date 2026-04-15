def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Test case
nums = [1, 2, 3, 4, 1]
result = contains_duplicate(nums)
print(f"Contains duplicate: {result}")
