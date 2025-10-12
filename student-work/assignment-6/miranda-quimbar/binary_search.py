def binary_search(nums, target):
    left = 0
    right = len(nums) -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Test case
nums = [-1,0,3,5,9,12]
target = 9
result = binary_search(nums, target)
print(f"The index of {target} if found in nums: {result}")