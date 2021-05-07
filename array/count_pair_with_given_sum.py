def count_pair_with_given_sum(arr, given_sum):
    """
    Approach is of maximum sub array
    :return:
    """
    best_sum, max_ending_here = (-5, 0)
    pair_count = 0
    for x in arr:
        print((x, max_ending_here))
        max_ending_here = x + max_ending_here
        if given_sum == max_ending_here:
            best_sum = max_ending_here
            pair_count += 1
        if max_ending_here < 0:
            max_ending_here = 0
    print(best_sum)
    print(pair_count)


count_pair_with_given_sum([1, 5, 7, -1], 6)
