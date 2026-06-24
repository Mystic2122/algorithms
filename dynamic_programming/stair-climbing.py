def climbStairs(costs):
    for i in range(2, len(costs)):
        costs[i] += min(costs[i-1], costs[i-2])
    return min(costs[-1],costs[-2])