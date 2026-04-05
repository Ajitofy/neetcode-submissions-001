class Solution:
    def groupAnagrams(self, arr: List[str]) -> List[List[str]]:
        l1=[]
        l2=[]
        l=0
        r=1
        n=len(arr)
        for i in range(n):
            present =False
            for k in l1:
                if arr[i] in k:
                    present=True
            if not present:
                l2.append(arr[i])
            else:
                continue
            print("in i loop: l2",i,l2)
            for j in range(i+1,n):
                if sorted(arr[i])==sorted(arr[j]):
                    l2.append(arr[j])
                    # arr.remove(j)
            l1.append(l2.copy())
            print("l1 begore l2 clear",l1)
            l2.clear()
            print("after clear",l1)
        return l1
        
        