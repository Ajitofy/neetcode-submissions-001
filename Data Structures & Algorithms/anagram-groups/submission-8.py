class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1=defaultdict(list)
        
        for i in strs:
            sorted_str=''.join(sorted(i))
            d1[sorted_str].append(i)
        return list(d1.values())
