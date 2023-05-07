def arrayOfProducts(array):
    # Write your code here.

    product = [1 for i in array]

    left_product = 1
    for i in range(len(array)):
        product[i] = left_product
        left_product *= array[i]

    right_product = 1
    for i in reversed(range(len(array))):
        product[i] *= right_product
        right_product *= array[i]

    return product
