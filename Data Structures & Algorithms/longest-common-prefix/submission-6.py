class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref= ""
        for i in range(len(strs[0])):

            for j in strs:
                if len(j) > 0 and  i < len(j)  and strs[0][i] == j[i]:
                    continue
                else:
                    return pref
            pref += strs[0][i]
        return pref
