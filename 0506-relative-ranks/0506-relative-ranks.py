class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)

        rank = {}

        for i, value in enumerate(sorted_scores):

            if i == 0:
                rank[value] = "Gold Medal"

            elif i == 1:
                rank[value] = "Silver Medal"

            elif i == 2:
                rank[value] = "Bronze Medal"

            else:
                rank[value] = str(i + 1)

        answer = []

        for value in score:
            answer.append(rank[value])

        return answer
        