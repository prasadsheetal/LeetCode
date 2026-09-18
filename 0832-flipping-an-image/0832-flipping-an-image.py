class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            left, right = 0, len(row) - 1
            while left <= right:
           
                if row[left] == row[right]:
                    row[left] ^= 1
                    if left != right:
                        row[right] ^= 1
                left += 1
                right -= 1
            
        return image