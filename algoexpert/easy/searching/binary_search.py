def binarySearch(array, target):
    # Write your code here.
    return helper(array, target, 0, len(array) - 1)


def helper(array, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    match = array[mid]
    if target == match:
        return mid
    elif target < match:
        return helper(array, target, left, mid - 1)
    else:
        return helper(array, target, mid + 1, right)


def helper(array, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        match = array[mid]
        if target == match:
            return mid
        elif target < match:
            right = mid - 1
        else:
            left = mid + 1
    return -1
