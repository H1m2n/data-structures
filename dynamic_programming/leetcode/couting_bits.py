class Solution:
    def fib(self, n: int) -> int:
        a, b = (0, 1)
        if n == 0:
            return a
        if n == 1:
            return b

        req_num = n - 1
        while req_num > 0:
            res = a + b
            a = b
            b = res
            req_num -= 1
        return res

