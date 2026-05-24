class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1=dict()
        d2=dict()

        for i in s:
            d1[i]=d1.get(i,0)+1
        
        for j in t:
            d2[j]=d2.get(j,0)+1
        
        if d1==d2:
            return True
        return False