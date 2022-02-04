# https://leetcode.com/problems/paint-house/

from typing import List
import copy


class Solution:
    """
    Approach ->
    1. keep track of total cost by adding min of the available choices, for curr row that we are processing
    2. As we can't paint same color to the adjacent house, so we will remove previous selected color from the choices
    3. at last, in induction step, we need to add the min cost of last house in ans.
    """

    def solve(self, costs, curr_row_i, prev_color_i, total_cost, dp):
        if curr_row_i == len(costs):
            return 0

        curr_row = costs[curr_row_i]
        curr_row_copy = copy.copy(curr_row)
        del curr_row_copy[prev_color_i]
        if (total_cost, curr_row_i, prev_color_i) in dp:
            return dp[(total_cost, curr_row_i, prev_color_i)]

        dp[(total_cost, curr_row_i, prev_color_i)] = total_cost + min(
            self.solve(costs, curr_row_i + 1, 0, curr_row_copy[0], dp),
            self.solve(costs, curr_row_i + 1, 1, curr_row_copy[1], dp)
        )
        return dp[(total_cost, curr_row_i, prev_color_i)]

    def minCost(self, costs: List[List[int]]) -> int:
        first_row = costs[0]
        curr_row_i = 0
        dp = {}
        # need to add the min cost of last house(part of induction step), and solve function is responsible to provide
        # the min cost of n-1 house
        total_cost = min(costs[-1]) + min(self.solve(costs, curr_row_i + 1, 0, first_row[0], dp),
                                          self.solve(costs, curr_row_i + 1, 1, first_row[1], dp),
                                          self.solve(costs, curr_row_i + 1, 2, first_row[2], dp))
        return total_cost


obj = Solution()
# costs = [[7, 6, 2]]
# costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
# costs = [[17, 2, 17], [8, 4, 10], [6, 3, 19], [4, 8, 12]]
costs = [[3, 5, 3], [6, 17, 6], [7, 13, 18], [9, 10, 18]]
print(obj.minCost(costs))
