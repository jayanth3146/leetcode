class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        total_palindrome = 0

        def expand_around_center(left:int,right:int)->int:
            total = 0
            while left>=0 and right < len(s) and s[left]==s[right]:
                total+=1
                left-=1
                right+=1
            return total
        for i in range(len(s)):
            total_palindrome+=expand_around_center(i,i)
            total_palindrome+=expand_around_center(i,i+1)
        return total_palindrome    




