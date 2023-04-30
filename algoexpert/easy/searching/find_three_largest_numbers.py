import math


def findThreeLargestNumbers(array):
    # Write your code here.
    first = -math.inf
    second = -math.inf
    third = -math.inf
    for i in array:
        if i > first:
            first, second, third = i, first, second
        elif i > second:
            second, third = i, second
        elif i > third:
            third = i
    return [third, second, first]


def findThreeLargestNumbers(array):
    # Write your code here.
    result = [None, None, None]
    for i in array:
        if result[2] is None or i > result[2]:
            shiftAndUpdate(result, i, 2)
        elif result[1] is None or i > result[1]:
            shiftAndUpdate(result, i, 1)
        elif result[0] is None or i > result[0]:
            shiftAndUpdate(result, i, 0)
    return result


def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]
