# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, depth=1):
    # Write your code here.
    total_sum = 0
    for ele in array:
        if type(ele) is list:
            total_sum += productSum(ele, depth + 1)
        else:
            total_sum += ele
    return total_sum * depth
