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

def cal_max_profit(item_weight, item_value, no_of_items, capacity=7):
    if no_of_items == 0 or capacity == 0:
        return 0
    wt_of_picked_item = item_weight[no_of_items - 1]
    value_of_picked_item = item_value[no_of_items - 1]
    # item_weight.pop()
    # item_value.pop()
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


item_weight = [1, 2, 3, 4, 5]
item_value = [1, 10, 4, 5, 7]
# item_weight = [1, 3, 4, 5]
# item_value = [1, 4, 5, 7]
print(cal_max_profit(item_weight, item_value, len(item_weight)))
