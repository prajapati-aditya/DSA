class Solution:
    def smallestNumber(self, n: int) -> int:
        bits = {
            1: 1,
            2: 3,
            4: 7,
            8: 15,
            16: 31,
            32: 63,
            64: 127,
            128: 255,
            256: 511,
            512: 1023,
            1024: 2047,
        }

        prev =1 
        for bit in bits.keys() :
            if bit > n :
                return bits[prev]
            prev = bit
        return bits[1024]
        