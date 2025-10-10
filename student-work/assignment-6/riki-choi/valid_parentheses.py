def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return not stack

# Test cases
test_cases = [
    "()",
    "()[]{}",
    "(]",
    "([)]",
    "{[]}"
]

for test in test_cases:
    result = is_valid(test)
    print(f"Input: '{test}' -> Output: {result}")