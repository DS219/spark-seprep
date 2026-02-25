# Ivan Wiandt
My name is Ivan and I like python because of its collection of easy to use premade libraries
### Example Code
``` # Open the file in read mode
text = open("4.txt", "r")

# Create an empty dictionary
d = dict()

# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()

    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()

    # Split the line into words
    words = line.split()

    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

# Print the contents of dictionary
l = [(count, key) for (key, count) in d.items()]
l = sorted(l, reverse=True)
for (count, key) in l:
    print(key, ":", count)
```
### Code Explanation
This simple script will take a text file and return the counts of every word

