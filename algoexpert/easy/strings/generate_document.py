# O(m * (n+m)) time complexity | O(1) space complexity
def generateDocument(characters, document):
    # Write your code here.
    for char in document:
        document_count = char_count(char, document)
        charac_count = char_count(char, characters)
        if charac_count < document_count:
            return False
    return True


def char_count(char, string):
    freq = 0
    for i in string:
        if i == char:
            freq += 1
    return freq


# O(c * (n+m)) time complexity | O(c) space complexity
def generateDocument(characters, document):
    # Write your code here.
    seen_char = set()
    for char in document:
        if char in seen_char:
            continue

        document_count = char_count(char, document)
        charac_count = char_count(char, characters)
        if charac_count < document_count:
            return False
        seen_char.add(char)
    return True


def char_count(char, string):
    freq = 0
    for i in string:
        if i == char:
            freq += 1
    return freq


# O(n+m) time complexity | O(c) space complexity
def generateDocument(characters, document):
    # Write your code here.
    count_dict = {}
    for char in characters:
        if char not in count_dict:
            count_dict[char] = 0
        count_dict[char] += 1
    for char in document:
        if char not in count_dict or count_dict[char] == 0:
            return False
        count_dict[char] -= 1
    return True
