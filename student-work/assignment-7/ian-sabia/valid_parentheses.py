def is_valid(s):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in matching:
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0


test_cases = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([])", True),
    ("([)]", False),
    ("{[]}", True),
    ("", True),
    ("((((", False),
]

print("Valid Parentheses - LeetCode #20")
print("=" * 40)

passed = 0
for s, expected in test_cases:
    result = is_valid(s)
    status = "PASS" if result == expected else "FAIL"
    if status == "PASS":
        passed += 1
    display = s if s else '""'
    print(f"  {status} | is_valid({display:10s}) = {str(result):5s} (expected {expected})")

print("=" * 40)
print(f"Results: {passed}/{len(test_cases)} tests passed")
