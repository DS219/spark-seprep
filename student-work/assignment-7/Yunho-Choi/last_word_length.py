def length_of_last_word(s: str) -> int:
    s = s.strip()
    words = s.split(" ")
    return len(words[-1])


if __name__ == "__main__":
    sentences = [
        "Hello World",
        "fly me to the moon",
        "I am going to find a job"
    ]

    for sentence in sentences:
        result = length_of_last_word(sentence)
        print(f"Input: '{sentence}' -> Length of last word: {result}")

