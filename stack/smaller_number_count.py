class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        sort_num = sorted(nums)
        # sort the numbers
        # get the nearest smallest index to left and put that into map
        # now iterate on orignal array and get the count of min element
        i = 0
        smaller_number_count = {}
        e_stack = []
        while i < len(sort_num):
            if len(e_stack) == 0:
                smaller_number_count[sort_num[i]] = 0
            elif len(e_stack) > 0 and e_stack[-1] < sort_num[i]:
                smaller_number_count[sort_num[i]] = len(e_stack)
            e_stack.append(sort_num[i])
            i += 1
        res = []
        for x in nums:
            res.append(smaller_number_count[x])
        return res


obj = Solution()
nums = [8, 1, 2, 2, 3]
nums = [6, 5, 4, 8]
nums = [7, 7, 7, 7]
print(obj.smallerNumbersThanCurrent(nums))
