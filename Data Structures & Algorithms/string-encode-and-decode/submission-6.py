class Solution:

    def encode(self, strs: List[str]) -> str:
        n=len(strs)
        s=''
        for i in strs:
            s=s+str(len(i))+"#"+i
        print(s)
        return s
        
    def decode(self, s: str) -> List[str]:
        l1=[]
        n=len(s)
        i=0
        while i<n:
            j=i
            while s[j]!="#":
                j+=1

            word_len=int(s[i:j])
            l1.append(s[j+1:j+1+word_len])
            i=j+1+word_len
        return l1
