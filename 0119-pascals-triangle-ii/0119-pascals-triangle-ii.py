class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        triangle = [[1]]

        for i in range(1, rowIndex + 1):
            previous = triangle[-1]
            current = [1]

            for j in range(1, i):
                current.append(previous[j - 1] + previous[j])

            current.append(1)
            triangle.append(current)

        return triangle[rowIndex]