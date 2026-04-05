class Solution:
    def isPalindrome(self, s: str) -> bool:
        l1=''
        for i in s:
            if i.isalnum():
                l1+=i.lower()
        if l1==l1[::-1]:
            return True
        else:
            return False
