class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sToT = {}
        tToS = {}

        for chS, chT in zip(s,t):
            if chS in sToT:
                if sToT[chS]!= chT:
                    return False

            else:
                sToT[chS]= chT

            if chT in tToS:
                if tToS[chT] != chS:
                    return False
            else:
                tToS[chT] = chS
        return True
        