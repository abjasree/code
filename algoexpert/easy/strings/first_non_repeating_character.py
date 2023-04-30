def firstNonRepeatingCharacter(string):
    # Write your code here.
    for i in range(len(string)):
        duplicate = False
        for j in range(len(string)):
            if string[j] == string[i] and i != j:
                duplicate = True
        if not duplicate:
            return i

    return -1


def firstNonRepeatingCharacter(string):
    # Write your code here.
    char_count = {}
    for i in string:
        char_count[i] = char_count.get(i, 0) + 1

    for idx in range(len(string)):
        char = string[idx]
        if char_count[char] == 1:
            return idx
    return -1
