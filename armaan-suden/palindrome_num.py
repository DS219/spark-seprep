def is_palindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    rev_half = 0
    while x > rev_half:
        rev_half = rev_half * 10 + (x % 10)
        x //= 10
    return x == rev_half or x == rev_half // 10

if __name__ == "__main__":
    tests = [121, -121, 10, 0, 1221, 12321, 1001, 123]
    for t in tests:
        print(f"x = {t:>6}  ->  {is_palindrome(t)}")

