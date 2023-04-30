def getNthFib(n):
    # Write your code here.
    fib_dict = {1: 0, 2: 1}
    for i in range(3, n + 1):
        if i not in fib_dict.keys():
            fib_dict[i] = fib_dict[i - 1] + fib_dict[i - 2]
    return fib_dict[n]


def getNthFib(n):
    # Write your code here.
    last_two = [0, 1]
    count = 3
    while count <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0], last_two[1] = last_two[1], next_fib
        count += 1
    return last_two[1] if n > 1 else last_two[0]
