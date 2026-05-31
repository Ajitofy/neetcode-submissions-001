class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1=defaultdict(list)
        for word in strs:
            count=[0]*26
            for i in word:
                index=ord(i)-ord('a')
                count[index]+=1
            d1[tuple(count)].append(word)
        return list(d1.values())