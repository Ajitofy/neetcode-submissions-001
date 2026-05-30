class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        res = sorted(zip(position,speed),reverse=True)
        for pos,sp in res:
            time = (target-pos)/sp
            stack.append(time)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
            
        return len(stack)