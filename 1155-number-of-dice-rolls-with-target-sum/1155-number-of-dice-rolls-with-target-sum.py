class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        mod = 10**9+7
        dp = [[0]*(target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        if target < 1 or target > n*k: return 0
        
        for x in range(1, n + 1):
            for y in range(1, k + 1):
                for z in range(y, target + 1):
                    dp[x][z] = (dp[x][z] + dp[x-1][z-y]) % mod
        return dp[-1][-1]