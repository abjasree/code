def commonCharacters(strings):
    # Write your code here.
    char_counts = {}
    for string in strings:
        unique_chars = set(string)
        for i in unique_chars:
            if i not in char_counts:
                char_counts[i] = 0
            char_counts[i] += 1
    com_char = []
    for chr, cnt in char_counts.items():
        if cnt == len(strings):
            com_char.append(chr)
    return com_char


def commonCharacters(strings):
    # Write your code here.
    small_str = find_small_string(strings)
    potential_common_chr = set(small_str)
    for string in strings:
        remove_non_exist_char(string, potential_common_chr)

    return list(potential_common_chr)


def find_small_string(strings):
    small_str = strings[0]
    for string in strings:
        if len(string) < len(small_str):
            small_str = string

    return small_str


def remove_non_exist_char(string, common_chr):
    uniq_str = set(string)
    for i in list(common_chr):
        if i not in uniq_str:
            common_chr.remove(i)
