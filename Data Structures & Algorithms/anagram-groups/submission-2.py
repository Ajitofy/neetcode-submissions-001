from collections import defaultdict
class Solution:
    def groupAnagrams(self, arr: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        for s in arr:
            count=[0]*26 #a...z

            for c in s:
                count[ord(c)-ord('a')]+=1
            res[tuple(count)].append(s)
        return res.values()

        
        