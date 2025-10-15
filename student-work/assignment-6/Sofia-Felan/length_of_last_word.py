def lengthOfLastWord(s):
    words = s.split()
    last_length = len(words[-1])
    return last_length


# Test case
sentence = "Hello world"
result = lengthOfLastWord(sentence)
print(f'Length of last word: {result}')