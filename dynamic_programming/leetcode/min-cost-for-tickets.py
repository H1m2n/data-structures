from typing import List


class Solution:
    def get_new_index(self, days, curr_index, duration):
        """
        get the new index for selected day pass to buy it again
        """
        if curr_index == len(days):
            return curr_index
        end_day = days[curr_index] + duration - 1
        new_day_index = curr_index
        while new_day_index < len(days) and days[new_day_index] <= end_day:
            new_day_index += 1
        return new_day_index

    def cal_min_cost(self, day_index, days, costs, dp):
        if day_index == len(days):
            return 0
        if day_index in dp:
            return dp[day_index]
        # utilise the pass until it is not expired,
        # so each recursive call will vary in size of recursion stack, so some may finish early than others
        # because we are calculating for next indices for each available passes
        total_cost_of_1_day_pass = costs[0] + self.cal_min_cost(self.get_new_index(days, day_index, 1), days, costs, dp)
        total_cost_of_7_day_pass = costs[1] + self.cal_min_cost(self.get_new_index(days, day_index, 7), days, costs, dp)
        total_cost_of_30_day_pass = costs[2] + self.cal_min_cost(self.get_new_index(days, day_index, 30), days, costs,
                                                                 dp)
        dp[day_index] = min(total_cost_of_1_day_pass, total_cost_of_7_day_pass, total_cost_of_30_day_pass)
        return dp[day_index]

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        return self.cal_min_cost(0, days, costs, dp)


obj = Solution()
days = [1, 4, 8, 12, 16, 18, 24, 30]
costs = [2, 7, 15]
# days = [1, 4, 6, 7, 8, 20]
# costs = [2, 7, 15]
print(obj.mincostTickets(days, costs))
