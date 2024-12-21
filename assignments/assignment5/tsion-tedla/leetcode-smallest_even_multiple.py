def smallest_even_multiple(n):
    if n % 2 == 0:
        return n
    else:
        return n * 2

# Test case
test_value = 6
result = smallest_even_multiple(test_value)
print(f"The smallest even multiple of {test_value} is {result}")
