from collections import defaultdict


# [1, 2, 1, 2, 3],  k = 2
# [1], [1, 2], [1, 2, 1], [1, 2, 1, 2], when now we include 3, then uniq character count will be 3,
# so we need to increment j and need to remove character from map
# currently map is -> {
#     1: 2
#     2: 2
#     3: 1
# }
# i = 1, currently map is -> {
#     1: 1
#     2: 2
#     3: 1
# }
# i = 2, currently map is -> {
#     1: 1
#     2: 1
#     3: 1
# }
# i = 3, currently map is -> {
#     2: 1
#     3: 1
# }


def substr_count_of_k_disticnt_char(nums, k):
    pass
