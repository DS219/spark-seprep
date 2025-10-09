class Solution(object):
    def contains_Duplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            
            else:
                seen.add(nums[i])

        return False



if __name__ == "__main__":
    # Given test cases
    tests = [
        ([1, 2, 3, 1], True),                    # Example 1
        ([1, 2, 3, 4], False),                   # Example 2
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),  # Example 3
    ]

    solution = Solution()
    for nums, expected in tests:
        got = solution.contains_Duplicate(nums)
        print(f"nums = {nums}\nexpected = {expected}, got = {got}\n")