from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        # arr = [3, 4, 2, 2, 1, 2, 2, 1, 1, 1, 2, 3, 2, 2]
        # m = 3
        # k = 2
        count = 0
        i = 0
        while i < len(arr):
            if i + m < len(arr) and arr[i] == arr[i + m]:
                count += 1
            else:
                count = 0
            if count == (k - 1) * m:
                return True
            i += 1

        return False


obj = Solution()
arr = [3, 4, 2, 2, 1, 2, 2, 1, 1, 1, 2, 3, 2, 2]
m = 3
k = 2

# arr = [1, 2, 1, 2, 1, 3]
# m = 2
# k = 3
print(obj.containsPattern(arr, m, k))
# i = 0, j = 2, ptr = [3, 2, 2]
# j = 3, if arr[i] == arr[j]; i++, j++, else i++

# i = 1, j = 3, if arr[i] == arr[j]; i++, j++
