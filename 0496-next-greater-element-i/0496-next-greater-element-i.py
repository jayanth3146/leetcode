class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        greater_num = {}
        for num in nums2:
            while stack and num > stack[-1]:
                smaller_num = stack.pop()
                greater_num[smaller_num] = num
            stack.append(num)
        return [greater_num.get(num,-1) for num in nums1]        