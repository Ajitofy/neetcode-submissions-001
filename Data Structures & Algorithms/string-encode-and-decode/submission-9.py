class Solution:

    def encode(self, strs: List[str]) -> str:
        enc=''
        for i in strs:
            enc+=str(len(i))+"#"+i
        return enc
    def decode(self, s: str) -> List[str]:
        res=[]
        l=0
        n=len(s)
        while l<n:
            j=l
            while s[j]!="#":
                j+=1
            
            k=int(s[l:j])
            res.append(s[j+1:j+1+k])
            print(res)
            l=j+1+k
        return res

