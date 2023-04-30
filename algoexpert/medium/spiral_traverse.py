def spiralTraverse(array):
    # Write your code here.
    result = []
    st_row, end_row = 0, len(array) - 1
    st_col, end_col = 0, len(array[0]) - 1

    while st_row <= end_row and st_col <= end_col:
        for col in range(st_col, end_col + 1):
            result.append(array[st_row][col])
        for row in range(st_row + 1, end_row + 1):
            result.append(array[row][end_col])
        for col in reversed(range(st_col, end_col)):
            if st_row == end_row:
                break
            result.append(array[end_row][col])
        for row in reversed(range(st_row + 1, end_row)):
            if st_col == end_col:
                break
            result.append(array[row][st_col])

        st_row += 1
        end_row -= 1
        st_col += 1
        end_col -= 1

    return result
