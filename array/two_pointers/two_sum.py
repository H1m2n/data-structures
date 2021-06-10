# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# [2, 7, 11, 15, 17, 18], target = 18
def two_sum(numbers, target):
    i, j = (0, len(numbers) - 1)
    for idx, x in enumerate(numbers):
        e_sum = numbers[i] + numbers[j]
        if e_sum == target:
            return [i + 1, j + 1]
        elif e_sum > target:
            j -= 1
        else:
            i += 1


# numbers = [2, 7, 11, 15, 17, 18]
# target = 18
# numbers = [2, 7, 11, 15]
# target = 9
numbers = [2,3,4]
target = 6
print(two_sum(numbers, target))
