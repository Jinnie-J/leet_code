from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d= {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        result = []
        
        def combi(index, cur):
            if index == len(digits):
                if len(cur) > 0:
                    result.append(''.join(cur))
                return
            for ch in d[digits[index]]:
                cur.append(ch)
                combi(index+1, cur)
                cur.pop()
        
        combi(0, [])
        
        return result