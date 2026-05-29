class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d1=dict()
        l=0
        longest=0
        max_f=0
        for r in range(len(s)):
            d1[s[r]]=d1.get(s[r],0)+1
            max_f=max(max_f,d1[s[r]])

            
            while ((r-l+1) - max_f) > k:
                d1[s[l]]-=1
                l+=1
            longest=max(longest,r-l+1)
        return longest
        
        