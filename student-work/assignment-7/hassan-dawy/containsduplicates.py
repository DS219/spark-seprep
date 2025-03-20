def containsDuplicate(nums):

    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

    # Test cases
print(containsDuplicate([1,2,3,1]))  # True
print(containsDuplicate([1,2,3,4]))  # False
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # True
