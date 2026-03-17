def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Test case
s = ["h", "e", "l", "l", "o"]
reverse_string(s)
print(f"Reversed string: {s}")
