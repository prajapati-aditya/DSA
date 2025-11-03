class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ''' we use monotonic stack '''
        stack = []
        next_great = { }
        for num in nums2 :
            while stack and num > stack[-1] :
                val = stack.pop()
                next_great[val] = num
            stack.append(num)
        # store -1 for other elements in stack, since they have no greater element
        for num in stack :
            next_great[num] = -1
        # now we'll return the required array of output acc to nums1 in dictionary
        res = []
        for num in nums1 :
            res.append(next_great[num])
        return res