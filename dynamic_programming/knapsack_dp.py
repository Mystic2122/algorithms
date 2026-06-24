# 0/1 knapsack problem
def knapsack(items: list[tuple], max_capacity):
    weights = []
    values = []
    n = len(items)
    for item in items:
        weights.append(item[0])
        values.append(item[1])

    dp = [[0] * (max_capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(max_capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
                
    return dp[n][max_capacity]

items = [(1, 15), (3, 20), (4, 30)]
max_capacity = 4

print(knapsack(items, max_capacity))
