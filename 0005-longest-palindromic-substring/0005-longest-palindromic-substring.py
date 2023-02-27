class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s)<2 or s == s[::-1]:
            return s
        
        def palindrom(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        
        
        answer=""
        for i in range(len(s)-1):
            answer = max(answer, palindrom(i,i+1), palindrom(i,i+2), key = len)
            
        return answer
            
        