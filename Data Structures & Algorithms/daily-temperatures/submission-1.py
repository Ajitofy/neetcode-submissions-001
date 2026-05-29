class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        l=r=0
        res=[]
        while r<len(temp):
            while r<len(temp) and  temp[l]>=temp[r]:
                if r==len(temp)-1:
                    res.append(0)
                    l+=1
                    r=l+1
                else:
                    r+=1
            if r<len(temp) and temp[l]<temp[r]:
                res.append(r-l)
                l+=1
                r=l+1
        res.append(0)
        return res