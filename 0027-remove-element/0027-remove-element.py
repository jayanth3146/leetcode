class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0 
        
        # Iterate through the array with a fast pointer 'i'
        for i in range(len(nums)):
            # If the current element is not the target value
            if nums[i] != val:
                # Move it to the front at index k
                nums[k] = nums[i]
                # Advance the valid element pointer
                k += 1
                
        # k represents the count of elements not equal to val
        return k