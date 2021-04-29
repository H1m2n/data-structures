class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i, x in enumerate(nums):
            try:
                zeroth_index = nums.index(0)
                is_zero_moved = True
                for n in nums[zeroth_index:]:
                    if n != 0:
                        is_zero_moved = False
                if is_zero_moved:
                    return
            except:
                return

            if x == 0:
                if i < len(nums) - 1:
                    nums[i] = nums[i + 1]
                    nums[i + 1] = 0
        print(nums)
        self.moveZeroes(nums)


# obj = Solution()
# item = [0,1,0,3,12]
# obj.moveZeroes(item)
# print(item)

def move_zero(arr):
    count = 0
    for i, n in enumerate(arr):
        if n != 0:
            arr[count] = arr[i]
            count += 1
        print((i, arr))
    while count < len(arr):
        arr[count] = 0
        count += 1


nums = [0, 1, 0, 3, 12]
move_zero(nums)
print(nums)


