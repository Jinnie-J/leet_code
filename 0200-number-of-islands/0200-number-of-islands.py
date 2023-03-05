class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    cnt += 1
        return cnt

        
    def dfs(self, grid, x, y):
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                grid[nx][ny]='0'
                self.dfs(grid,nx,ny)
        