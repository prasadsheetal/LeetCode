class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])

        daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

        answer = sum(daysInMonth[:month-1]) + day

        isLeap = (
            (year % 400 == 0) or 
            (year % 4 == 0 and year % 100 !=0)
        )

        if isLeap and month > 2:
            answer += 1

        return answer