class Solution:
        def removeDuplicates(self, s: str) -> str:
            stack = []
        
            for char in s:
            # If the stack is not empty and the current character 
            # matches the top of the stack, remove the duplicate.
                if stack and stack[-1] == char:
                    stack.pop()
                else:
                    stack.append(char)
                
            return "".join(stack)
        