class Solution:
    def reverseWords(self, s: str) -> str:
        
        arr = s.split(" ")
        
        for i in range(len(arr)):
            tmp=""
            for index in range(len(arr[i])-1,-1,-1):
                tmp += arr[i][index]
            arr[i]= tmp
            
        return ' '.join(arr)
        