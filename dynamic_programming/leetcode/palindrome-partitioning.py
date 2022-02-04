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

    def solve(self, palindrome_check_str, input, res):
        if self.is_palindrome(palindrome_check_str):
            res.append(palindrome_check_str)

            if len(input) == 0:
                return res
            print(input)
            self.solve(input[0], input[1:], res)
        return res

    def partition(self, s: str) -> List[List[str]]:
        """
        do check of palindrome for left substring
        and give right substring as a input for recursive check
        eg with "aab"
        a ab
        aa b
        aab
        """
        out_arr = []
        i, j = (0, 0)
        while j < len(s):
            res = []
            self.solve(s[i:j + 1], s[j + 1:], res)
            # print(s[i:j + 1], s[j + 1:])
            if len(res) > 0:
                out_arr.append(res)
            j += 1
        return out_arr

obj = Solution()
s = 'aaa'
print(obj.partition(s))