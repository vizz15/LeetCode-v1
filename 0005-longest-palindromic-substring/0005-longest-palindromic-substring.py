class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0
        
        def expand_around_center(left: int, right: int) -> int:
            # Expand outwards as long as characters match and indices are valid
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the found palindrome
            return right - left - 1

        for i in range(len(s)):
            # Odd length palindromes (like "aba", center is 'b')
            len1 = expand_around_center(i, i)
            # Even length palindromes (like "bbacabb", center is between 'a' and 'c')
            len2 = expand_around_center(i, i + 1)
            
            max_len = max(len1, len2)
            
            # If we found a longer palindrome, update our tracking boundaries
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start : end + 1]
