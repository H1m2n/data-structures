class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # [1, 2, 3, 4, 5, 6, 7]
        arr_len = len(nums)
        while (k > 0):
            # always picked-up value from last position as we have rotated array for every position
            # picked-up last value from array
            tmp_elm = nums[arr_len - 1]

            # iterate over remaining element from right to left and shift them in right by 1 step
            for i in range(arr_len - 2, -1, -1):
                nums[i + 1] = nums[i]

            # and put picked-up element in 1st position of array
            nums[i] = tmp_elm
            k -= 1
            # do this process recursively until we got position == 0


# obj = Solution()
# arr = [1,2,3,4,5,6,7]
# obj.rotate(arr, 1)
# print(arr)


def rotate_arr(arr, n):
    index_start_point = len(arr) - n
    index_adjust_point = index_start_point
    tmp_arr = []
    while len(arr) > index_start_point:
        tmp_arr.append(arr[index_start_point])
        index_start_point += 1

    tmp_i = -1
    for i in range(index_adjust_point - 1, -1, -1):
        arr[tmp_i] = arr[i]
        tmp_i = tmp_i - 1

    print(tmp_arr)
    for i, x in enumerate(tmp_arr):
        arr[i] = x
    print(arr)


def rotate(nums, k):
    n = len(nums)
    a = [0] * n
    for i in range(n):
        print(i, ((i + k) % n))
        a[(i + k) % n] = nums[i]
    print(a)


arr = [1, 2, 3, 4, 5, 6, 7]
rotate(arr, 3)
