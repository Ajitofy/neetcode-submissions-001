class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        final=0
        for i in tokens:
            if i in ['+','*','-','/']:
                if i == '+':
                    final=stack[-2]+stack[-1]
                elif i == '-':
                    final=stack[-2]-stack[-1]
                elif i == '*':
                    final=int(stack[-2]*stack[-1])
                elif i == '/':
                    final=int(stack[-2]/stack[-1])
                stack.pop()
                stack[-1]=final

            else:
                stack.append(int(i))
        return stack[-1]