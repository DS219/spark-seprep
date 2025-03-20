def remove_element(nums, val):
    for i in range(nums.count(val)):
        nums.remove(val)
    return len(nums)


# Test
list1 = [3, 2, 2, 3]
value = 3

print("Expected OP: 2", "Actual OP:", remove_element(list1, value), "list1:", list1)
