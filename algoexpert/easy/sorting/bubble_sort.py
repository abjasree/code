def bubbleSort(array):
    # Write your code here.
    sorted = False
    while not sorted:
        sorted = True
        counter = 0
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
        counter += 1
    return array
