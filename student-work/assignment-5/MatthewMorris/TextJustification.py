def full_justify(words, max_width):
    result = []
    current_line = []
    current_length = 0

    for word in words:

        if current_length + len(word) + len(current_line) <= max_width:
            current_line.append(word)
            current_length += len(word)
        else:
            spaces_needed = max_width - current_length
            spaces_between = len(current_line) - 1 if len(current_line) > 1 else 1
            if len(current_line) == 1:
                result.append(current_line[0] + ' ' * spaces_needed)
            else:
                spaces_per_gap = spaces_needed // spaces_between
                extra_spaces = spaces_needed % spaces_between
                justified_line = ''
                for i, w in enumerate(current_line[:-1]):
                    justified_line += w
                    spaces = spaces_per_gap + (1 if i < extra_spaces else 0)
                    justified_line += ' ' * spaces
                justified_line += current_line[-1]
                result.append(justified_line)
            current_line = [word]
            current_length = len(word)
    if current_line:
        last_line = ' '.join(current_line)
        last_line += ' ' * (max_width - len(last_line))
        result.append(last_line)

    return result

words = ["This", "is", "an", "example", "of", "text", "justification."]
max_width = 10

result = full_justify(words, max_width)
for line in result:
    print(line)
