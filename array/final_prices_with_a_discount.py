class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        # i = 2, j > 2 and prices[j] <= prices[i]
        # buy_amount = price[i] - price[j]

        # we need to use stack here
        i = len(prices) - 1
        final_prices = []
        e_stack = []
        while i >= 0:
            if len(e_stack) == 0:
                # last item can't have any discount
                final_prices.append(prices[i])
            elif len(e_stack) > 0:
                # pop until we don't get prices[j] < prices[i]
                tmp_stack = e_stack
                while len(e_stack) > 0 and e_stack[-1] > prices[i]:
                    e_stack.pop()

                if len(e_stack) == 0:
                    # we don't get any discount
                    final_prices.append(prices[i])
                else:
                    print(prices[i], e_stack[-1])
                    final_prices.append(prices[i] - e_stack[-1])
                e_stack = tmp_stack

            e_stack.append(prices[i])
            i -= 1
        final_prices.reverse()
        return final_prices


prices = [8, 4, 6, 2, 3]
obj = Solution()
print(obj.finalPrices(prices))
