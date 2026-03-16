def removeDuplicates(nums):
    unique_numbers = sorted(set(nums))
    nums[:len(unique_numbers)] = unique_numbers
    return len(unique_numbers)

nums = [4, 4, 7]
result = removeDuplicates(nums)
print(f"Array after removing duplicates: {nums[:result]}")
print(f"Number of unique elements: {result}")

