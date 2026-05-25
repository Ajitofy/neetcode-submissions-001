from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1=defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            d1[sorted_word].append(word)
        return list(d1.values())