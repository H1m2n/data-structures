from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        range_list = []
        i, j = (0, 0)
        while j < len(nums):
            print(i, j)
            if j == len(nums) - 1 or nums[j] + 1 != nums[j + 1]:
                if i == j:
                    range_list.append(f"{nums[i]}")
                else:
                    range_list.append(f"{nums[i]}->{nums[j]}")
                i = j + 1
            j += 1

        # for j in range(len(nums)):
        #     print(i, j)
        #     if j == len(nums) - 1 or nums[j] + 1 != nums[j + 1]:
        #         range_list.append(f"{i}->{j}")
        #         i = j + 1
        return range_list


obj = Solution()
nums = [0, 1, 2, 4, 5, 7]
print(obj.summaryRanges(nums))
[3,2,2,1,2,2,1,1,1,2,3,2,2]
3
2