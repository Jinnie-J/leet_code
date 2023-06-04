class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        startingPos = -1
        endingPos = -1
        m = len(nums)
        
        if (m != 0) and (target >= nums[0]) and (target <= nums[m-1]):
            for i in range(m):
                if startingPos == -1:
                    if nums[i] == target:
                        startingPos = i
                        endingPos = i    
                elif nums[i] == target:
                    endingPos = i
                else:     
                    break
        return [startingPos, endingPos]