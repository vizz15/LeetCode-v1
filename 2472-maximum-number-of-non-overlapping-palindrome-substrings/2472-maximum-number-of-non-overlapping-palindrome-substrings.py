class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        intervals = []
        
        # Step 1: Find all valid palindromes of length k or k + 1 using center expansion
        for center in range(2 * n - 1):
            # If center is even: single character center (odd length palindrome)
            # If center is odd: between two characters center (even length palindrome)
            left = center // 2
            right = left + (center % 2)
            
            while left >= 0 and right < n and s[left] == s[right]:
                current_len = right - left + 1
                
                # We only need the shortest valid palindromes of length k or k + 1
                if current_len >= k:
                    intervals.append((left, right))
                    break # Stop expanding this center to keep intervals as short as possible
                    
                left -= 1
                right += 1
                
        # Step 2: Greedy interval scheduling (Select maximum number of non-overlapping intervals)
        # Sort intervals primarily by their end index
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        last_end = -1
        
        for start, end in intervals:
            # Check if the current interval starts after the last chosen interval ends
            if start > last_end:
                count += 1
                last_end = end # Update the boundary to the end of the current interval
                
        return count
