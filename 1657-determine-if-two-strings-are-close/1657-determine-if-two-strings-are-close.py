class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
            
        freq1 = [0] * 26
        freq2 = [0] * 26

        for char in word1:
            freq1[ord(char) - ord('a')] += 1

        for char in word2:
            freq2[ord(char) - ord('a')] += 1

        for i in range(26):
            if (freq1[i] == 0) != (freq2[i] == 0):
                return False

        return sorted(freq1) == sorted(freq2)