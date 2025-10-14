def add_two_number(l1, l2):
    carry=0
    output=[]
    i = 0
    while i < len(l1) or i < len(l2) or carry:
        val1 = l1[i] if i < len(l1) else 0
        val2 = l2[i] if i < len(l2) else 0

        total = val1 + val2 + carry
        carry = total // 10
        output.append(total % 10)
        i += 1

    return output
# Test case
l1= [2, 4, 3]
l2= [5, 6, 4]
result = add_two_number(l1, l2)
print(f"The linked list resulted from l1 and l2 is {result}")