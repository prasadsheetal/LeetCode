class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_length,needle_length=len(haystack),len(needle)
        for i in range(haystack_length-needle_length+1):
            if haystack[i:i+needle_length]==needle:
                return i
        return -1