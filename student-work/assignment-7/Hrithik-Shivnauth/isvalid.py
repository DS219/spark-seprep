def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:  # If it's a closing bracket
            top_element = stack.pop() if stack else '#'  # Get last open bracket
            if mapping[char] != top_element:
                return False  # Mismatch
        else:
            stack.append(char)  # Push open bracket

    return not stack  # If stack is empty, it's valid

# Test cases
test_cases = ["()", "()[]{}", "(]", "{[]}", "([)]"]
for s in test_cases:
    print(f"{s}: {is_valid(s)}")
