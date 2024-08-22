#!/usr/bin/python3
"""Making change"""


def makeChange(coins, total):
    """Returns fewest number of coins needed to meet total"""
    if total <= 0:
        return 0
    # Initialize DP array with infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    # Iteraction through all amounts from 1 to total
    for amount in range(1, total + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
        # if the dp[total] still infinity, cannot form amount
        return dp[total] if dp[total] != float('inf') else -1
