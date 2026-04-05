class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=len(s1)-1
        d1={}
        for i in s1:
            d1[i]=d1.get(i,0)+1
        if s1:
            while r<len(s2):
                var=s2[l:r+1]
                d2={}
                for i in var:
                    if i in d1:
                        d2[i]=d2.get(i,0)+1
                
                if d1==d2:
                    return True
                r+=1
                l+=1
            return False
        else:
            return False
        