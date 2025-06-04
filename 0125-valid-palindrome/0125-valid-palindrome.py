class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=[]
        for ch in s:
            if ch.isalnum():
                s1.append(ch.lower())
        s=''.join(s1)
        rev=s1[::-1]
        return s1==rev
        