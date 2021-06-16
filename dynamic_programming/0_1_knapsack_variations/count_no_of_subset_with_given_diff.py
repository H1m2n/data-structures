# This problem will reduce to count_of_subset_sum_with_a_given_sum
# How?
# I have an array arr = [1, 1, 2, 3]
# we need to find out no of subsets that has difference of 1
# how we need to do partition -> array should be divided into 2 partitions

# s1 = [1, 1, 2], s2 = [3], sum(s1) - sum(s2) = 1
# s1 = [1, 3], s2 = [1, 2], sum(s1) - sum(s2) = 1
# s1 = [1, 3], s2 = [1, 2], sum(s1) - sum(s2) = 1


# so upto now we have one equation
# so eq1: sum(s1) - sum(s2) = 1

# we can say that if we do sum of 2 subsets then total sum will be equals to sum of array
# so eq2: sum(s1) + sum(s2) = sum(array)


# if we do maths with 2 equations

# sum(s1) - sum(s2) = 1
# + sum(s1) + sum(s2) = 7
# ------------------------
# 2 sum(s1) = diff + sum(arr)
#
# sum(s1) = (diff + sum(arr)) / 2
#
# sum(s1) = (1+7) / 2 = 4

# so at last we need to count all the subsets that has the sum of 4(problem -> count_of_subset_sum_with_a_given_sum)
