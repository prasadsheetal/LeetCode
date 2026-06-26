class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            last = 0

            while num:

                last += num % 10
                num //= 10
            
            num = last

        return num



        