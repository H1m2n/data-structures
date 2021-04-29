from collections import defaultdict

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def_dict = defaultdict(lambda: 0)

        for x in nums:
            def_dict[x] = def_dict[x] + 1

        for k, v in def_dict.items():
            if v > 1:
                return True
        return False

obj = Solution()
is_contains_duplicate = obj.containsDuplicate([1,1,2])
print(is_contains_duplicate)