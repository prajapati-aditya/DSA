class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        rr = 0      # resultant row
        max_cnt = 0
        for r in range(row) :
            count = 0
            for c in range(col) :
                if mat[r][c] == 1 :
                    count += 1
            if max_cnt < count :
                max_cnt = count
                rr = r

                
        return [rr,max_cnt]
