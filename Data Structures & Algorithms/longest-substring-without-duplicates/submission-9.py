class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        l=0
        r=1
        n=len(s)
        s1=set()

        for r in range(n):
            while s[r] in s1:
                s1.remove(s[l])
                l+=1
            s1.add(s[r])
            res=max(res,len(s1))
        return res

        