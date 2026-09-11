from collections import Counter

class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        # 1. Count the frequencies of digits available in our pool
        available_counts = Counter(digits)
        unique_count = 0
        
        # 2. Loop through all possible 3-digit even numbers
        for num in range(100, 1000, 2):
            # Extract individual digits
            hundreds = num // 100
            tens = (num // 10) % 10
            units = num % 10
            
            # Count how many of each digit the current number requires
            required_counts = Counter([hundreds, tens, units])
            
            # 3. Check if we have enough copies of each required digit
            possible = True
            for digit, count in required_counts.items():
                if available_counts[digit] < count:
                    possible = False
                    break
            
            if possible:
                unique_count += 1
                
        return unique_count
