class Solution:

    def digitSum(self, s: str, k: int) -> str:
        
        while len(s)>k:            
            arr= [s[i:i+k] for i in range(0, len(s), k)]

            arr_int = [int(i) for i in arr]

            tmp=[]
            for i in range(len(arr)):
                tmp.append(sum(int(j) for j in arr[i]))
             
            tmp_str = list(map(str, tmp))
            
            s = ''.join(tmp_str)
            print(s)
            
        return s
        