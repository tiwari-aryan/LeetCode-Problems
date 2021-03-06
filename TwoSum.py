class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        dict_nums = {}
        for i, n in enumerate(nums):
            if target - n in dict_nums:
                return [dict_nums[target - n], i]
            dict_nums[n] = i
