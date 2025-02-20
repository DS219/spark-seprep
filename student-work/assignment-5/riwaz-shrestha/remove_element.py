def removeElement(nums, val):
  j=0
  for i in range(0, len(nums)):
    if nums[i] != val:
      nums[j] = nums[i]
      j+=1
  return j

# Test case
nums=[3,2,2,3]
val=3
result=removeElement(nums,val)
print(result, nums)
