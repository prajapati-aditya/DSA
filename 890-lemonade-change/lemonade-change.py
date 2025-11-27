class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0
        count10 = 0
        
        for b in bills :
            if b == 5 :
                count5 += 1
            # 
            elif b == 10 :
                # check 5's change
                if count5 <= 0 :
                    return False
                count10 += 1
                count5 -= 1
            #
            else :
                if count10 >= 1 and count5 >=1 :
                    count10 -= 1
                    count5 -= 1
                elif count5 >= 3 :
                    count5 -= 3
                    
                else : # ( count10 < 1 and count5 <1 ) or (count5 <3) :
                    return False 
            
        return True