ind = []
for i in range(len(nums)):
if target - nums[i] in nums[:i]:
    ind = [i, (nums.index(target-nums[i]))]
    return ind
