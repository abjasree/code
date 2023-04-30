def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]

    return []


def twoNumberSum(array, targetSum):
    # Write your code here.
    num_dict = {}

    for i in array:
        if i in num_dict.keys():
            return [i, num_dict[i]]
        num_dict[targetSum - i] = i
    return []


def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] + array[right] == targetSum:
            return [array[left], array[right]]
        elif array[left] + array[right] > targetSum:
            right -= 1
        else:
            left += 1
    return []
