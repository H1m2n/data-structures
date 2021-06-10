# counting sort
# https://www.programiz.com/dsa/counting-sort


# radix sort
# https://www.programiz.com/dsa/radix-sort
# [121, 001, 432, 023, 564, 045, 788]


# Radix sort
# 1. Group numbers based on 1st digit
# 1st digit sort
{
    # 1: [121, 001],
    # 2: [432],
    # 3: [023],
    # 4: [564],
    # 5: [045],
    # 8: [788]
}
# 2. get the max of keys present in map(that is 8)

# 3. draw index from 0 to 8 with default 0 value present in it

# 4. iterate on dictionary(key, value) and increment the count at index(mapping => key represent index)
# [0, 2, 1, 1, 1, 1, 0, 0, 1]

# 5. calculate cumulative sum
# [0, 0, 2, 3, 4, 5, 6, 6, 6]

# 6. create an empty array with default None values and put value at correct position in newly created array
# correct position = cumulative arr(value at index - 1)
# [121, 001, 432, 023, 564, 045, 788]

# 2nd digit sort
# {
#     0: [001],
#     2: [121, 023],
#     3: [432],
#     4: [045],
#     6: [564],
#     8: [788]
#
# }

# [1, 0, 2, 1, 1, 0, 1, 0, 1]
#
# [0, 1, 1, 3, 4, 5, 5, 6, 6]
#
# [001, 023, 121, 432, 045, 564, 788]
