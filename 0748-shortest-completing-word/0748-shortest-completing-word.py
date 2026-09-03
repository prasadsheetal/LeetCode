class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        required = Counter(
            ch.lower()
            for ch in licensePlate
            if ch.isalpha()
        )
        answer = ""

        for word in words:
            if answer and len(word) >= len(answer) :
                continue

            count = Counter(word)

            if all(count[ch] >= needed
                    for ch, needed in required.items()):
                answer = word

        return answer
