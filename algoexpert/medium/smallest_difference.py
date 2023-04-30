def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    idx1 = 0
    idx2 = 0
    smallest_diff = float("inf")
    current_diff = float("inf")
    smallest_pair = []
    while idx1 < len(arrayOne) and idx2 < len(arrayTwo):
        num1 = arrayOne[idx1]
        num2 = arrayTwo[idx2]
        current_diff = abs(num1 - num2)

        if num1 < num2:
            idx1 += 1
        elif num2 < num1:
            idx2 += 1
        else:
            return [num1, num2]
        if smallest_diff > current_diff:
            smallest_diff = current_diff
            smallest_pair = [num1, num2]
    return smallest_pair
