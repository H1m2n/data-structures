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
        return False or subset_sum(arr[:no_of_items - 1], sum)
    else:
        return (subset_sum(arr[:no_of_items - 1], sum - selected_item)) or (
                False or subset_sum(arr[:no_of_items - 1], sum))


# dynamic programming caching approach
subset_sum_dict = {}


def subset_sum_caching(arr, sum):
    print(subset_sum_dict)
    if len(arr) == 0 and sum == 0:
        return True
    if len(arr) == 0 and sum > 0:
        return False

    no_of_items = len(arr)
    selected_item = arr[no_of_items - 1]
    if (selected_item, sum) in subset_sum_dict:
        print('heree..')
        return subset_sum_dict[(selected_item, sum)]
    # print(subset_sum_dict)
    if selected_item > sum:
        subset_sum_dict[(selected_item, sum)] = False or subset_sum(arr[:no_of_items - 1], sum)
        return subset_sum_dict[(selected_item, sum)]
    else:
        subset_sum_dict[(selected_item, sum - selected_item)] = (subset_sum(arr[:no_of_items - 1], sum - selected_item)) \
                                                                or (False or subset_sum(arr[:no_of_items - 1], sum))
        return subset_sum_dict[(selected_item, sum - selected_item)]


# print(subset_sum(arr, sum))
print(subset_sum_caching(arr, sum))
