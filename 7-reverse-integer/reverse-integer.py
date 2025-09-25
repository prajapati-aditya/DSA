class Solution:
    def reverse(self, x: int) -> int:
        max_int = (2 ** 31 ) - 1
        min_int = -2 ** 31

        sign = -1 if x<0 else 1
        x = x*sign
        rev = 0
        while x :
            rem = x % 10
            x = x // 10

            if rev >( max_int - rem ) //10 :
                return 0

            rev = rev*10 + rem
        return sign*rev