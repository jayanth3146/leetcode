class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1}
        current_sum = 0
        total_subarr = 0
        for num in nums:
            current_sum+=num

            diff = current_sum - k
            if diff in prefix_sum:
                total_subarr+=prefix_sum[diff]

            #record the current running sum in hashmap
            prefix_sum[current_sum] = prefix_sum.get(current_sum,0)+1
        return total_subarr        