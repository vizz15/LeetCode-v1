class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split("-"))
        days_passed = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        total = days_passed[month] + day
    
    # Add 1 if it's a leap year and we passed February
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400   == 0)
        if month > 2 and is_leap:
            total += 1
        
        return total

        
        