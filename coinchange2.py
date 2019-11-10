from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(0, amount+1)]
        dp[0] = 1
        
        for coin in coins:
            for a in range(1, amount+1):
                if coin <= a:
                    dp[a] += dp[a - coin]
        return dp[amount]