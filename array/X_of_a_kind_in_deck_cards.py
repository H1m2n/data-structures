import collections
from typing import List
import math
from functools import reduce


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        vals = collections.Counter(deck).values()
        return reduce(math.gcd, vals) >= 2


obj = Solution()
print(obj.hasGroupsSizeX([0, 0, 0, 1, 1, 1, 2, 2, 2]))
