def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def main():
    limit = 50
    primes = [n for n in range(2, limit + 1) if is_prime(n)]

    print("Devin Barnett - Assignment 4")
    print("Prime Number Explorer")
    print(f"Prime numbers from 2 through {limit}:")
    print(", ".join(str(n) for n in primes))
    print(f"Total primes found: {len(primes)}")


if __name__ == "__main__":
    main()
