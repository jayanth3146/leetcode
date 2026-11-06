class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        global_prod = nums[0]
        max_prod = nums[0]
        min_prod = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_prod,min_prod = min_prod,max_prod

            max_prod = max(num, max_prod*num)
            min_prod = min(num, min_prod*num)

            global_prod = max(global_prod, max_prod)
        return global_prod    
