class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        l=0
        n = len(height)
        r = n-1

        while(l<=r):
            h = min(height[l],height[r])
            w = r-l
            area = h*w
            max_area = max(area, max_area)
            if (height[l]<= height[r]):
                l+=1
            else:
                r-=1    
        return max_area        

