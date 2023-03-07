class Solution:
    def reverse(self, x: int) -> int:
        answer = 0
        sign = 1
        
        if x < 0:
            sign = -1
            x = x * -1
            
        while x > 0:
            rem = x % 10
            answer = answer * 10 + rem
            x = x // 10
            
        if -2147483648 < answer < 2147483648: 
            return answer * sign
        else:
            return 0