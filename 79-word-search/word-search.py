class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row , col = len(board) , len( board[0])

        def backtrack (r,c,i) :
            if i == len(word) :     #reached end of target word
                return True
            
            if ( r < 0 or c < 0 or
                 r >= row or c >= col or
                 word[i] != board[r][c] or
                 board[r][c] == '$' ) :
                return False

            temp = board[r][c]      # store curr value
            board[r][c] = '$'       # marked as read

            res = ( backtrack(r+1,c,i+1) or      
                    backtrack(r-1,c,i+1) or
                    backtrack(r,c+1,i+1) or
                    backtrack(r,c-1,i+1) )
            
            board[r][c] = temp      #reset the value marked
            return res
        
        for r in range(row) :
            for c in range(col) :
                if board[r][c] == word[0] and backtrack(r,c,0) :
                    return True
        return False