def subset_sum(arr, sum):
    if len(arr) >= 0 and sum == 0:
        return 1
    if len(arr) == 0 and sum > 0:
        return 0

    no_of_items = len(arr)
    selected_item = arr[no_of_items - 1]
    if selected_item > sum:
        # we can't include current item, now try to get subset for rest of the items
        return subset_sum(arr[:no_of_items - 1], sum)
    else:
        # here we ave 2 choices, either include curr element or not
        # if including then -> do recursion for rest of the items by selecting curr item
        # if not then -> we are not including curr item, now try to get subset for rest of the items
        return (subset_sum(arr[:no_of_items - 1], sum - selected_item)) + (
            subset_sum(arr[:no_of_items - 1], sum))


# dynamic programming caching approach
memoized_dict = {}


def subset_sum_memoized(arr, sum):
    if len(arr) >= 0 and sum == 0:
        return 1
    if len(arr) == 0 and sum > 0:
        return 0

    no_of_items = len(arr)
    selected_item = arr[no_of_items - 1]
    if (selected_item, sum) in memoized_dict:
        # print('heree..', memoized_dict)
        return memoized_dict[(selected_item, sum)]
    # print(memoized_dict)
    if selected_item > sum:
        memoized_dict[(selected_item, sum)] = subset_sum_memoized(arr[:no_of_items - 1], sum)
        return memoized_dict[(selected_item, sum)]
    else:
        memoized_dict[(selected_item, sum)] = (
                                                  subset_sum_memoized(arr[:no_of_items - 1], sum - selected_item)
                                              ) + (
                                                  subset_sum_memoized(arr[:no_of_items - 1], sum)
                                              )
        return memoized_dict[(selected_item, sum)]


def subset_sum_top_down(arr, sum):
    # sum will be on X-axis
    # arr will be on Y-axis
    n = len(arr) + 1
    w = sum + 1
    t = [[None for i in range(w)] for j in range(n)]
    for i, row in enumerate(t):
        for j, col in enumerate(row):
            if i == 0 and j > 0:
                t[i][j] = 0
            if i >= 0 and j == 0:
                t[i][j] = 1

    for i, row in enumerate(t):
        for j, col in enumerate(row):
            if i == 0 or j == 0:
                continue

            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j] + t[i - 1][j - arr[i - 1]]
            else:
                t[i][j] = t[i - 1][j]
    print(t)
    return t[i][j]


arr = [2, 3, 5, 6, 8, 10]
sum = 10

# arr = [1, 2, 3, 3]
# sum = 6
print(subset_sum(arr, sum))
print(subset_sum_memoized(arr, sum))
print(subset_sum_top_down(arr, sum))
