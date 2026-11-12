class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        while (low<high):
            speed = (low + high)//2

            hour = 0
            for pile in piles:
                hour+=(pile+speed-1)//speed
                if hour > h:
                    break
            #if koko finishes in time try a lesser speed
            if hour <= h:
                high = speed
            #otherwise koko needs to eat faster    
            else:
                low = speed +1
        return low            

