def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False

    return not stack

# Test case
s = "()[]{}"
result = isValid(s)
print(f"Is the string \"{s}\" valid? {result}")
