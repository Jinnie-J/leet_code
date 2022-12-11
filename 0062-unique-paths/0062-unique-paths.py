class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp= [[0]*n for i in range(m)]
        
        dx=[-1,0]
        dy=[0,-1]
        
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j]=1
                    continue
                
                for k in range(2):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    
                    if 0<=nx<m and 0<=ny<n:
                        dp[i][j] += dp[nx][ny]
                
        print(dp)
        return dp[m-1][n-1]
                    
                
                