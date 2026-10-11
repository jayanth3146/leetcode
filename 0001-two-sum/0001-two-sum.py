class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen1 = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen1:
                return [seen1[diff],i]
            seen1[num] = i       