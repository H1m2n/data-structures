# Identification:
# we have give a string or array, we get the feel of breaking that string into parts. and for each partitions
# we need to apply our logic, for each partition we will get some temp ans.
# by looking those temp ans we need to find out our original ans.


# let say we have a string of length n
# so suppose i is located at the near of starting point and j is located at the near of ending point
# if we need to applying partition, then we need to break string at kth index
# Actually we don't know where we should break, so will applying partition for i to j
# means k = i, k = i+1, k = i+2, until we hit j


# variation will depend on the questions asked
def standard_format(s, i, j):
    if i > j:
        return 0

    ans = 0
    k = i
    while k <= j:
        temp_ans1 = standard_format(s, i, k)
        temp_ans2 = standard_format(s, k + 1, j)

        # get the temp answer wth current partition, let say suppose we need to do sum
        # and in answer suppose we need to find maximum
        temp_ans = temp_ans1 + temp_ans2
        if ans < temp_ans:
            ans = temp_ans
        k += 1

    return ans
