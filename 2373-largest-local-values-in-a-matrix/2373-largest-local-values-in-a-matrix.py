class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(grid)
        cols = len(grid[0])
        
        resMatrix = [[0]*(cols-2) for _ in range(rows-2)]
        
        for c in range(cols-2):
            for r in range(rows-2):
                
                mx=[]
                currMax=0
                for i in range(r,r+3): 
                    res=grid[i][c:c+3]
                    curr = max(res)
                    currMax=max(curr,currMax)
                
                    
                resMatrix[r][c]=currMax
                
        return resMatrix