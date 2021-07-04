class Solution:
    dp_map = {}

    def memoized_cal(self, i, n):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if i in self.dp_map:
            return self.dp_map[i]
        self.dp_map[i] = self.memoized_cal(i + 1, n - 1) + self.memoized_cal(i + 2, n - 2)
        return self.dp_map[i]

    def recursive_cal(self, i, n):
        if n == 0:
            return 1
        if n < 0:
            return 0

        return self.recursive_cal(i + 1, n - 1) + self.recursive_cal(i + 1, n - 2)

    def climbStairs(self, n: int) -> int:
        # return self.recursive_cal(0, n)
        return self.memoized_cal(0, n)


obj = Solution()
print(obj.climbStairs(3))
print(obj.dp_map)
# {4: 1, 3: 2, 2: 3, 1: 5, 0: 8}
# {4: 1, 3: 2, 2: 4, 1: 8, 0: 16}
