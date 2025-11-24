class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):            
            for j in range(len(grid)):       
                same = True                           
                for k in range(len(grid)):      
                    if grid[i][k] != grid[k][j]:
                        same = False     
                        break
                if same:
                    count += 1       

        return count