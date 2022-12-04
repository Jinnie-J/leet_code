class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for i, v in enumerate(nums):
            if v in dict_nums: return [i, dict_nums[v]]
            dict_nums[target - v] = i