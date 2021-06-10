class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [1, 2, 3, 1, 1, 3]
        count = 0
        e_stack = []
        i = len(nums) - 1
        while i >= 0:
            if len(e_stack) == 0:
                e_stack.append(nums[i])
            elif len(e_stack) > 0:
                # pop until stack is not empty and check peek with nums[i], and put element into temp stack
                tmp_stack = []
                while len(e_stack) > 0:
                    if e_stack[-1] == nums[i]:
                        count += 1
                    tmp_stack.append(e_stack[-1])
                    e_stack.pop()
                e_stack = tmp_stack
                e_stack.append(nums[i])
            i -= 1
        return count


obj = Solution()
nums = [1, 2, 3, 1, 1, 3]
nums = [1, 1, 1, 1]
# nums = [1, 2, 3]
print(obj.numIdenticalPairs(nums))
