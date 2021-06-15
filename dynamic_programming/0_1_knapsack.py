# problem: You have a knapsack bag, its capacity is 7
# item weight = [1, 2, 3, 4, 5]
# item value = [1, 3, 4, 5, 7] respectively
# We need to get maximum number of profit by satisfying condition
# no of weight of items == 7 and max profit

# formula is  V[i, w] = max{V[i-1, w], V[i-1, w - w[i]] + P[i]}
# Approach: Before approaching question, make choice diagram
#  include item
# /      \
# yes    no

# recursive approach
def cal_max_profit(item_weight, item_value, no_of_items, capacity=7):
    # Base cond(think of min valid input)
    # either store doesn't has any item or we don't have any capacity of a beg
    if no_of_items == 0 or capacity == 0:
        return 0
    wt_of_picked_item = item_weight[no_of_items - 1]
    value_of_picked_item = item_value[no_of_items - 1]
    if wt_of_picked_item > capacity:
        # if an item weight is > than curr capacity then exclude that item
        return cal_max_profit(item_weight, item_value, no_of_items - 1, capacity)
    else:
        # if an item weight is <= than curr capacity, then we have 2 choices their, either we can include this
        # item or not so
        remaining_capacity = capacity - wt_of_picked_item
        return max(
            value_of_picked_item + cal_max_profit(item_weight, item_value, no_of_items - 1, remaining_capacity),
            # including
            cal_max_profit(item_weight, item_value, no_of_items - 1, capacity)  # excluding
        )


memoized_dict = {}


# memoization
def cal_max_profit_memoized(item_weight, item_value, no_of_items, capacity=7):
    # print(no_of_items, capacity, "debug")
    if no_of_items == 0 or capacity == 0:
        return 0

    wt_of_picked_item = item_weight[no_of_items - 1]
    value_of_picked_item = item_value[no_of_items - 1]
    # import pdb;pdb.set_trace()
    if (wt_of_picked_item, value_of_picked_item) in memoized_dict:
        print('herre...', memoized_dict)
        return memoized_dict[(wt_of_picked_item, value_of_picked_item)]

    if wt_of_picked_item > capacity:
        # if an item weight is > than curr capacity then exclude that item
        memoized_dict[(no_of_items, capacity)] = cal_max_profit_memoized(item_weight, item_value, no_of_items - 1,
                                                                         capacity)
        return memoized_dict[(no_of_items, capacity)]
    else:
        # if an item weight is <= than curr capacity, then we have 2 choices their, either we can include this
        # item or not so
        remaining_capacity = capacity - wt_of_picked_item
        memoized_dict[(no_of_items, capacity)] = max(
            value_of_picked_item + cal_max_profit_memoized(item_weight, item_value, no_of_items - 1,
                                                           remaining_capacity),
            # including
            cal_max_profit_memoized(item_weight, item_value, no_of_items - 1, capacity)  # excluding
        )
        return memoized_dict[(no_of_items, capacity)]


# top down approach
def cal_max_profit_top_down(item_weight, item_value, no_of_items, capacity=7):
    # here we need to create a matrix for no_of_items + 1, capacity + 1
    # where capacity is in X-axis and no_of_items in Y-axis
    # Top down approach composes 2 parts
    # 1. initialization
    # 2. choice diagram logic
    # created a matrix
    n = no_of_items + 1
    w = capacity + 1
    t = [[None for i in range(w)] for j in range(n)]
    for i, row in enumerate(t):
        for j, col in enumerate(row):
            if i == 0 or j == 0:
                t[i][j] = 0
    print(t)

    for i, row in enumerate(t):
        for j, col in enumerate(row):
            if i == 0 or j == 0:
                continue
            if item_weight[i - 1] <= j:
                t[i][j] = max(item_value[i - 1] + t[i - 1][j - item_weight[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]

    return t[i][j]


item_weight = [1, 2, 3, 4, 5]
item_value = [1, 10, 4, 5, 7]
# item_weight = [1, 3, 4, 5]
# item_value = [1, 4, 5, 7]
# print(cal_max_profit(item_weight, item_value, len(item_weight)))
print(cal_max_profit_memoized(item_weight, item_value, len(item_weight)))
print(cal_max_profit_top_down(item_weight, item_value, len(item_weight)))
