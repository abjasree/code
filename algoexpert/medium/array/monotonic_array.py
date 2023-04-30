def isMonotonic(array):
    # Write your code here.
    if len(array) <= 2:
        return True
    direction = array[-1] - array[0]
    for i in range(1, len(array) - 1):
        diff = array[i] - array[i - 1]
        if direction > 0 and diff < 0:
            return False
        elif direction < 0 and diff > 0:
            return False
        elif direction == 0 and (diff < 0 or diff > 0):
            return False
    return True


def isMonotonic(array):
    # Write your code here.
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(array)):
        diff = array[i] - array[i - 1]
        if diff < 0:
            isNonDecreasing = False
        if diff > 0:
            isNonIncreasing = False
    return isNonDecreasing or isNonIncreasing
