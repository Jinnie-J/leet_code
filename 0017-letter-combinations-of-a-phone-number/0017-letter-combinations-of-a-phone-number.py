from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={}
        d['2']=['a','b','c']
        d['3']=['d','e','f']
        d['4']=['g','h','i']
        d['5']=['j','k','l']
        d['6']=['m','n','o']
        d['7']=['p','q','r','s']
        d['8']=['t','u','v']
        d['9']=['w','x','y','z']
        
        if not digits:
            return []
        
        digits_arr=list(digits)
        
        answer_arr=[]
        for digits in digits_arr:
            answer_arr.append(d[digits])
        
        result = list(product(*answer_arr))
        answer= []
        for item in result:
            answer.append(''.join(item))
        
        return answer
        