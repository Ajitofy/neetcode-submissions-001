class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1 = set()
        l=0
        r=0
        longest=0
        
        while l<=r and r<(len(s)):
            if s[r] not in s1:
                s1.add(s[r])
                count=len(s1)
                longest = max(count,longest)
                r+=1
            else:
                while s[l] != s[r]:
                    s1.remove(s[l])
                    l+=1
                s1.remove(s[l])
                l+=1
        return longest