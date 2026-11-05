class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        remainder_counts = defaultdict(int)
        remainder_counts[0] = 1
    
        prefix_sum = 0
        total_subarr = 0

        for num in nums:
            prefix_sum+=num

            remainder = prefix_sum % k
            if remainder in remainder_counts:
                total_subarr+=remainder_counts[remainder]

            remainder_counts[remainder]+=1
        return total_subarr        