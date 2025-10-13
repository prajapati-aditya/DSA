class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [ ]
        seen = set ()
        for num in nums1 :
            if num not in seen :
                seen.add(num)
        for num in nums2 :
            if num in seen and num not in res :
                res.append(num)
        return res

        