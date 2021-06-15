arr = [2, 3, 7, 8, 10]
sum = 11


# x axis -> 12 points of (sum)
# y axis -> 6 points of (arr)


# recursive approach
def subset_sum(arr, sum):
    if len(arr) == 0 and sum == 0:
        return True
    if len(arr) == 0 and sum > 0:
        return False

    no_of_items = len(arr)
    selected_item = arr[no_of_items - 1]
    if selected_item > sum:
        # we can't include current item, now try to get subset for rest of the items
        return False or subset_sum(arr[:no_of_items - 1], sum)
    else:
        # here we ave 2 choices, either include curr element or not
        # if including then -> do recursion for rest of the items by selecting curr item
        # if not then -> we are not including curr item, now try to get subset for rest of the items
        return (subset_sum(arr[:no_of_items - 1], sum - selected_item)) or (
                False or subset_sum(arr[:no_of_items - 1], sum))


# dynamic programming caching approach
memoized_dict = {}


def subset_sum_memoized(arr, sum):
    if len(arr) == 0 and sum == 0:
        return True
    if len(arr) == 0 and sum > 0:
        return False

    no_of_items = len(arr)
    selected_item = arr[no_of_items - 1]
    if (selected_item, sum) in memoized_dict:
        print('heree..', memoized_dict)
        return memoized_dict[(selected_item, sum)]
    # print(memoized_dict)
    if selected_item > sum:
        memoized_dict[(selected_item, sum)] = False or subset_sum_memoized(arr[:no_of_items - 1], sum)
        return memoized_dict[(selected_item, sum)]
    else:
        memoized_dict[(selected_item, sum - selected_item)] = (
                                                    subset_sum_memoized(arr[:no_of_items - 1], sum - selected_item)
                                                ) or (
                                                    False or subset_sum_memoized(arr[:no_of_items - 1], sum)
                                                )
        return memoized_dict[(selected_item, sum - selected_item)]


# print(memoized_dict)
# print(subset_sum(arr, sum))
print(subset_sum_memoized(arr, sum))
