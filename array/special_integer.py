import math
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        #
        least_occ = int((0.25*len(arr)))
        if len(arr) == 1 and least_occ == 1:
            return arr[0]
        print(least_occ)
        i, j = (0, 0)
        while j < len(arr):
            # cal the window size
            if arr[i] == arr[j]:
                print('herre', i, j)
                window_size = j - i + 1
                if window_size > least_occ:
                    return arr[i]
                # increase window size
                j += 1
            else:
                # if above condition is not true, then move i to current j
                # and increment j by 1
                i = j
                j += 1


obj = Solution()
arr = [1, 2, 3, 3]
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 12, 12]
# arr = [1,2,3,3]
print(obj.findSpecialInteger(arr))
