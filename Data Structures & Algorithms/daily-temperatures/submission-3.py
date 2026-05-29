class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n=len(temp)
        res=[0]*n
        stack=[]

        for i in range(n):
            curr_temp=temp[i]

            while stack and curr_temp>temp[stack[-1]]:
                past_index=stack.pop()
                res[past_index]=i-past_index
            
            stack.append(i)

        return res
