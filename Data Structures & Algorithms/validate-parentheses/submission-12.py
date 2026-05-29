class Solution:
    def isValid(self, s: str) -> bool:
        d1={')':'(',']':'[','}':'{'}

        stack=[]

        for char in s:
            if char in d1 and stack and  d1[char]==stack[-1] :
                stack.pop()
            else:
                stack.append(char)
        return stack==[]
        
                