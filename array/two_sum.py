class Solution(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i:]):
                if x + y == target:
                    return (i, j)


obj = Solution()
out = obj.two_sum([2, 7, 11, 15], 9)
print(out)


# optimal solution
class Solution1(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i, x in enumerate(nums):
            existing_num = nums_dict.get(x)
            if existing_num:
                existing_num.append(i)
            else:
                nums_dict[x] = [i]

        for k, v in nums_dict.items():
            if len(v) == 2:
                return v
            paired_value = target - k
            paired_value_i = nums_dict.get(paired_value)
            if paired_value_i:
                return (v[0], paired_value_i[0])


obj = Solution1()
out = obj.two_sum([3, 3, 3], 6)
print(out)
