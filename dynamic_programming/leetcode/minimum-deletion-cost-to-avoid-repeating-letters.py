from typing import List
from collections import OrderedDict
import sys


class SolutionBk:
    def is_del_required(self, cost_map):
        prev_key = None
        no_use_keys = []
        for key, value in cost_map.items():
            idx, str_i = key
            if prev_key is None:
                prev_key = (idx, str_i)
            else:
                if prev_key[1] == str_i:
                    # if 2 adjacent values are matched, then we need to send both the keys back
                    # to decide which one to delete on basis of cost
                    return True, [prev_key, key]
                else:
                    # if not, then we will update the prev_key with curr_key, to check for next adjacent
                    # delete the previous key as it of no use to calculate the cost
                    no_use_keys.append(prev_key)
                    prev_key = (idx, str_i)
        for key in no_use_keys:
            del (cost_map[key])

        return False, None

    def pick_min_cost_key(self, key_list, cost_map):
        min_cost = sys.maxsize
        min_cost_key = None
        for key in key_list:
            if cost_map[key] < min_cost:
                min_cost_key = key
                min_cost = cost_map[key]
        return min_cost, min_cost_key

    def del_ele(self, cost_map, total_min_cost):
        # as deletion is easy on map, so we will do this process on map
        is_required, key_list = self.is_del_required(cost_map)
        if not is_required:
            return total_min_cost
        min_cost, min_cost_key = self.pick_min_cost_key(key_list, cost_map)
        total_min_cost[0] = total_min_cost[0] + min_cost
        del (cost_map[min_cost_key])
        self.del_ele(cost_map, total_min_cost)
        return total_min_cost

    def minCost(self, s: str, cost: List[int]) -> int:
        cost_map = OrderedDict()
        for i, x in enumerate(cost):
            cost_map[(i, s[i])] = x
        min_cost = self.del_ele(cost_map, [0])
        print(min_cost)
        return min_cost[0]


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        left, ans = (0, 0)
        for right in range(1, len(s)):
            if s[left] == s[right]:
                if cost[left] < cost[right]:
                    ans += cost[left]
                else:
                    ans += cost[right]
                    # If right is cheaper, delete right and kept left
                    # position for next step calculation
                    continue

            # this process is require, if cost[left] < cost[right], because now we need a new left for next comparision
            left = right
        return ans


obj = SolutionBk()
# s = "abc"
# cost = [1, 2, 3]
# s = "abaac"
# cost = [1, 2, 3, 4, 5]
s = "aabaa"
cost = [1, 2, 3, 4, 1]
s = "aabaaaa"
cost = [1, 2, 3, 4, 1, 5, 6]
obj.minCost(s, cost)
