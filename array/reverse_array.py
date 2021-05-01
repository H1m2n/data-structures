def reverse_arr(arr):
    arr_len = len(arr)
    j = arr_len - 1
    for i in range(arr_len // 2):
        arr[j], arr[i] = (arr[i], arr[j])
        j -= 1


arr = [1, 2, 3, 4, 5]
reverse_arr(arr)
print(arr)
