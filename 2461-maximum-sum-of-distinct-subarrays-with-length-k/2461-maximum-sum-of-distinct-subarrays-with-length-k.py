class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        max_sum = 0
        current_sum = 0
        freq = {}
        left = 0
        
        for right in range(len(nums)):
            # Add the incoming element to the window
            current_sum += nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            
            # If the window size exceeds k, shrink it from the left
            if right - left + 1 > k:
                left_num = nums[left]
                current_sum -= left_num
                freq[left_num] -= 1
                if freq[left_num] == 0:
                    del freq[left_num]
                left += 1
            
            # When the window hits exactly length k, check if all elements are distinct
            if right - left + 1 == k:
                if len(freq) == k:
                    max_sum = max(max_sum, current_sum)
                    
        return max_sum         
