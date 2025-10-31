class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1]*n for _ in range (m)]
        def path(i,j) :
            if i < 0 or j < 0 :
                return float('inf')
            if i == 0 and j == 0:
                return grid[i][j]
            if dp[i][j] != -1 :
                return dp[i][j]
            else :
                x = path(i-1,j)
                y = path(i,j-1)
                dp[i][j] = min(x,y)+grid[i][j]
                return dp[i][j]
        return path( len(grid)-1 , len(grid[0])-1 )
        