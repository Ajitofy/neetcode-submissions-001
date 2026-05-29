class Solution:
    def calPoints(self, op: List[str]) -> int:
        stack=[]

        for i in op:
            try:
                new=int(i)
                stack.append(new)
            except:
                if i == "+":
                    new= stack[-1]+stack[-2]
                    stack.append(new)
                elif i == "C":
                    stack.pop()
                    # print(stack)
                else:
                    new=stack[-1]*2
                    stack.append(new)
                
        sum=0
        for num in stack:
            sum+=num
        return sum