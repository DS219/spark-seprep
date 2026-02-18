# Jack He

Hey, my name is Jack He and my favorite programming language is Python because of it's simplicity and versatility. It can be used for anything, from technical interviews to the backend of websites.

## Example Code

```
def squareNumbers(numbers):

    squares = []

    for num in numbers:
        squares.append(num**2)

    return squares

def main():
    list = [1, 2, 3]

    print(squareNumbers(list))

if __name__ == "__main__":
    main()
```

### Code Explanation

The following code exerpt is a function that takes in an argument of a list of numbers and squares them by raising each of the elements of the list by the second power to which each product gets appended to a list that's initally empty. The list gets returned with all of the elements of the original list being squared.

To run the following code from the terminal, copy the above to `squares.py` and run it with `python squares.py`. You must have Python installed to run it. See [Python install page](https://www.python.org/downloads/).
