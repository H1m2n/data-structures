# hypothesis and base condition work together, can be easily explained by comment in base condition
# to get the intermediate output, we need to store that output somewhere like  dp[n] = 1 + self.helper(n, dp)
# It is important to return a value from the function, if we expect intermediate results to store

class Solution:
    def helper(self, n, dp):
        # base condition
        if n == 1:
            # need to return -1, beacuse we are incrementing while storing steps for a particular no in hypothesis step,
            # and in base case if n == 1, then steps should be 0
            return -1

        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        # hypothesis step
        if n in dp:
            return dp[n]
        dp[n] = 1 + self.helper(n, dp)
        # induction step
        return dp[n]

    def cal_power(self, lo, hi):
        """
        Function to calculate power list for each range no
        """
        power_list = []
        dp = {}
        for x in range(lo, hi + 1):
            if x in dp:
                power_list.append((x, dp[x]))
            else:
                dp[x] = 1 + self.helper(x, dp)
                power_list.append((x, dp[x]))
        return power_list

    def getKth(self, lo: int, hi: int, k: int) -> int:
        """
        Approach ->
        1. get the no of steps by using recursion
        2. for calculating any step further for a number, if it is already available in dp, then get from there otherwise calculate
        3. After getting power of each range no, sort it on first power and then on number
        4. Go to kth location and return the answer
        """
        power_list = self.cal_power(lo, hi)
        sorted_power_list = sorted(power_list, key=lambda x: (x[1], x[0]))
        return sorted_power_list[k - 1][0]


obj = Solution()
lo = 12
hi = 15
k = 2
print(obj.getKth(lo, hi, k))
# dp = {}
# obj.helper(12, dp)
# print('********')
# print(dp)
