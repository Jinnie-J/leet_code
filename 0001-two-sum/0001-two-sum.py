class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for index, value in enumerate(nums):
            if value in dict_nums: 
                return [index, dict_nums[value]]
            
            dict_nums[target - value] = index
