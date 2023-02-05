class Solution:
    def bitwiseComplement(self, n: int) -> int:
        answer=''
        
        binaryNum = format(n, 'b')
        
        for x in binaryNum:
            answer +='1' if x=='0' else '0'
        
        return int(answer, 2)
        
