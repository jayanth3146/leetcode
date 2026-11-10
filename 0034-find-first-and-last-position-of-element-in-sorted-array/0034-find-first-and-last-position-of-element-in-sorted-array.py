class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
         # Helper function to find either the first or last position
        def find_bound(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid  # Record the candidate index
                    if is_first:
                        right = mid - 1  # Lock down the left half for earlier occurrences
                    else:
                        left = mid + 1   # Lock down the right half for later occurrences
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound

        # Return both the leftmost and rightmost indices
        return [find_bound(True), find_bound(False)]      
            
        
        
                                