def knapsack(items: list[tuple], max_capacity):
    weights = []
    values = []
    n = len(items)
    for item in items:
        weights.append(item[0])
        values.append(item[1])

    dp = [[0] * (len(items)) for _ in range(max_capacity + 1)]
    for l in range(max_capacity):
        dp[0].append(0)

    for i in range(1, n + 1):
        for w in range(max_capacity + 1):
            if weights[i - 1] <= w:
                dp[w][i] = max(
                    dp[i - weights[i - 1]][w - 1] + values[i - 1], dp[i - 1][w]
                )


items = [(1, 15), (3, 20), (4, 30)]
max_capacity = 4

print(knapsack(items, max_capacity))
