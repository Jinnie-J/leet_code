class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        arr=[]
        left=0
        right=0

        def backtrack(arr,left,right):
            if len(arr) == 2 * n:
                answer.append("".join(arr))
                return
            if left < n:
                arr.append("(")
                backtrack(arr, left+1, right)
                arr.pop()
            if right < left:
                arr.append(")")
                backtrack(arr, left, right+1)
                arr.pop()

        
        backtrack(arr,left,right)
        return answer