import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0:
            return False
        
        return math.log2(n) == math.trunc(math.log2(n))
        