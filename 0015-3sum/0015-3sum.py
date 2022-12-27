class Solution:            
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i-1] == nums[i]:
                continue
                
            k = len(nums)-1
            j = i+1
            
            while j<k:     
                s = nums[i] + nums[j] + nums[k]

                if s>0:
                    k -=1
                elif s<0:
                    j +=1
                else:
                    answer.append([nums[i],nums[j],nums[k]])
                    j+=1

                    while nums[j] == nums[j-1] and j<k:
                        j+=1 
        
        return answer
        
        

        