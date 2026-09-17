class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        result = []
        start = 0
        n = len(s)

        for i in range(n + 1):
            if i == n or s[i] != s[start]:
                if i - start >= 3:
                    result.append([start,i - 1])
                start = i

        return result
        