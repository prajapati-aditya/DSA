class Solution:
    def largestOddNumber(self, num: str) -> str:
        check = set ( ("1", "3", "5", "7", "9") )
        for i in range (len(num)-1, -1, -1) :
            if num[i] in check :
                return num[0:i+1]
        return ""