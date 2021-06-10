from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # 4, 2, 5, 7
        # 0  1  2  3

        # Approach - 1
        # will create 2 stacks one for odd and one for even
        # now loop through length of nums and fill up array with odd and even stack

        # Approach - 2
        # for even index if element is not even then find the nearest event element located at odd index
        # same we need to do for odd indexs
        evenIndex = 0
        oddIndex = 1
        while evenIndex < len(nums) and oddIndex < len(nums):
            if (nums[evenIndex] % 2 != 0):
                while (nums[oddIndex] % 2 != 0):
                    oddIndex += 2
                nums[evenIndex], nums[oddIndex] = (nums[oddIndex], nums[evenIndex])

            elif (nums[oddIndex] % 2 != 1):
                while (nums[evenIndex] % 2 != 1):
                    evenIndex += 2

                nums[evenIndex], nums[oddIndex] = (nums[oddIndex], nums[evenIndex])

            evenIndex += 2
            oddIndex += 2

        return nums

        # e_stack, o_stack = ([], [])
        #
        # for x in nums:
        #     if x % 2 == 0:
        #         e_stack.append(x)
        #     else:
        #         o_stack.append(x)
        #
        # res = []
        # i = 0
        # while i < len(nums):
        #     if i % 2 == 0:
        #         res.append(e_stack[-1])
        #         e_stack.pop()
        #     else:
        #         res.append(o_stack[-1])
        #         o_stack.pop()
        #     i += 1
        # return res


obj = Solution()
nums = [648, 831, 560, 986, 192, 424, 997, 829, 897, 843]
print(obj.sortArrayByParityII(nums))
