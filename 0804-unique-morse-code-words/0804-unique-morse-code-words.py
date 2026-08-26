class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
            "....", "..", ".---", "-.-", ".-..", "--", "-.",
            "---", ".--.", "--.-", ".-.", "...", "-", "..-",
            "...-", ".--", "-..-", "-.--", "--.."
        ]

        transformations = set()

        for word in words:
            code = []

            for char in word:
                index = ord(char) - ord('a')
                code.append(morse[index])

            transformations.add("".join(code))

        return len(transformations)
        