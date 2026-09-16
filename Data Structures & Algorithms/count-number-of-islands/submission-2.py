class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        adjs = [
                         (0,-1), 
                (-1,0),           (1,0),
                         (0,1)  
            ]

        stack = []
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "0":
                    grid[i][j] = "0"
                    
                    stack.append((i,j))

                    while stack:
                        el = stack.pop()
                        for adj in adjs:
                            if el[0] + adj[0] >= 0 and el[0] + adj[0] < len(grid) and el[1] + adj[1] >=0 and el[1] + adj[1] < len(grid[0]):
                                if grid[el[0] + adj[0]][el[1]+ adj[1]] != "0":
                                    grid[el[0] + adj[0]][el[1]+ adj[1]] = "0"

                                    stack.append((el[0] + adj[0],el[1] + adj[1]))

                    count+=1
        
        return count