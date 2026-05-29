class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=r=0
        d1=dict()
        max_f=0
        longest=0
        
        while r<len(s):
            # for i in range(len(s)):
            d1[s[r]]=d1.get(s[r],0)+1
            win_len=r-l+1
        
            max_f=max(max_f,d1[s[r]])
            # print(win_len,max_f,k)
            if  win_len-max_f<=k:
                longest=max(longest,win_len)
                r+=1
            else:
                d1[s[l]]=d1.get(s[l])-1
                l+=1
                r+=1
            
            
        return longest
            