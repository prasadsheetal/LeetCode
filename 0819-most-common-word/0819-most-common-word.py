class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for c in "!?',;.":
                paragraph = paragraph.replace(c," ")
        banned_set = set(banned)
        words = paragraph.split()
        counts = {}
        max_word = " "
        max_freq = 0

        for word in words:
            if word not in banned_set:
                counts[word] = counts.get(word,0 ) + 1
                if counts[word] > max_freq:
                    max_freq = counts[word]
                    max_word = word
        return max_word