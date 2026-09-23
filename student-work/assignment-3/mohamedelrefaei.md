# Mohamed Elrefaei
Hey, I'm Mohamed Elrefaei. I'm a junior at BU in Data Science, and my favorite programming language is Python, as it's the first one I learned.
## Example code
``` 
# Defining first function
def calc(number_1, number_2):
    number_3 = number_1 + number_2
    number_4 = number_3 ** number_2
    number_5 = round(number_4 * number_1 / number_2)
    number_6 = round(number_5 - number_3 + number_4)
    print("This is the calc function:", number_3, number_4, number_5, number_6)

# Defining second function
def type_change():
    string = "Calc is short for calculator I'm just using slang guys"
    integer = 41
    float = 0.67
    boolean = True
    bool_to_int = int(boolean)
    float_to_int = int(float)
    string_to_int = len(string)
    print("This is the type change function:", bool_to_int, float_to_int, string_to_int)
    print(string)

# Defining third function
def iter():
    list = []
    iterate = (1,2,3,4,5,6,7,8,9,10)
    for i in iterate:
        list.append(i)
    print("This is the iter function:", list)

# Inputs
number_1 = int(input("Give me one number:"))
number_2 = int(input("And another:"))

# Outputs
calc(number_1, number_2) # A function using user-inputted parameters!
type_change() # A function that type changes (only to ints though)
iter() # A function that iterates over a list and appends
```

### Code Explanation:
Literally just describes and puts into action a couple fundamentals of python (Loops, arithmetic, type changing)
Just need to run the script and give input to the calc function