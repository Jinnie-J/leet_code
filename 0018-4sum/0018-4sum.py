class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(nums)

        result = set()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):

                new_target = target - nums[i] - nums[j]

                k = j+1
                l = len(nums)-1
                while l > k:
                    if new_target == nums[k] + nums[l]:
                        result.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    elif new_target > nums[k] + nums[l]:
                        k += 1
                    else:
                        l -= 1

        return list(result)