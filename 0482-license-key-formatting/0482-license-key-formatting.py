class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = s.replace("-","").upper()

        res = []
        count = 0

        for i in range(len(chars) -1,-1,-1):
            res.append(chars[i])
            count += 1

            if count == k and i != 0:
                res.append("-")
                count= 0

        return "".join(res[::-1])