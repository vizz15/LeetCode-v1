class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2

        left_sum = sum(int(c) for c in num[:mid] if c != '?')
        left_q = num[:mid].count('?')

        right_sum = sum(int(c) for c in num[mid:] if c != '?')
        right_q = num[mid:].count('?')

        delta_sum = left_sum - right_sum
        delta_q = right_q - left_q
        

        if delta_sum * 2 == delta_q * 9:
            return False  # Bob wins
            
        return True  # Alice wins

        