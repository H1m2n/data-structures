# https://leetcode.com/problems/longest-turbulent-subarray/

arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]


#
# [9, 4]
# [4, 2, 10, 7, 8]
#
# 9 > 4 > 2
#
# 8 < 9 > 1

def max_turbulent_size(arr):
    if len(arr) == 1:
        return len(arr)
    diff_prev = 0
    max_turbulent, turbulent_size, j = (1, 1, 1)
    while j < len(arr):
        # turbulent condition is , if arr[j-2] < arr[j-1] > arr[j] or arr[j-2] > arr[j-1] < arr[j]
        # so we calculated diff of prev pair and compare current pair and check for condition
        if (diff_prev > 0 and arr[j] < arr[j - 1]) or (diff_prev < 0 and arr[j] > arr[j - 1]):
            turbulent_size = turbulent_size + 1
            diff_prev = arr[j] - arr[j - 1]
        else:
            diff_prev = arr[j] - arr[j - 1]
            # if diff_prev != 0 then we need to add pair to increase turbulent size
            turbulent_size = 2 if diff_prev != 0 else 1
        max_turbulent = max(max_turbulent, turbulent_size)
        j += 1
    return max_turbulent


arr = [9, 4, 2, 10, 7, 8, 9, 1, 9]
print(max_turbulent_size(arr))
