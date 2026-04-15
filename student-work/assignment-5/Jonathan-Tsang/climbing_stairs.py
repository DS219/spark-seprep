def climbing_stairs(n):
    if n <= 2:
        return n
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr

print(climbing_stairs(2))   # 2
print(climbing_stairs(3))   # 3
print(climbing_stairs(10))  # 89
