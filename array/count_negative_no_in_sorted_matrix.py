def count_negative_no_in_sorted_matrix(grid):
    neg_sum = 0
    for arr in grid:
        i, j = (0, len(arr) - 1)
        while i <= j:
            if arr[j] > 0:
                # no negative element
                break
            elif arr[i] < 0:
                neg_sum += 1
                i += 1
            elif arr[i] > 0 and arr[j] < 0:
                i += 1
    return neg_sum


grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [1, -1, -1, -2], [-1, -1, -2, -3]]
# grid = [[4, 3, 2, -1]]
# grid = [[1, 1, -1, -2]]
# grid = [[-1, -1, -2, 3]]
print(count_negative_no_in_sorted_matrix(grid))
