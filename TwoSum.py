class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for i, num in enumerate(nums):
            print(i, num)
            if target - num in nums:
                print(i, num)
