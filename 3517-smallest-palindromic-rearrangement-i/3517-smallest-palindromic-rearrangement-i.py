class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        
        # Get the first half of the string
        half_len = n // 2
        first_half = list(s[:half_len])
        
        # Sort the first half alphabetically to ensure it's the lexicographically smallest
        first_half.sort()
        
        # Reconstruct the sorted first half as a string
        left_side = "".join(first_half)
        
        # The right side is a perfect mirror image of the left side
        right_side = left_side[::-1]
        
        # If the string length is odd, insert the middle character in between
        if n % 2 != 0:
            middle_char = s[half_len]
            return left_side + middle_char + right_side
        else:
            return left_side + right_side

        