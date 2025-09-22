def longest_increasing_subsequence(arr):
    dp = [1] * len(arr)
    for i in range(len(arr)):
        j = 0
        for j in range(i):
            # put <= in the if statement for longest non-decreasing subsequence
            if arr[j] < arr[i]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)


arr = [-1, 3, 4, 5, 2, 2, 2, 2]

print(longest_increasing_subsequence(arr))
