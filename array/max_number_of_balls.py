class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """

        # 15 = 1 + 5 = 6
        # 14 = 1 + 4 = 5
        # 13 = 1 + 3 = 4
        # 12 = 1 + 2 = 3
        # 11 = 1 + 1 = 2
        # 10 = 1 + 0 = 1
        # 9 =  9
        # 8 =  8
        # 7 =  7
        # 6 =  6
        # 5 =  5

        # loop in given range
        # for each number sum its digits and put into dictionary with respective count
        # iterate on dictionary and get the max number

        max_count = 0
        num_count = {}
        i = lowLimit
        while i <= highLimit:
            num = i
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num = num // 10
            if digit_sum not in num_count:
                num_count[digit_sum] = 1
            else:
                num_count[digit_sum] = num_count[digit_sum] + 1
            i += 1

        for num, count in num_count.items():
            if max_count < count:
                max_count = count
        return max_count


obj = Solution()
obj.countBalls()
