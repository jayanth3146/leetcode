class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return -1
        left = max(nums)
        right = sum(nums)
        result = right
        while(left<=right):
            mid = (left+right)//2
            subarray_count = 1
            current_sum = 0
            for num in nums:
                if current_sum + num <= mid:
                    current_sum+=num
                else:
                    subarray_count +=1
                    current_sum = num

                    if subarray_count >k:
                        break
            if subarray_count <= k:
                result = mid
                right = mid-1
            else:
                left = mid+1
        return result             


