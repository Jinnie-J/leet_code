from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d= {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        }
        
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
        