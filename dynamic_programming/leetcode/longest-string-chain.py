# https://leetcode.com/problems/longest-string-chain/
from typing import List


class Solution:
    def subseq(self, s1, s2, i, j, dp):
        if i == 0 or j == 0:
            return 0

        if (i, j) in dp:
            return dp[(i, j)]

        if s1[i - 1] == s2[j - 1]:
            dp[(i, j)] = 1 + self.subseq(s1, s2, i - 1, j - 1, dp)
        else:
            dp[(i, j)] = max(self.subseq(s1, s2, i - 1, j, dp), self.subseq(s1, s2, i, j - 1, dp))
        return dp[(i, j)]

    def longestStrChain(self, words: List[str]) -> int:
        """
        Approach -> As, we know chain is possible for 2 words s1 and s2, if len(s1) - 1 == len(s2)
        why so? because exactly one char is missing
        1. so first we will sort the word array on basis of length
        2. get longest common subsequence for s1 and s2, if len(LCS) == s1, where len(s1) < len(s2), then increase the
           chain count
        3. at last return the final count
        """
        i, j = (0, 1)
        words.sort(key=lambda x: len(x))
        print(words)
        count = 1  # as a single word can also be the part of chain
        while j < len(words):
            # print(i, j)
            lcs_count = 0
            if len(words[i]) + 1 == len(words[j]):
                lcs_count = self.subseq(words[i], words[j], len(words[i]), len(words[j]), {})
            if lcs_count == len(words[i]):
                print('herre', words[i], words[j])
                count += 1
                j += 1
                i = j - 1
            else:
                j += 1
        return count


obj = Solution()
# words = ["a", "b", "ba", "bca", "bda", "bdca"]
# words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
# words = ["abcd", "dbqca"]
# words = ["bdca", "bda", "ca", "dca", "a"]
# words = ["a", "pa", "zxa", "dca", "bdca"]
# words = ["a","b","ba","abc","abd","bdca"]
# words = ["a", "b", "ba", "bca", "bda", "bdca"]
words = ["a","ab","ac","bd","abc","abd","abdd"]
print(obj.longestStrChain(words))
# s1 = 'pcxbc'
# s2 = 'pcxbcf'
# print(obj.is_subseq(s1, s2, len(s1), len(s2), {}))
