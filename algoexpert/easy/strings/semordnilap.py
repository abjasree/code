def semordnilap(words):
    # Write your code here.
    words_set = set(words)
    pairs = []
    for word in words:
        reverse = word[::-1]
        if reverse in words_set and reverse != word:
            pairs.append([word, reverse])
            words_set.remove(word)
            words_set.remove(reverse)
    return pairs
