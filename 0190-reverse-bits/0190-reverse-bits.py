class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        for _ in range(32):
            bit = n & 1
            answer <<= 1
            answer |= bit
            n >>= 1

        return answer
        