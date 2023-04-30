def isValidSubsequence(array, sequence):
    # Write your code here.
    seq_idx = 0
    for i in array:
        if seq_idx == len(sequence):
            break
        if sequence[seq_idx] == i:
            seq_idx += 1
    return seq_idx == len(sequence)
