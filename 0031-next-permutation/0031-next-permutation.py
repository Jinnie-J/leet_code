class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        #134652 -> 135642 -> 135246
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]: #뒤에부터 확인해서 뒤에 수가 더 크면
                start = i-1 #그 수가 기준 (4)
            
                for k in range(len(nums)-1, start, -1):
                    if nums[k] > nums[start]: #뒤부터 확인해서 start보다 큰 수가 있으면 바꿔주기
                        end = k #5
                        nums[start], nums[end] = nums[end], nums[start] #4,5 바꾸기

                        #역순으로
                        for m in range(int((len(nums) - start)/2)):
                            nums[start+1+m], nums[len(nums)-1-m] = nums[len(nums)-1-m], nums[start+1+m]

                        break
                break
            if i==1:
                nums.reverse()
        