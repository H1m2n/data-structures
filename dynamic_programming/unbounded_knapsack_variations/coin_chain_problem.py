# problem statement:
# We have an array where we have given n no of coins, we need to find out no of ways for which
# we can have target amount
# coins = [1, 2, 3]
# target amount = 5


# no of ways ->
# [2, 3] = 2 + 3 = 5
# [1, 1, 3] = 1 + 1 + 3 = 5
# [1, 1, 1, 2] = 1 + 1 + 1 + 2 = 5
# [1, 1, 1, 1, 1] = 5
# [1, 2, 2] = 5

# so for given problem we can have 5 no of ways
# as we can see here we don't have any restriction that how many times we are selecting a coin
# so this is a type of unbound problem

# as we need to create subsets for which if we do sum then it should give us a given amount
# so this problem is looks like unbounded subset problem

def coin_chain_problem(coins, amount):
    n = len(coins) + 1
    w = amount + 1
    t = [[None for i in range(w)] for j in range(n)]
    for i, row in enumerate(t):
        for j, col in enumerate(row):
            if i == 0 and j > 0:
                t[i][j] = 0
            if i >= 0 and j == 0:
                t[i][j] = 1

    for i, row in enumerate(t):
        for j, col in enumerate(row):
            if i == 0 or j == 0:
                continue

            if coins[i - 1] <= j:
                t[i][j] = t[i - 1][j] + t[i][j - coins[i - 1]]
            else:
                t[i][j] = t[i - 1][j]
    return t[i][j]


coins = [1, 2, 3]
amount = 5
print(coin_chain_problem(coins, amount))
