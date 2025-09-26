class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        l=strs[0]
        result=""
        r=strs[-1]
        for i in range(min(len(l),len(r))):
            if l[i]!=r[i]:
                return result
            
            result+= l[i]
        return result    
        



        