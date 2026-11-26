class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows= len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    heights[c]+=1
                else:
                    heights[c]=0
            max_area = max(max_area, self.findLargestRectangle(heights))
        return max_area
    def findLargestRectangle(self, heights:list[int])->int:
        stack = []
        max_area = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index,height = stack.pop()
                max_area = max(max_area, height * (i-index))
                start = index     
            stack.append((start,h))
        for index,height in stack:
            max_area = max(max_area, height * (len(heights)- index))
        return max_area              


