class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        n = len(dist)
        if hour<=n-1:
            return -1

        def can_react_on_time(speed: int)->bool:
            total_time = 0.0

            #for all the trains except the last, round up to the next integer hour'
            for i in range(n-1):
                total_time+=math.ceil(dist[i]/speed)
            total_time+=dist[-1]/speed

            return total_time <= hour

        left = 1
        right = 10**7
        ans = -1
        while(left <= right):
            mid = (left+right)//2

            if can_react_on_time(mid):
                ans = mid
                right = mid  -1
            else:
                left =mid+1
        return ans            
