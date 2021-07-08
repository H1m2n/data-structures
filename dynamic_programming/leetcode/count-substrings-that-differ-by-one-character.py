class Solution:
    def get_possible_seq(self, s, out, seq_list):
        if len(s) == 0:
            return
        op1 = out
        if len(op1) > 0:
            seq_list.add(op1)
        op1 += s[0]
        self.get_possible_seq(s[1:], op1, seq_list)

        op2 = out
        # we can't have choice to not include next letter, if out is not empty
        # so we have choice to not include only if previous out is empty
        if len(op2) == 0:
            self.get_possible_seq(s[1:], op2, seq_list)

    def countSubstrings(self, s: str, t: str) -> int:
        seq_list = set()
        self.get_possible_seq(s, '', seq_list)

        max_substr_len = len(s) - 1


obj = Solution()
s = 'aba'
t = 'baba'
obj.countSubstrings(s, t)
# {'a', 'b', 'ab'}
