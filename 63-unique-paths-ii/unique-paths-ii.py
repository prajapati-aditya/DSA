class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid )
        n = len(obstacleGrid[0])
        cache = [[-1 for _ in range(n)] for _ in range(m)]

        def path(i,j) :
            if i >= m or j >= n  :
                return 0
            
            if obstacleGrid[i][j] ==1 :         # obstacle should come before value check
                return 0

            if i == m-1 and j== n-1 :
                return 1
            
            
            # check in cache fro solution ;
            if cache[i][j] != -1 :
                return cache[i][j]
            else :
                cache[i][j] = path(i , j+1) + path(i+1, j) 
                return cache[i][j] 
        return path(0 , 0 )
