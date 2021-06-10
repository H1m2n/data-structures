# arr = [6, 2, 5, 4, 5, 1, 6]  denoting building block height
# Note: This problem is easily understandable if we draw histogram on paper
# When we plot this array in histogram(building blocks), then on plotting we can found that
# if we able to find NSL and NSR then tha area in between NSL and NSR is the area that we can build for
# for current building block

# we assuming that we have building blocks of height 0 at index -1 and 7
# index = 0,  1,  2,  3,  4,  5,  6
# arr = [6,  2,  5,  4,  5,  1,  6]
# NSL = [-1,-1,  1,  1,  3, -1,  5]
# NSR = [1,  5,  3,  5,  5,  7,  7]

# width formula = (index of NSR - index of NSL - 1)
# width=[1,  5,  1,  3,  1,  7,  1]

# area formula = height * width
# area = [6, 10, 5, 12, 5, 7, 6]

# so ans = 12

def nearest_smallest_at_left(arr):
    nearest_smallest = []
    e_stack = []
    for i in range(0, len(arr), 1):
        arbitary_i = -1
        if len(e_stack) == 0:
            nearest_smallest.append((-1, arbitary_i))
        elif len(e_stack) > 0 and e_stack[-1][0] <= arr[i]:
            nearest_smallest.append(e_stack[-1])
        elif len(e_stack) > 0 and e_stack[-1][0] >= arr[i]:
            while len(e_stack) > 0 and e_stack[-1][0] >= arr[i]:
                e_stack.pop()

            if len(e_stack) == 0:
                nearest_smallest.append((-1, arbitary_i))
            else:
                nearest_smallest.append(e_stack[-1])
        e_stack.append((arr[i], i))
    return nearest_smallest


def nearest_smallest_at_right(arr):
    nearest_smallest = []
    e_stack = []
    for i in range(len(arr) - 1, -1, -1):
        arbitary_i = len(arr)
        if len(e_stack) == 0:
            nearest_smallest.append((-1, arbitary_i))
        elif len(e_stack) > 0 and e_stack[-1][0] <= arr[i]:
            nearest_smallest.append(e_stack[-1])
        elif len(e_stack) > 0 and e_stack[-1][0] >= arr[i]:
            while len(e_stack) > 0 and e_stack[-1][0] >= arr[i]:
                e_stack.pop()

            if len(e_stack) == 0:
                nearest_smallest.append((-1, arbitary_i))
            else:
                nearest_smallest.append(e_stack[-1])
        e_stack.append((arr[i], i))
    nearest_smallest.reverse()
    return nearest_smallest


def cal_width(arr, arr_of_nsl, arr_of_nsr):
    # width formula = (index of NSR - index of NSL - 1)
    width_arr = []
    for i in range(0, len(arr), 1):
        index_of_nsr = arr_of_nsr[i][1]
        index_of_nsl = arr_of_nsl[i][1]
        width_arr.append(index_of_nsr - index_of_nsl - 1)
    return width_arr


def maximum_area_histogram(arr):
    arr_of_nsl = nearest_smallest_at_left(arr)
    arr_of_nsr = nearest_smallest_at_right(arr)
    width_arr = cal_width(arr, arr_of_nsl, arr_of_nsr)
    max_area = 0
    for i, x in enumerate(arr):
        max_area = max(max_area, x * width_arr[i])
    return max_area


arr = [6, 2, 5, 4, 5, 1, 6]
print(maximum_area_histogram(arr))
