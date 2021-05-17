# problem statement
# John goes to shopping with his mom. There he saw a toy shop.
# He want to buy "maximum no of toys" that are reside in a rack of toy shop, so his mom tells him
# that "you can have at-most 2 toys and you need to pick it up in line"
from collections import defaultdict


def pick_toys(arr, k):
    i = j = 0
    max_toys = 0
    uniq_toy_map = defaultdict(lambda: 0)
    while j < len(arr):
        uniq_toy_map[arr[j]] = uniq_toy_map[arr[j]] + 1
        no_of_uniq_toys = len(uniq_toy_map)
        if no_of_uniq_toys < k:
            j += 1
        elif no_of_uniq_toys == k:
            max_toys = max(max_toys, sum(uniq_toy_map.values()))
            j += 1
        elif no_of_uniq_toys > k:
            while no_of_uniq_toys > k:
                uniq_toy_map[arr[i]] = uniq_toy_map[arr[i]] - 1
                if uniq_toy_map[arr[i]] == 0:
                    del (uniq_toy_map[arr[i]])
                    no_of_uniq_toys -= 1
                i += 1
            j += 1
    return max_toys


arr = ['a', 'b', 'a', 'c', 'c', 'a', 'b']
print(pick_toys(arr, 2))
