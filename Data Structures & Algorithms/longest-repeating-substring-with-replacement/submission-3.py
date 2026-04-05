class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        res=0
        d1=dict()
        r=0
        n=len(s)
        while r<n:
            d1[s[r]]=d1.get(s[r],0)+1

            if (r-l+1)-max(d1.values())>k:
                d1[s[l]]=d1.get(s[l])-1
                l+=1
            res=max(res,r-l+1)
            r+=1
        return res
