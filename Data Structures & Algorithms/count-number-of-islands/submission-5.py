class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        stack = []
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "0":
                    grid[i][j] = "0"
                    
                    stack.append((i,j))

                    self.dfs(stack,grid)
                    
                    count+=1
        
        return count

    def dfs(self,stack,grid):

        adjs = [
                         (0,-1), 
                (-1,0),           (1,0),
                         (0,1)  
            ]

        while stack:

            el = stack.pop()
            for adj in adjs:

                m = el[0] + adj[0]
                n = el[1] + adj[1]

                if 0 <= m < len(grid) and 0 <= n < len(grid[0]):
                    
                    if grid[m][n] != "0":
                        grid[m][n] = "0"
                        stack.append((m,n))


