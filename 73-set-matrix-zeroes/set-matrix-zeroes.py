class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.  okkkkk
        """
        row = len(matrix)
        rowFlag = False     # checks if fisrt row has to be made 0 or not
        col = len(matrix[0])
        colFlag = False

        " updating row and col flag"
        for i in range(col) :
            if matrix[0][i] == 0 :
                rowFlag = True

        for i in range(row) :
            if matrix[i][0] == 0 :
                colFlag = True
        " now make the first row col 0 of those element which is zero"
        for i in range(row) :
            for j in range(col) :
                if matrix[i][j] == 0 :
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        " we update everywhere except first row and col"
        for i in range(1,row) :
            for j in range(1,col) :
                if matrix[0][j] == 0 or matrix[i][0] == 0 :
                    matrix [i][j] = 0
        " now according to flag update first row and col"
        if rowFlag :
            for i in range(col) :
                matrix[0][i] = 0
        if colFlag :
            for i in range(row) :
                matrix[i][0] = 0
        return matrix