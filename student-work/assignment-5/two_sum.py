def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_map:
            return [num_map[diff], i]
        num_map[num] = i

# Test case
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(f"Indices of the two numbers that add up to {target}: {result}")
