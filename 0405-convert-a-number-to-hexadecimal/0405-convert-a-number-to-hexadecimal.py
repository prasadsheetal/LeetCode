class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        num &= 0xffffffff

        hexChars = "0123456789abcdef"
        result = []

        while num:

            digit = num % 16
            result.append(hexChars[digit])

            num //= 16

        return "".join(result[::-1])
        