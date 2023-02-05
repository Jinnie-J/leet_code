class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d={}
        for i in range(len(mat)):
            d[i]= sum(mat[i])
            
        sorted_d = sorted(d.items(), key=lambda x: x[1])

        answer = []
        for i in range(k):
            answer.append(sorted_d[i][0])
        
        return answer