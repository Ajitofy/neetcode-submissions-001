class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        res=0

        for i in tokens:
            if i == "+":
                add=stack.pop()+stack.pop()
                stack.append(add)
            elif i == "*":
                mul=stack.pop()*stack.pop()
                stack.append(mul)
            elif i == "-":
                first=stack.pop()
                second=stack.pop()
                sub=second-first
                stack.append(sub)
            elif i == "/":
                first=stack.pop()
                second=stack.pop()
                div = int(second/first)
                stack.append(div)
            else:
                stack.append(int(i))
        return stack[-1]