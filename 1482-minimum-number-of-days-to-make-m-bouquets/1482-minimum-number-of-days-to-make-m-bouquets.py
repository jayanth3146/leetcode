class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        left = min(bloomDay)
        right = max(bloomDay)
        ans = -1
        while left <= right:
            mid = (left+right)//2

            flower = 0
            bouquets = 0
            for bloom in bloomDay:
                if bloom<=mid:
                    flower+=1
                    if flower == k:
                        bouquets+=1
                        flower = 0
                else:
                    flower = 0
            if bouquets >= m:
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans                             
