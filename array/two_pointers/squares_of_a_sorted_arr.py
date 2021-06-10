"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].


Ans:
[-4,-1,0,3,10]
[16, 1, 0, 9, 100]

[-7,-3,2,3,11]
[49, 9, 4, 9, 11]

if array in sorted order and contains both negative and positive
then square we got like this
-----decreasing---->after one point----increasing---->
16   1    0                           9  100
          i                           j
so get a point where we start seeing increment and from their put elements by traversing back and forth into a
new array
"""


def squares_of_a_sorted_arr(arr):
    n = len(arr)
    left, right = 0, n - 1
    index = n - 1
    result = [0 for x in arr]

    while index >= 0:

        if abs(arr[left]) >= abs(arr[right]):
            result[index] = arr[left] * arr[left]
            left += 1
        else:
            result[index] = arr[right] * arr[right]
            right -= 1
        index -= 1

    for i in range(n):
        arr[i] = result[i]
    print(result)


arr = [-4, -1, 0, 3, 10]

squares_of_a_sorted_arr(arr)
