from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        # 1. Validate if a palindrome is possible
        odd_chars = [char for char, count in counts.items() if count % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        # 2. Extract the mid character if length is odd
        mid = odd_chars[0] if odd_chars else ""
        if mid:
            counts[mid] -= 1
            
        # Divide remaining counts by 2 to generate the left-half character pool
        for char in counts:
            counts[char] //= 2
            
        half_len = n // 2
        path = []
        
        # 3. Backtracking function to build the optimal left half
        def backtrack(idx, is_greater):
            if idx == half_len:
                # Mirror the left half to create the full candidate palindrome string
                left_str = "".join(path)
                full_palindrome = left_str + mid + left_str[::-1]
                
                # Check if it satisfies the strictly greater condition
                if full_palindrome > target:
                    return full_palindrome
                return ""
            
            # Try every character from 'a' to 'z' greedily for a minimal lexicographical layout
            for ascii_val in range(ord('a'), ord('z') + 1):
                char = chr(ascii_val)
                
                if counts[char] > 0:
                    # If not yet greater, we cannot pick a character smaller than target[idx]
                    if not is_greater and char < target[idx]:
                        continue
                        
                    # Choose character
                    counts[char] -= 1
                    path.append(char)
                    
                    # Update status if this choice makes our current path strictly greater than target
                    next_greater = is_greater or (char > target[idx])
                    
                    result = backtrack(idx + 1, next_greater)
                    if result: 
                        return result  # Early return the first valid sequence found
                        
                    # Backtrack (Undo choice)
                    path.pop()
                    counts[char] += 1
                    
            return ""

        return backtrack(0, False)
