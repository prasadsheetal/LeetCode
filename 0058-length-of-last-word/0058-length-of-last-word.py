class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len1 = 0

        s = s.strip()

        for i in range(len(s)):
            if s[i] == ' ':
                len1 = 0
            else:
                len1 += 1

        return len1
        