def quickSort(arr, low, high):
    if low < high:
        # /* pi is partitioning index, arr[pi] is now
        #    at right place */
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)  # Before pi
        quickSort(arr, pi + 1, high)  # After pi


def partition(arr, low, high):
    pivot_ele = arr[high]

    j = high
    # elements less than reside in left from pivot greater elements reside in right
    i = low
    while i < j:
        if arr[i] < pivot_ele:
            i += 1
        else:
            if i == j - 1:
                arr[j], arr[j - 1] = (arr[j - 1], arr[j])
            else:
                temp = arr[j - 1]
                arr[j - 1] = pivot_ele
                arr[j] = arr[i]
                arr[i] = temp
            j -= 1
    return i


arr = [3, 7, 8, 5, 2, 1, 9, 5, 4]
quickSort(arr, 0, 8)
print(arr)
