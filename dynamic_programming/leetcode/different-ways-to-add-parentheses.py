# https://leetcode.com/problems/different-ways-to-add-parentheses/
from typing import List


class Solution:

    def solve_expr(self, expression, dp):
        ans = []
        # Base case.
        if '+' not in expression and '-' not in expression and '*' not in expression:
            ans.append(int(expression))

        for i, x in enumerate(expression):
            if x in ['*', '+', '-']:
                left_substr = expression[0:i]
                right_substr = expression[i + 1:]
                if left_substr in dp:
                    left_evaluated = dp[left_substr]
                else:
                    left_evaluated = self.solve_expr(left_substr, dp)
                    dp[left_substr] = left_evaluated

                if right_substr in dp:
                    right_evaluated = dp[right_substr]
                else:
                    right_evaluated = self.solve_expr(right_substr, dp)
                    dp[right_substr] = right_evaluated
                # left_evaluated = self.solve_expr(expression[0:i], dp)
                # right_evaluated = self.solve_expr(expression[i+1:], dp)
                # as after evaluation of partition, we will get left_evaluated and right_evaluated array,
                # so we need to apply the current operator to each value between left and right evaluated values
                # that's why we looping below and evaluating expression for current operator
                for y in right_evaluated:
                    for x in left_evaluated:
                        tmp_ans = eval(str(x) + expression[i] + str(y))
                        ans.append(tmp_ans)

        return ans

    def diffWaysToCompute(self, expression: str) -> List[int]:
        dp = {}
        return self.solve_expr(expression, dp)


obj = Solution()
expr = "2*3-4*5"
# expr = "11"
expr = "2-1-1"
print(obj.diffWaysToCompute(expr))
