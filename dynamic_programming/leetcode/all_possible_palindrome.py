from typing import List


class Solution:
    def is_palindrome(self, s):
        i, j = (0, len(s) - 1)
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def solve(self, s, op, res):
        if len(op) != 0 and self.is_palindrome(op):
            res.append(op)
        if len(s) == 0:
            return

        # picking is always available
        op1 = op
        op1 += s[0]
        self.solve(s[1:], op1, res)

        # while, we can't leave a char, when we have something in previous output
        op2 = op
        if len(op2) == 0:
            self.solve(s[1:], op2, res)

    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.solve(s, '', res)
        return res


obj = Solution()
s = 'aab'
obj.partition(s)
