class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        set_nums=set(nums)

        new_list=list(set_nums)
        new_list.sort(reverse=True)
        return new_list[:k]

        