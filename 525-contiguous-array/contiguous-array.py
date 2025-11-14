class Solution:
    def findMaxLength(self, nums):
        prefix = 0
        store = {0 : -1}     
        maxLen = 0
        
        for i , num in enumerate(nums):
            if num == 0:
                prefix -= 1
            else:
                prefix += 1
            
            if prefix in store:
                length = i - store[prefix]
                if length > maxLen:
                    maxLen = length
            else:
                store[prefix] = i
        
        return maxLen

        