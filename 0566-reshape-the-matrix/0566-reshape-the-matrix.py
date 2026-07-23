class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        if rows * cols != r * c:
            return mat

        reshaped = [[0] * c for _ in range(r)]

        for i in range(rows):
            for j in range(cols):
                position = i * cols + j
                new_row = position//c
                new_col = position % c

                reshaped[new_row][new_col] = mat[i][j]

        return reshaped
        