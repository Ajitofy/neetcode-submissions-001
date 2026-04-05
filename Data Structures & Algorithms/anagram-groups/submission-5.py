from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        create list
        loop thorough each word,create hashmap and populate in dict
        """
        d1=defaultdict(list)
        
        for word in strs:
            count=[0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            d1[tuple(count)].append(word)
        return list(d1.values())