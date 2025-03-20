def fizzBuzz():
    i = 1

    while i <= 100:
        if i % 3 == 0:
            print("Fizz\n")
            if i % 5 == 0:
                print("Buzz\n")
        elif i % 5 == 0:
            print("Buzz\n")
        else:
            print(i, "\n")

        i += 1


if __name__ == "__main__":
    fizzBuzz()
