from collections import defaultdict
class Solution:
    def groupAnagrams(self, arr: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in arr:
            count=[0]*26 # as there are 26 lowercase alphabets
            for j in i:
                count[ord(j)-ord('a')]+=1
        
            res[tuple(count)].append(i)
        return res.values()
        