
def hasDuplicate(nums):
    return len(set(nums)) < len(nums)


# Test case
nums = [2, 7, 11, 15]
answer = hasDuplicate(nums)
print(f"The boolean value for {nums} is {answer}")