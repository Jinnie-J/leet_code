class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]  
        cnt = 0
        queue = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    cnt += 1
                    queue.append([i, j])
                    grid[i][j] = 0
                    
                while queue:
                    x, y = queue.pop(0)
                    
                    for curr_dir in dir:
                        nx = x + curr_dir[0]
                        ny = y + curr_dir[1]
                        
                        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                            continue
                            
                        if grid[nx][ny] == "1":
                            queue.append([nx, ny])
                            grid[nx][ny] = 0
        return cnt                    
