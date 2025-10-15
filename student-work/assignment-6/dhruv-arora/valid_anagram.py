def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in t:
        if ch not in counts:
            return False
        counts[ch] -= 1
        if counts[ch] == 0:
            del counts[ch]
    return not counts

if __name__ == "__main__":
    tests = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("aacc", "ccac", False),
        ("", "", True),
    ]
    for s, t, expected in tests:
        got = is_anagram(s, t)
        print(f"is_anagram({s!r}, {t!r}) -> {got} (expected {expected})")
