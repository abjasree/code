def sortedSquaredArray(array):
    # Write your code here.
    left = 0
    right = len(array) - 1
    squared_array = []
    while left <= right:
        if abs(array[left]) < abs(array[right]):
            squared_array.append(array[right]**2)
            right -= 1
        else:
            squared_array.append(array[left]**2)
            left += 1
    squared_array.reverse()
    return squared_array
