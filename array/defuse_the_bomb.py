from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = []
        if k == 0:
            for x in code:
                res.append(0)
            return res
        elif k > 0:
            j, l = (1, 1)
        elif k < 0:
            n = len(code)
            j, l = (n + k, n + k)

        i, e_sum, k = (0, 0, abs(k))
        while i < len(code):
            e_sum += code[j]
            if k > 1:
                k -= 1
                j += 1
            elif k == 1:
                res.append(e_sum)
                e_sum -= code[l]
                j += 1
                if j == len(code):
                    j = 0
                l += 1
                if l == len(code):
                    l = 0
                i += 1
        return res


obj = Solution()
code = [5, 7, 1, 4]
k = 3
code = [2, 4, 9, 3]
k = -2
print(obj.decrypt(code, k))
