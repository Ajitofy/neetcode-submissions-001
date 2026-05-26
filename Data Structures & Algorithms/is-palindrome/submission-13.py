class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        t=""
        for i in s:
            if i.isalnum():
                t+=i
            else:
                continue
        print(t) 
        l=0
        r=len(t)-1
        
        while t and t[l].lower() == t[r].lower() and l<r:
            l+=1
            r-=1
        print(l,r)
        if l==r or l>r:
            return True
        else:
            return False    
            
