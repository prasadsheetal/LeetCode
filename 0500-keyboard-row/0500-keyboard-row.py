class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")

        result = []

        for word in words:
            letters = set(word.lower())

            if (
                letters <= first_row
                or letters <= second_row
                or letters <= third_row
            ):

                result.append(word)

        return result        