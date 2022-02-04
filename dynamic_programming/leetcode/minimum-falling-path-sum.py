from typing import List


class Solution:
    # [2, 1, 3]
    # [6, 5, 4] => [7, 6, 5]
    # [7, 8, 9] => [7, 8, 9] => [13, 13, 14]

    # [1, 2, 3]
    # [4, 5, 6] => [5, 6, 8]
    # [7, 8, 9] => [7, 8, 9] => [12, 13, 15]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        Approach ->
        Note: This is a reverse approach
        1. initialize a dp matrix with same dimension
        2. copy first row value as it is in dp of 1st row, ie: initialization process
        3. To calculate current element in dp, we need to get previous row's cell value from dp table according to the
           rule -> (row - 1, col - 1), (row - 1, col), or (row - 1, col + 1), rule is slightly changed due to reverse
           approach, and add it to the matrix[i][j]
        4. we need to get min sum from step2, and will store it in dp[i][j]
        5. we'll get the o/p at last row(min cell value will be the o/p)
        """
        dp = [[None for j in range(0, len(matrix[0]))] for i in range(0, len(matrix))]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0:
                    # initialization
                    dp[i][j] = matrix[i][j]
                else:
                    if j == 0:
                        # for left corner element, we have only 2 choices to select
                        dp[i][j] = min((matrix[i][j] + dp[i - 1][j]), (matrix[i][j] + dp[i - 1][j + 1]))
                    elif j == len(dp[0]) - 1:
                        # for right corner element, we have only 2 choices to select
                        dp[i][j] = min((matrix[i][j] + dp[i - 1][j]), (matrix[i][j] + dp[i - 1][j - 1]))
                    else:
                        dp[i][j] = min((matrix[i][j] + dp[i - 1][j - 1]), (matrix[i][j] + dp[i - 1][j]),
                                       (matrix[i][j] + dp[i - 1][j + 1]))

        last_row = dp[len(dp) - 1]
        return min(last_row)


class SolutionRecursiveApproach:

    def solve(self, i, j, out, mat, i_max, j_max, out_arr, dp):
        """
        DP code
        """
        if i == i_max:
            out_arr.append(out)
            return out
        # if (i, j) in dp:
        #     return dp[(i, j)]
        # make choice for the current node
        if j == 0:
            # then we'll have only 2 choices available
            # if (i, j, i + 1, j) in dp:
            #     return dp[(i, j, i + 1, j)]
            op1 = out
            op1 += mat[i + 1][j]
            dp[(i, j, i + 1, j)] = self.solve(i + 1, j, op1, mat, i_max, j_max, out_arr, dp)

            # if (i, j, i + 1, j + 1) in dp:
            #     return dp[(i, j, i + 1, j + 1)]
            op2 = out
            op2 += mat[i + 1][j + 1]
            dp[(i, j, i + 1, j + 1)] = self.solve(i + 1, j + 1, op2, mat, i_max, j_max, out_arr, dp)
        elif j == j_max:
            # then we'll have only 2 choices available
            # if (i, j, i + 1, j - 1) in dp:
            #     return dp[(i, j, i + 1, j - 1)]
            op1 = out
            op1 += mat[i + 1][j - 1]
            dp[(i, j, i + 1, j - 1)] = self.solve(i + 1, j - 1, op1, mat, i_max, j_max, out_arr, dp)

            # if (i, j, i + 1, j) in dp:
            #     return dp[(i, j, i + 1, j)]
            op2 = out
            op2 += mat[i + 1][j]
            dp[(i, j, i + 1, j)] = self.solve(i + 1, j, op2, mat, i_max, j_max, out_arr, dp)

        else:
            # we have 3 choices available
            # if (i, j, i + 1, j - 1) in dp:
            #     return dp[(i, j, i + 1, j - 1)]
            op1 = out
            op1 += mat[i + 1][j - 1]
            dp[(i, j, i + 1, j - 1)] = self.solve(i + 1, j - 1, op1, mat, i_max, j_max, out_arr, dp)

            # if (i, j, i + 1, j) in dp:
            #     return dp[(i, j, i + 1, j)]
            op2 = out
            op2 += mat[i + 1][j]
            dp[(i, j, i + 1, j)] = self.solve(i + 1, j, op2, mat, i_max, j_max, out_arr, dp)

            # if (i, j, i + 1, j + 1) in dp:
            #     return dp[(i, j, i + 1, j + 1)]
            op3 = out
            op3 += mat[i + 1][j + 1]
            dp[(i, j, i + 1, j + 1)] = self.solve(i + 1, j + 1, op3, mat, i_max, j_max, out_arr, dp)
        return out

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        out_arr = []
        i_max = len(matrix) - 1
        j_max = len(matrix[0]) - 1
        dp = {}
        for j, x in enumerate(matrix[0]):
            self.solve(0, j, matrix[0][j], matrix, i_max, j_max, out_arr, dp)
        print(out_arr)
        return min(out_arr)


obj = Solution()
# matrix = [[100, -42, -46, -41], [31, 97, 10, -10], [-58, -51, 82, 89], [51, 81, 69, -51]]
# matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
# matrix = [[-19, 57], [-40, -5]]
matrix = [[-48]]
print(obj.minFallingPathSum(matrix))
# [15, 16, 14, 15, 16, 14, 15, 13, 14, 15, 13, 14, 15, 16, 17, 15, 16]
# [15, 16, 29, 31, 16, 23, 22, 44, 30, 30, 37]
