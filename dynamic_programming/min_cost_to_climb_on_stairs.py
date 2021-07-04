from typing import List


class Solution:
    dp = {}

    def cost_cal1(self, cost, i=0):
        print(i)
        if len(cost) == 0:
            return 0
        # if i in self.dp:
        #     return self.dp[i]
        self.dp[i] = cost[0] + min(self.cost_cal(cost[1:], i+1), self.cost_cal(cost[2:], i+2))
        i += 1
        return self.dp[i-1]

    def cost_cal(self, cost):
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])
        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])
        return min(cost[len(cost)-1], cost[len(cost)-2])

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.cost_cal(cost)


obj = Solution()
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# cost = [10, 15, 20]
print(obj.minCostClimbingStairs(cost))
print(cost)
# print(obj.dp)
