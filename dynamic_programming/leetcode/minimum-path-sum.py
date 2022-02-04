from typing import List
import copy
import sys


class SolutionBk:
    def solve(self, grid, out, i, j, dp, min_path_sum):
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            out.append(grid[i][j])
            min_path_sum[0] = min(min_path_sum[0], sum(out))
            return min_path_sum[0]

        if i == len(grid) - 1:
            # we don't have any choice to go down, so we need to select right path
            op1 = copy.copy(out)
            op1.append(grid[i][j])
            self.solve(grid, op1, i, j + 1, dp, min_path_sum)

        elif j == len(grid[0]) - 1:
            # we don't have any choice to go right, so we need to select downside path
            op2 = copy.copy(out)
            op2.append(grid[i][j])
            self.solve(grid, op2, i + 1, j, dp, min_path_sum)
        else:
            # we have choice available to move right or down
            op3 = copy.copy(out)
            op3.append(grid[i][j])
            self.solve(grid, op3, i + 1, j, dp, min_path_sum)

            op4 = copy.copy(out)
            op4.append(grid[i][j])
            self.solve(grid, op3, i, j + 1, dp, min_path_sum)
        return min_path_sum

    def minPathSum(self, grid: List[List[int]]) -> int:
        i, j = (0, 0)
        return self.solve(grid, [], i, j, {}, [sys.maxsize])[0]


class Solution():
    def solve(self, grid, i, j, dp):
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            # if we reach at the bottom right corner cell, return that cell value to include in path
            return grid[i][j]

        if (i, j) in dp:
            return dp[(i, j)]

        row_path = col_path = sys.maxsize
        if i < len(grid) - 1:
            # explore path of next row and same col
            row_path = grid[i][j] + self.solve(grid, i + 1, j, dp)
        if j < len(grid[0]) - 1:
            # explore path of next column and same row
            col_path = grid[i][j] + self.solve(grid, i, j + 1, dp)

        # we need to select the minimum one
        dp[(i, j)] = min(row_path, col_path)

        return dp[(i, j)]

    def minPathSum(self, grid: List[List[int]]) -> int:
        i, j = (0, 0)
        dp = {}
        return self.solve(grid, i, j, dp)


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
# grid = [[1, 2, 3], [4, 5, 6]]
obj = Solution()
print(obj.minPathSum(grid))
