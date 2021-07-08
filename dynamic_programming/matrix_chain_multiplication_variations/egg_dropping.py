class Solution:
    def solve(self, e, f, dp):
        # base condition
        if f == 0 or f == 1:
            # if floor is not given or only one floor is available, then we simply return f as a min no of attempts
            return f
        if e == 1:
            # in worst case egg is suppose not broken, to check it we need to throw egg from each floor,
            # so min no of attempts will be f
            return f

        if (e, f) in dp:
            return dp[(e, f)]

        min_attempts = 1001
        for i in range(1, f + 1):
            # if egg is broken at particular floor, then we need to go downside for further checking by egg having e-1
            low = self.solve(e - 1, i - 1, dp)
            # if egg is not broken, then we can move up on the floor and can reuse egg
            high = self.solve(e, f - i, dp)
            # to determine the min attempt by using all eggs efficiently, we need to check worst case possibility
            # that's why for eac attempt we need to calculate for max
            attempts = 1 + max(low, high)
            if min_attempts > attempts:
                min_attempts = attempts
        dp[(e, f)] = min_attempts
        return dp[(e, f)]

    def twoEggDrop(self, n: int) -> int:
        dp = {}
        return self.solve(2, n, dp)


obj = Solution()
# print(obj.twoEggDrop(2))
print(obj.twoEggDrop(100))
