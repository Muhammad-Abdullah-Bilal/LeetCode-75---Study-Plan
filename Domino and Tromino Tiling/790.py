class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * (n + 1)
        gap = [0] * (n + 1)
        
        dp[0] = 1
        if n >= 1:
            dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = (dp[i-1] + dp[i-2] + 2 * gap[i-1]) % MOD
            gap[i] = (gap[i-1] + dp[i-2]) % MOD
        
        return dp[n]

