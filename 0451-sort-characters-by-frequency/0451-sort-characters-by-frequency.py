class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        return "".join(char * count for char, count in counts.most_common())
        