class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n= len(nums)
        res = [-1]*n
        stack = []
        for i in range(2*n):
            current_sum = nums[i % n]
            while stack and nums[stack[-1]] < current_sum:
                res[stack.pop()] = current_sum
            if i < n:
                stack.append(i)
        return res            