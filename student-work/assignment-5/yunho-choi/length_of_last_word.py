def length_of_last_word(s: str) -> int:
    # Start from the end and skip trailing spaces
    i = len(s) - 1
    while i >= 0 and s[i] == " ":
        i -= 1

    # Count characters until we hit a space or the start
    length = 0
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1

    return length


# Simple test cases (optional but helpful)
if __name__ == "__main__":
    tests = [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
        ("a", 1),
        ("a ", 1),
        ("  ", 0),  # not in LeetCode constraints, but safe
    ]

    for s, expected in tests:
        got = length_of_last_word(s)
        print(f"input={s!r} -> {got} (expected {expected})")

