"""
Approach:
- This code utilizes dynamic programming to solve the knapsack problem, aiming to determine the maximum value achievable with a given maximum weight limit.
- It initializes a 2D array, dp, to store the maximum values for different combinations of items and weight limits.
- The algorithm iterates through each item and each weight limit, computing the maximum value achievable considering whether to include or exclude the current item.
- The function returns the maximum value that can be achieved with the provided weight limit.
"""

def maximum_value(max_weight, items):
    n = len(items)
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, max_weight + 1):
            if items[i - 1]["weight"] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1]["weight"]] + items[i - 1]["value"])
            else:
                dp[i][j] = dp[i - 1][j]
                
    return dp[n][max_weight]
