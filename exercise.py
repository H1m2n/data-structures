# robbery question
def rob(nums):
    rob1, rob2 = 0, 0

    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

def rob1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    start_indexes = {
        0: 0,
        1: 0
    }
    for start_index, amount in start_indexes.items():
        # total_money = []
        print("start index - {}".format(start_index))
        for i, x in enumerate(nums[start_index:]):
            try:
                if not ((i + 1) % 2 == 0):
                    amount = amount + x
                    print(amount)
            except:
                pass
        start_indexes[start_index] = amount

    robbery_amount = 0
    for start_index, amount in start_indexes.items():
        if robbery_amount < amount:
            robbery_amount = amount
    return robbery_amount


print(rob([1,2,3,1]))
print(rob([2,1,1,2]))