class Solution:
    def mySqrt(self, x: int) -> int:
        if x <2:
            return x
        left, right = 1, x // 2
        ans = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Check if mid squared is equal to x
            if mid == x // mid:
                return mid
            # If mid squared is greater than x, narrow down the left half
            elif mid > x // mid:
                right = mid - 1
            # If mid squared is less than x, narrow down the right half
            else:
                ans = mid  # Save mid as a potential lower bound result
                left = mid + 1
                
        return ans               