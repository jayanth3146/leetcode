class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l=0
        min_length = float("inf")
        sum1 = 0
        for r in range(len(nums)):
            sum1+=nums[r]
            while(sum1>=target):
                min_length = min(min_length, r-l+1)
                sum1-=nums[l]
                l+=1
        return min_length if min_length != float("inf") else 0        