def hasDuplicate(nums):
        for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                        if nums[i] == nums[j]:
                                return True
        return False

nums = [1,2,2,3]
result = hasDuplicate(nums)
print(f"The array of {nums} has a duplicate result: {result}")
