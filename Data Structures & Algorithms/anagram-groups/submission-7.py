class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            if tuple(count) in res:
                res[tuple(count)].append(word)
            else:
                res[tuple(count)] = [word]
        return list(res.values())