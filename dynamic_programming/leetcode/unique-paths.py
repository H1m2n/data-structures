# https://leetcode.com/problems/unique-paths/
class SolutionBk:
    def solve(self, m, n, i, j, count):
        if i == m - 1 and j == n - 1:
            count[0] = count[0] + 1
            return count

        if i < m - 1:
            self.solve(m, n, i + 1, j, count)
        if j < n - 1:
            self.solve(m, n, i, j + 1, count)

    def uniquePaths(self, m: int, n: int) -> int:
        count_track = [0]
        self.solve(m, n, 0, 0, count_track)
        print(count_track)


class Solution:
    def solve(self, m, n, i, j, dp):
        if i == m - 1 and j == n - 1:
            return dp[(i, j)]

        if (i, j) in dp:
            dp[(i, j)] = dp[(i, j)] + 1
            return dp[(i, j)]

        if i < m - 1:
            dp[(i, j)] = self.solve(m, n, i + 1, j, dp)
        if j < n - 1:
            dp[(i, j)] = self.solve(m, n, i, j + 1, dp)
        return dp[(i, j)]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[i][j]


obj = Solution()
m = 3
n = 7
print(obj.uniquePaths(m, n))
