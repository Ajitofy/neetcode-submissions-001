class Solution:

    def encode(self, strs: List[str]) -> str:
        # if strs:
        s1=''
        for i in strs:
            s1+=str(len(i))+'#'+i
        print(s1)
        return s1
        # else:
        #     # print(s1)
        #     return strs
    def decode(self, s: str) -> List[str]:
            # if s:
            res,i=[],0
            print('s:',s)
            while i<len(s):
                j=i
                num=''
                print(i,j)
                while s[j]!='#':
                    num+=s[j]
                    j+=1
                print('i,j,num:',i,j,num)
                res.append(s[j+1:j+int(num)+1])
                print('res:',res)
                i=j+int(num)+1
            return res
            # else:
                # return 