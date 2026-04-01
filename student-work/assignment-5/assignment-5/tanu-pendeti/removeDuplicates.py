class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_numbers = sorted(set(nums))
        nums[:len(unique_numbers)] = unique_numbers
        return len(unique_numbers)

    #test case
    nums = [4,4,7]
    result = removeDuplicates(nums)
    print(result)

