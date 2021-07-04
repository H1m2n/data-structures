from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #     [1]
        #    [1, 1]
        #   [1, 2, 1]
        #  [1, 3, 3, 1]
        # [1, 4, 6, 4, 1]

        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            pascal_trngle = [[1], [1, 1]]
            n = 2
            while n <= numRows:
                print(n)
                new_row = [None] * n
                new_row[0], new_row[-1] = (1, 1)
                prev_row = pascal_trngle[-1]
                print(prev_row)
                i, j = (0, 1)
                while j < len(prev_row):
                    new_row[j] = prev_row[i] + prev_row[j]
                    i += 1
                    j += 1

                pascal_trngle.append(new_row)
                n += 1
        return pascal_trngle

obj = Solution()
obj.generate(6)