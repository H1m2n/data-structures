"""
Problem -
You are given a list of n-1 integers and these integers are in the range of 1 to n.
There are no duplicates in the list. One of the integers is missing in the list.
Write an efficient code to find the missing integer.

Method 1: This method uses the technique of the summation formula.

Approach: The length of the array is n-1.
So the sum of all n elements, i.e sum of numbers from 1 to n can be calculated using the formula n*(n+1)/2.
Now find the sum of all the elements in the array and subtract it from the sum of first n natural numbers,
it will be the value of the missing element.
"""


def missing_integer(arr):
    """
    convert list into map
    iterate on list
    next_ele = curr ele + 1, that next_ele should be available in map
    :param arr:
    :return:
    """
    arr_map = {}
    for x in arr:
        arr_map[x] = 1
    expected_ele = None
    for x in arr:
        expected_ele = x + 1
        if not arr_map.get(expected_ele):
            break
    return expected_ele


def getMissingNo(A):
    n = len(A)
    total = (n + 1) * (n + 2) / 2
    sum_of_A = sum(A)
    return int(total - sum_of_A)


print(missing_integer([1, 2, 4, 6, 3, 7, 8]))
print(missing_integer([1, 2, 3, 5]))

print(getMissingNo([1, 2, 4, 6, 3, 7, 8]))
print(getMissingNo([1, 2, 3, 5]))
