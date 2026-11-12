class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while(low < high):
            capacity = (low+high)//2

            #count how many days are needed in this capacity
            days_needed = 1
            load = 0
            for w in weights:
                if load + w > capacity:
                    days_needed+=1
                    load = 0
                load+=w
            if days_needed <= days:
                high = capacity
            else:
                low = capacity + 1
        return high                    