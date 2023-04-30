def runLengthEncoding(string):
    # Write your code here.
    encode = []
    length = 1
    n = len(string)
    for i in range(1, n):
        current = string[i]
        previous = string[i - 1]
        if current != previous or length == 9:
            encode.append(str(length))
            encode.append(previous)
            length = 0
        length += 1
    encode.append(str(length))
    encode.append(string[n - 1])
    return "".join(encode)
