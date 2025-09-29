from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        dict1 = Counter (s)
        
        sorted_char = sorted(dict1.items(), key = lambda x : x[1], reverse =True )
        res = ""
        for ch , count in sorted_char :
            res = res+(ch*count)
        return res
        