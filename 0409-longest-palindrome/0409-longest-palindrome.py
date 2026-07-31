from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        has_odd = False
        
        for count in counts.values():
            # Add all possible pairs for this character
            length += (count // 2) * 2
            # Check if there is a remainder to use as a center
            if count % 2 == 1:
                has_odd = True
                
        # If at least one character had an odd count, 
        # we can place it in the unique center of the palindrome
        if has_odd:
            length += 1
            
        return length
