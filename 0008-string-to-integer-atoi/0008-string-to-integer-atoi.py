class Solution:
    def myAtoi(self, s: str) -> int:
        s.lstrip()
        answer = 0
        minus = False
        first = True
        
        for st in s:
            if st == ' ' and first == True:
                s.lstrip()
                continue
            elif (st == '+' or st == '-') and first == True:
                if st=='-':
                    minus = True
                if first == True:
                    first = False
                    
            elif '0' <= st <= '9':
                answer *= 10
                answer += int(st)
                if first == True:
                    first = False
            else:
                break
                
        if minus:
            answer *= -1
            
        if answer > 2**31-1:
            answer = 2**31-1
        elif answer < -2**31:
            answer = -2**31
            
        return answer
        