class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(arr=[],left=0,right=0):
            if len(arr) == 2 * n:
                ans.append("".join(arr))
                return
            if left < n: # '('가 가능하다면
                arr.append("(")
                backtrack(arr, left+1, right)
                arr.pop()
            if right < left: # ')'가 가능하다면
                arr.append(")")
                backtrack(arr, left, right+1)
                arr.pop()
        backtrack()
        return ans