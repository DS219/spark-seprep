def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            stack.append(char)
    
    return not stack

# Test
print(is_valid("()[]{}"))
print(is_valid("([)]"))
print(is_valid("{[]}"))
