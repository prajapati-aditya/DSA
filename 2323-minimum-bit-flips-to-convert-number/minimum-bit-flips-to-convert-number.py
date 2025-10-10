class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # xor start and goal 
        # wherever bits are diff . they become 1. so count that bits
        return (start ^ goal).bit_count()
        