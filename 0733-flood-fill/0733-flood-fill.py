class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old = image[sr][sc]

        if old == color:
            return image

        rows,cols = len(image), len(image[0])
        stack = [(sr,sc)]

        image [sr][sc] = color

        while stack:
            r,c = stack.pop()

            for nr,nc in ((r - 1, c), (r + 1, c),
            (r,c -1), (r, c + 1)):

                if (0 <= nr < rows and 0 <= nc <cols and image[nr][nc] == old):
                    image[nr][nc] = color
                    stack.append((nr,nc))
        
        return image