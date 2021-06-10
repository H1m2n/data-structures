# Problem statement: I have stock prices of a particular company on consecutive days.
# I need to find the count of consecutive days(include the current days as well) where the stock price is less than or
# equal to the current day price
#
# Stock price of day 1 to day 7
# eg:  [100, 80, 60, 70, 60, 75, 85]
# out: [1,   1,   1,  2,  1,  4,  6]

# Explanation: we need to found consecutive smaller price, so if we can found nearest left greater price
# then we can solve this problem easily with stack
# Now for consecutive count we need to calculate using indexes let say for eg: for day 7 the stock price is 85
# and index is 6. for day 7 price we found nearest greater element 100 at index 0
# so the day count will be 6 - 0 = 6


def stock_span_problem(nums):
    nearest_greater_ele = []
    e_stack = []  # in stack we need to store index of the element as well, so (ele, i)
    for i in range(0, len(nums), 1):
        if len(e_stack) == 0:
            nearest_greater_ele.append((-1, -1))
        elif len(e_stack) > 0 and nums[i] < e_stack[-1][0]:
            nearest_greater_ele.append(e_stack[-1])
        elif len(e_stack) > 0 and nums[i] > e_stack[-1][0]:
            while len(e_stack) > 0 and nums[i] > e_stack[-1][0]:
                e_stack.pop()

            if len(e_stack) == 0:
                nearest_greater_ele.append((-1, -1))
            else:
                nearest_greater_ele.append(e_stack[-1])
        e_stack.append((nums[i], i))

    stock_span = []
    for i in range(0, len(nums), 1):
        _nearest_greater_ele = nearest_greater_ele[i]
        if _nearest_greater_ele[1] == -1:
            # this means we don't found any consecutive smaller so for this output will be 1
            stock_span.append(1)
        else:
            stock_span.append(i - _nearest_greater_ele[1])
    return stock_span


nums = [100, 80, 60, 70, 60, 75, 85]
# [-1, 100, 80, 80, 70, 80, 100]
print(stock_span_problem(nums))
