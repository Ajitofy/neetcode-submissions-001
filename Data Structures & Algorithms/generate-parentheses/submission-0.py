class Solution:
    def generateParenthesis(self, no: int) -> List[str]:
        stack=[]
        res=[]

        def backtracking(openN,closeN):
            # base condition: open == close == n
            # add ( when open<no
            # add ) when  close < open

            if openN==closeN==no:
                res.append("".join(stack))
                return
            if openN<no:
                stack.append("(")
                #openN+=1
                backtracking(openN+1,closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                #closeN+=1
                backtracking(openN,closeN+1)
                stack.pop()

        backtracking(0,0)
        return res